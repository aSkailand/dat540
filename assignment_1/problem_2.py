import string

birthday = '16-04-1994'
file = 'plain.txt'

def encryptFile():
    fileData = list(getFileData(file).lower())
    alphabetList = list(string.ascii_lowercase)
    index = 0

    for character in fileData:
        if (character in alphabetList):
            alphabetIndex = alphabetList.index(character.lower())
            if ((alphabetIndex + 4) >= len(alphabetList)):
                deltaIndex = -len(alphabetList[alphabetIndex:-1]) + 3
                fileData[index] = alphabetList[deltaIndex] 
            else:
                fileData[index] = alphabetList[alphabetIndex + 4]
        index += 1
    encryptedString = ''
    for letter in fileData:
        encryptedString += letter
    print(encryptedString)
    

def getFileData(filePath):
    with open('plain.txt') as file:
        return file.read()



if __name__ == "__main__":
    encryptFile()