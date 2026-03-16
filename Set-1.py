s1={'Math', 'Physics', 'Chemistry'}
s2={'Physics', 'Biology', 'Math'}
print('Common subjects are:', s1.intersection(s2))
print('Subjects taken by only first student is:', s1-s2)
print('Subjects taken by only second student is:', s2-s1)
print('Total unique subjects are:', (s1^s2 | s1&s2))
