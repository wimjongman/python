import os
import encoder

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
    file.write("words,index,frequency,abstracts\n")
        
    for word in codes:
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
    
    
    

def main(selected_file):
    choice = intro(selected_file)
    if choice == 1:
        selected_file = select_file()
        if len(selected_file) == 0:
            print('')
            print('Goodbye!')
            return
    elif (choice == 2) and (len(selected_file) != 0):
        encoder.encode(selected_file, words, codes, abstr_freqs,
                       total_freqs, abstracts, encodedAbstracts)
        print()
        print("--------------------")
        print("Found " + str(len(words)) + " unique words")
        print("in " + str(len(abstracts)) + " abstracts.")
        print("--------------------")
        
    elif (choice == 3) and (len(selected_file) != 0):
        write_files(selected_file, words, abstr_freqs,
                    total_freqs, encodedAbstracts)

    elif choice == 0:
        print('')
        print('Goodbye!')
        return
    main(selected_file)

words, codes, abstr_freqs, total_freqs = {}, {}, {}, {}
abstracts, encodedAbstracts = {}, {}

main('')
