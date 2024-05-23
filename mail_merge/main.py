#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
        
def getNames(fileName):
    names = []
    with open(fileName) as f:
        data = f.read()
        names = data.splitlines()
        
    return names
        
def getStartingLetter(fileName):
    with open(fileName) as f:
        data = f.read()
        return data
    
    
def writeToFile(fileName, dataString):
    with open(fileName, 'w') as f:
        f.write(dataString)
    
def main():
    names = getNames('./Input/Names/invited_names.txt')
    template = getStartingLetter('./Input/Letters/starting_letter.txt')
    
    outputFilePath = './Output/ReadyToSend/'
    
    for name in names:
        newLetter = template.replace('[name]', name.strip())
        print(newLetter)
        writeToFile(outputFilePath + name.strip() + '.txt', newLetter)
        

    
    
    
    
main()
    
    
    