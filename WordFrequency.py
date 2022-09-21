File = open('sometext.txt','r') 
#print(File.read())
Dictionary = {}
#print(Dictionary)

for x in File: 

    x = x.lower()
    x = x.replace(',','')
    x = x.replace('.','')

    words = x.split(" ")

    for word in words: 
        if word in Dictionary: 
            Dictionary[word] = Dictionary[word]+1
        
        else: 
            Dictionary[word] = 1

for key in list(Dictionary.keys()):
    print(key, ':', Dictionary[key])

print(Dictionary)




File.close()