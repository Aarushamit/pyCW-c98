filePath = input("enter the path of the file you want to open: ")
fileOpener = open(filePath, "r")
def wordCounter():
    wordCount = 0
    for character in fileOpener:
        words = character.split()
        wordCount = wordCount+len(words)

    print(wordCount)

wordCounter()
    
