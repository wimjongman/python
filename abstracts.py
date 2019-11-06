import os
import math
import string

def intro(selected_file):
    print('')
    print('Welcome to Abstracts')
    print('')
    if len(selected_file) != 0:
        print('Selected file: ' + selected_file)
        print('Output file: ' + selected_file + '.output')
        print('Index file: ' + selected_file + '.index.CSV')
        print('')
    print('1: Load input file')
    print('2: Process file')
    print('3: Save output files')
    print('0: Exit program')
    print('')
    return int(input('Please type 1, 2, 3 or 0: '))

def list_dir():
    print('')
    print('Current directory: ' + os.getcwd())
    print('')
    menu = 1
    print('1: ../')
    files = {0:'', 1: '../'}
    for entry in os.listdir(os.getcwd()):
        if not entry.startswith('.'):
            menu = menu + 1
            if os.path.isdir(entry):
                entry = entry + '/'
            print(str(menu) + ': ' + entry)
            files[menu] = entry
    print('0: Exit program')
    choice = int(input('Please type 1 to ' + str(menu) + ' or 0: '))
    return files[choice]

def select_file():
    file_name = list_dir()
    if file_name.endswith('/'):
        os.chdir(file_name)
        return select_file()
    if len(file_name) == 0:
        return ''
    return file_name

def count_word_in_abstracts(word, abstr_freqs):
    count = 0
    for abstract_index in abstr_freqs:
        if word in abstr_freqs[abstract_index]:
            count += 1
    return count

def write_files(selected_file, words, abstr_freqs,
                    total_freqs, encodedAbstracts):
    output_file = selected_file + '.output'
    file = open(output_file, "w+")
    for abstract_index in encodedAbstracts:
        file.write(encodedAbstracts[abstract_index] + '\n')
    file.close()

    csv_file = selected_file + '.index.csv'
    file = open(csv_file, "w+")
    file.write("word,number,frequency,abstracts\n")

    index_size = 0
    for word in codes:
        index_size += len(word)
        if codes[word] == 0:
            continue
        file.write(word + ',')
        file.write(str(codes[word]) + ',')
        if word in total_freqs:
            file.write(str(total_freqs[word]) + ',')
            file.write(str(count_word_in_abstracts(word, abstr_freqs)) + '\n')
        else:
            file.write("0,")
            file.write("0\n")

    for word in codes:
        if codes[word] != 0:
            continue
        file.write(word + ',')
        file.write(str(codes[word]) + ',')
        if word in total_freqs:
            file.write(str(total_freqs[word]) + ',')
            file.write(str(count_word_in_abstracts(word, abstr_freqs)) + '\n')
        else:
            file.write("0,")
            file.write("0\n")

    file.close()
    
    orig_size = os.path.getsize(selected_file);
    output_size = os.path.getsize(output_file);
    # index_size = os.path.getsize(csv_file);
    
    comp_rate = math.floor((output_size + index_size) / orig_size * 100)
    print()
    print("--------------------")
    print("Found " + str(len(words)) + " unique words")
    print("in " + str(len(abstracts)) + " abstracts.")
    print("The compression rate is " + str(comp_rate) + "%")
    print("--------------------")

    words_per_letter = {}
    unique_words_per_letter = {}
    for letter in string.ascii_lowercase:
        words_per_letter[letter] = 0
        unique_words_per_letter[letter] = 0
        for word in total_freqs:
            if word[:1] == letter:
                if word.lower() == word:
                    words_per_letter[letter] += total_freqs[word]
                    unique_words_per_letter[letter] += 1 

    all_players = {}
    for letter in string.ascii_lowercase:
        all_players[letter] = letter
        
    weener_list = {}
    while len(weener_list) < 26:
        weener = next(iter(all_players))
        weener_freq = words_per_letter[weener]
        for letter in all_players:
            if letter == weener:
                continue
            if words_per_letter[letter] > weener_freq:
                weener = letter
                weener_freq = words_per_letter[letter]
        del all_players[weener]
        weener_list[weener] = weener_freq
        
    for letter in weener_list:
        print (letter + str(weener_list[letter]))


def main(selected_file):
    choice = intro(selected_file)
    if choice == 1:
        selected_file = select_file()
        if len(selected_file) == 0:
            print('')
            print('Goodbye!')
            return
 
    elif (choice == 2) and (len(selected_file) != 0):
        encode(selected_file, words, codes, abstr_freqs,
                       total_freqs, abstracts, encodedAbstracts)

    elif (choice == 3) and (len(selected_file) != 0):
        write_files(selected_file, words, abstr_freqs,
                    total_freqs, encodedAbstracts)

    elif choice == 0:
        print('')
        print('Goodbye!')
        return
    main(selected_file)
    
def store_word(word, abstract_nr, abstr_freqs, total_freqs, codes, words):

    if not word in codes:
        wordCount = len(words) + 1
        words[wordCount] = word
        codes[word] = wordCount

#    if word.lower() != word:
#        return
#        if not word.lower() in codes:
#            codes[word.lower()] = 0        

    myWord = word.lower()
    
    if not myWord in total_freqs:
        total_freqs[myWord] = 1
    else:
        total_freqs[myWord] += 1
    
    if not abstract_nr in abstr_freqs:
        abstr_freqs[abstract_nr] = {}
    
    if not myWord in abstr_freqs[abstract_nr]:
        abstr_freqs[abstract_nr][myWord] = 1
    else:
        abstr_freqs[abstract_nr][myWord] += 1
        
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
    
    ''' Put all cap words without lowercase in codes with code 0'''
    for index in words:
        word = words[index]
        low_word = word.lower()
        if low_word not in codes:
            codes[low_word] = 0

words, codes, abstr_freqs, total_freqs = {}, {}, {}, {}
abstracts, encodedAbstracts = {}, {}

main('')
