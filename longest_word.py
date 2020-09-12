sentence=input("enter any sentence")
print(sentence)
words=sentence.split()
print(words)
long_word_length=len(words[0])
for i in words:
    word_length=len(i)
    if word_length > long_word_length:
        long_word_length=word_length
        currentword=i
print("longest word is:",currentword)
print("length is:",long_word_length)

