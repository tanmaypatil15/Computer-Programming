#WAP in python that read a text file and counts the number of times a certain letter appers in the text file.
f1=input("Enter file name in 'txt' extension: ")
l=input("Enter the letter to be search in file: ")
letter_count=0
word_count=0
line_count=0
with open(f1, 'r') as f:
    print("Contents in file are:")
    print(f.read())
with open(f1, 'r') as f:
    for line in f:
        line_count=line_count+1
        words= line.split()
        for i in words:
            word_count=word_count+1
            for letters in i:
                if letters==l:
                    letter_count = letter_count + 1
print("Number of lines present:",line_count)
print("Number of words present:",word_count)
print("Occurence of entered letter is",letter_count)

