def function1(file_name):
    lines=0
    words=0
    characters=0
    with open(file_name, 'r') as file:
     for line in file:
        lines+=1
        word=line.split()
        words+=len(word)
        characters+=len(line)
    print(lines)
    print(words)
    print(characters)

function1(r"C:\Users\lab\File1.txt")
