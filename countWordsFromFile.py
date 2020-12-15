def countWordsFromFile():
    wordCounter = 0
    fileName = input("Enter the file name / path")
    f = open(fileName, 'r')
    #lines = f.readlines()

    for line in f:
        words = line.split()
        print(words)
        wordCounter = wordCounter+len(words)

    print("Number of Words: " + str(wordCounter))

countWordsFromFile()