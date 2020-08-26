character_count=0
word_count = 1
intro = input("What is your name?\n")
print(intro)

for i in intro:
    character_count = character_count+1


    if(i == " "):
        word_count = word_count+1


print ("number of words are",word_count)
print ("number of letters in the line are",character_count)
