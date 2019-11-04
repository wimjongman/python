import os

def intro(selected_file):
    print('')
    print('Welcome to Abstracts')
    print('')
    if len(selected_file) != 0:
        print('Selected file is ' + selected_file)
        print('')
    print('1: Load input file')
    print('2: Process file')
    print('3: Save output file')
    print('0: Exit program')
    print('')
    return int(input('Please type 1, 2, 3 or 0: '))

def list_dir():
    print('')
    print('Current directory: ' + os.getcwd())
    print('')
    menu = 1
    print('1: ../')
    files = {0:'',1: '../'}
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
    elif len(file_name) == 0:
        return ''
    else:
        return file_name
        
def main(selected_file):
    choice = intro(selected_file)
    if choice == 1:
        selected_file = select_file()
        if len(selected_file) == 0:
            print('')
            print('Goodbye!')
            return  
    elif choice == 0:
        print('')
        print('Goodbye!')
        return
    main(selected_file)

main('')

