def match_words(words):
    ctr = 0
    list = []
    for word in words: 
        if len(word) > 1 and word [0] == word[-1]:
            ctr += 1 
            list.append(word)
            print("Words that match are:", list)
            return ctr 

count = match_words (['bac', 'abc', 'xyz', '1234', '2110'])
print("Number of words that match are:", count)