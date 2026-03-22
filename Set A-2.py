#Accept a paragraph from the user. Create a set of unique words.Display
#the number of unique words and display the common words between two sentences.

p=input('Enter paragraph: ')
sent=p.split('.')
s1=sent[0].split()
s2=sent[1].split()
unique=set(p.split())
print('Unique words are:', unique)
print('No. of unique words:', len(unique))
print('Common word between two sentences is:', set(s1)&set(s2))
