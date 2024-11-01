import json


# Parse the JSON file `coca60000_freq.json` and filter out only the English words.
# [
#   {
#     "headword": "and",
#     "content": [
#       {
#         "PoS": "conjunction",
#         "Rank": "3",
#         "Freq": "24778098"
#       },
#       {
#         "PoS": "noun",
#         "Rank": "36203",
#         "Freq": "220"
#       }
#     ]
#   },
# ]
# Freq is the sum of all frequencies of the PoS.
# Sort by frequency in descending order.
# Output:
# ```txt
# word|rank
# ...
# ```

def process_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    word_freq = {}
    for entry in data:
        headword = entry['headword']
        total_freq = sum(int(content['Freq']) for content in entry['content'])
        word_freq[headword] = total_freq
    
    sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
    
    rank = 1 
    with open('coca60000-rank.txt', 'w') as output_file:
        for word, freq in sorted_words:
            output_file.write(f"{word}|{rank}\n")
            rank += 1

if __name__ == "__main__":
    process_json('coca60000_freq.json')