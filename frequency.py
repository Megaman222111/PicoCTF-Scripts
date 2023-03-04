# Program to get letter count in a text file
 
# explicit function to return the letter count
def letterFrequency(fileName, letter):
    # open file in read mode
    file = open(fileName, 'r')
 
    # store content of the file in a variable
    text = file.read()
 
    # using count()
    return text.count(letter)
 
 
# call the function and display the letter count
print('a: ', letterFrequency('study-guide.txt', 'a'))
print('b: ', letterFrequency('study-guide.txt', 'b'))
print('c: ', letterFrequency('study-guide.txt', 'c'))
print('d: ', letterFrequency('study-guide.txt', 'd'))
print('e: ', letterFrequency('study-guide.txt', 'e'))
print('f: ', letterFrequency('study-guide.txt', 'f'))
print('g: ', letterFrequency('study-guide.txt', 'g'))
print('h: ', letterFrequency('study-guide.txt', 'h'))
print('i: ', letterFrequency('study-guide.txt', 'i'))
print('j: ', letterFrequency('study-guide.txt', 'j'))
print('k: ', letterFrequency('study-guide.txt', 'k'))
print('l: ', letterFrequency('study-guide.txt', 'l'))
print('m: ', letterFrequency('study-guide.txt', 'm'))
print('n: ', letterFrequency('study-guide.txt', 'n'))
print('o: ', letterFrequency('study-guide.txt', 'o'))
print('p: ', letterFrequency('study-guide.txt', 'p'))
print('q: ', letterFrequency('study-guide.txt', 'q'))
print('r: ', letterFrequency('study-guide.txt', 'r'))
print('s: ', letterFrequency('study-guide.txt', 's'))
print('t: ', letterFrequency('study-guide.txt', 't'))
print('u: ', letterFrequency('study-guide.txt', 'u'))
print('v: ', letterFrequency('study-guide.txt', 'v'))
print('w: ', letterFrequency('study-guide.txt', 'w'))
print('x: ', letterFrequency('study-guide.txt', 'x'))
print('y: ', letterFrequency('study-guide.txt', 'y'))
print('z: ', letterFrequency('study-guide.txt', 'z'))