def compression_rate():
    file = open()
    










































def encodenumber():
    slash = '\\'
    counter = 0
    getal = ''
    word = ''
    alles = ''
    getal = getal + ' '
    for letter in getal:
        if (letter.isnumeric() == True) & (counter > 0):
            word = word + letter
        if (letter.isnumeric() == True) & (counter == 0):
            word = word + slash + letter
            counter = counter + 1
        if (letter.isnumeric() == False) & (letter != ' ') & (letter.isalpha() == False):
            word = word + letter
            counter = 0
        if letter == ' ':
            word = word + letter
            alles = alles + word
            word = ''
            counter = 0
    print(alles)
             
    
         
def number_backslash():
    slash = '\\'
    openfile = open("input.txt")
    word = ''
    for letter in openfile.read():
        if letter.isnumeric() == True:
            word += slash + letter
        elif letter == slash:
            word += '\\\\'
        else:
            word += letter
    return word



def x():
    slash = '\\'
    openfile = open("input.txt")
    word = ''
    for letter in openfile.read():
        if letter == slash:
            word += '\\\\'
        else:
            word += letter
    print(word)
            
            
