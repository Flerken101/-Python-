
with open('Chapter 9.py',encoding='gb18030',errors='ignore') as file_object:
    contents = file_object.read()

filename = 'Chapter 9.txt'

with open(filename,"w") as file_object:
    file_object.write(contents)
    words = file_object.split()
    words_number = len(words)
    print("The text has " + str(words_number) + " words.")