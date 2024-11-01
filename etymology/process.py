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

coca6000 = set()
with open('../coca60000/coca60000-rank.txt', mode='r', encoding='utf-8') as file:
    for line in file:
        word = line.split('|')[0]
        coca6000.add(stripword(word))

def filter_eng_eng_etymology():
    results = []
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
            row['term'] = stripword(row['term'])
            row['related_term'] = stripword(row['related_term'])
            if row['term'] not in coca6000 or row['related_term'] not in coca6000:
                continue
            results.append(row)
    # write back to `etymology-en.csv`,
    # Only keep ['term', 'reltype', 'related_term']
    with open('etymology-en.csv', mode='w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['term', 'reltype', 'related_term'])
        for row in results:
            writer.writerow({
                'term': row['term'],
                'reltype': row['reltype'],
                'related_term': row['related_term']
            })

def parse_etymology_csv(file_path):
    results = []
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            results.append({
                'term': row['term'],
                'related_term': row['related_term'],
                'reltype': row['reltype']
            })
    return results

if __name__ == "__main__":
    filter_eng_eng_etymology()
    # etymology_data = parse_etymology_csv("etymology-en.csv")
    # for entry in etymology_data:
    #     if entry['term'] == 'correctly':
    #         print(entry)