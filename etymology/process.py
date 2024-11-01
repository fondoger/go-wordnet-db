import csv

# NOTE:
# `etymology.csv` is a large file
# Downloaded from: https://github.com/droher/etymology-db

# Parse: `etymology.csv`
# Columns:
# term_id,lang,term,reltype,related_term_id,related_lang,related_term,position,group_tag,parent_tag,parent_position

# Filter: lang==English,related_lang==English
# Returns { term, related_term, reltype }


def stripword(word):
    return (''.join([ n for n in word if n.isalnum() ])).lower()

def pickLong(terms, a, b):
    if a == None:
        return b
    if b == None:
        return a
    assert(terms[a] != None)
    assert(terms[b] != None)
    if terms[a] > terms[b]:
        return b
    if terms[a] < terms[b]:
        return a
    if len(a) > len(b):
        return a
    return b

coca6000 = set()
with open('../coca60000/coca60000-rank.txt', mode='r', encoding='utf-8') as file:
    for line in file:
        word = line.split('|')[0]
        coca6000.add(stripword(word))

def filter_eng_eng_etymology():
    rows = []
    terms = {}
    with open('etymology.csv', mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if not(row['lang'] == 'English' and row['related_lang'] == 'English'):
                continue
            # term and related_term don't have spaces
            if row['reltype'] in ['etymologically_related_to']:
                continue
            if ' ' in row['term'] or ' ' in row['related_term']:
                continue
            if row['term'] == row['related_term']:
                continue
            if row['reltype'] == 'doublet_with':
                # `doublet_with` 表示具有相同的词源，但是不够直观看到联系
                #  week -> wick
                continue
            if row['reltype'] == 'back-formation_from':
                # `back-formation_from` 表示反向关系
                # investigate -> investigation
                continue
            if row['reltype'] == 'derived_from':
                # 不直观
                # jab -> job
                continue
            if row['reltype'] == 'cognate_of':
                # 听起来相似，或者意思相近，不直观
                # past -> pass
                continue
            if row['reltype'] == 'initialism_of':
                # 仅仅首字母有关系
                continue
            if row['reltype'] == 'clipping_of':
                # A 是 B 的口语缩短版本
                # dep -> department
                continue
            if row['reltype'] == 'abbreviation_of':
                # 简写
                continue
            if row['reltype'] == 'borrowed_from':
                # 不直观
                continue
            if row['reltype'] == 'initialism_of':
                # 不直观
                continue
            if row['reltype'] == 'blend_of':
                # 不直观
                continue
            if row['reltype'] == 'has_affix':
                # 剔除不包含完整词根的词(不够直观)
                if row['related_term'] not in row['term']:
                    continue

            row['term'] = stripword(row['term'])
            row['related_term'] = stripword(row['related_term'])
            rows.append(row)
            terms[row['related_term']] = terms.get(row['related_term'], 0) + 1
    
    # Sort rows by term
    rows = sorted(rows, key=lambda x: x['term'])

    results = {}
    reltypes = {}
    for row in rows:
        results[row['term']] = pickLong(terms, results.get(row['term'], None), row['related_term'])
        if results[row['term']] == row['related_term']:
            reltypes[row['term']] = row['reltype']
    # write back to `etymology-en.csv`,
    # Only keep ['term', 'related_term']
    reltype_set = set()
    termsNew = {}
    with open('etymology-en.csv', mode='w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['term', 'reltype', 'related_term'])
        for term, related_term in results.items():
            if related_term not in coca6000:
                continue
            if reltypes[term] == 'has_suffix' and related_term in ['in', 'ism', 'form', 'ie', 'lite', 'son']:
                # Skip common suffix, which is not the major meaning of the word
                continue
            writer.writerow({
                'term': term,
                'reltype': reltypes[term],
                'related_term': related_term
            })
            reltype_set.add(reltypes[term])
            termsNew[related_term] = termsNew.get(related_term, 0) + 1
            
    print("RelTypes:")
    print(reltype_set)
    print("Top 100 termsNew:")
    print(sorted(termsNew.items(), key=lambda x: x[1], reverse=True)[:100])


if __name__ == "__main__":
    filter_eng_eng_etymology()