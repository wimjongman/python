def store_word(word, abstract_nr, abstr_freqs, total_freqs, codes, words):

    if not word in codes:
        wordCount = len(words) + 1
        words[wordCount] = word
        codes[word] = wordCount

    if word.lower() != word:
        if not word.lower() in codes:
            codes[word.lower()] = 0        

    if not word.lower() in total_freqs:
        total_freqs[word.lower()] = 1
    else:
        total_freqs[word.lower()] += 1
    
    if not abstract_nr in abstr_freqs:
        abstr_freqs[abstract_nr] = {}
    
    if not word.lower() in abstr_freqs[abstract_nr]:
        abstr_freqs[abstract_nr][word.lower()] = 1
    else:
        abstr_freqs[abstract_nr][word.lower()] += 1
        
def encode(file_name, words, codes,  abstr_freqs, total_freqs,
           abstracts, encodedAbstracts):
    word = ''
    abstractCount = 0
    file = open(file_name)
    for abstract in file.readlines():
        coded=''
        abstracts[abstractCount] = abstract;
        for char in abstract:
            if char.isalpha():
                word += char
                continue
            if char.isnumeric():
                coded += '\\' + char
                continue
            if char == '\\':
                coded += '\\' + char
                continue
            if word == '':
                coded += char
                continue
            
            store_word(word, abstractCount, abstr_freqs, total_freqs,
                       codes, words)
            coded += str(codes[word]) + char
            word =  ''

        if word != '': 
            store_word(word, abstractCount, abstr_freqs, total_freqs,
                       codes, words)
            coded += str(codes[word])

        encodedAbstracts[abstractCount] = coded
        coded=''
        abstractCount += 1
