characterCount = 0
wordCount = 1
intro = input("enter your introduction : ")

for character in intro:
    characterCount=characterCount+1

    if(character==" "):
        wordCount=wordCount+1
print(wordCount)
print(characterCount)



