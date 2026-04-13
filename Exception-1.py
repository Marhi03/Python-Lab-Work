try:
    def copy_content(source, destination):
     with open(source, 'r') as f1:
        content=f1.read()
     with open(destination, 'w') as f2:
        f2.write(content)
     f=open(r"C:\Users\lab\File2.txt", 'r')
     content1=f.readlines()
     print(content1)

    copy_content(r"C:\Users\lab\File.txt", r"C:\Users\lab\File2.txt")
    print('File copied')
except FileNotFoundError:
    print('File is not found')
