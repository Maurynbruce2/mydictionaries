Text = open('info_security.txt','r')
Encryption = open('encrypted.txt','w')
reader = Text.read()




code = {'A':'~','B':'!','C':'@','D':'#','E':'$',
'F':'%','G':'^','H':'&','I':'*','J':'(','K':')','L':'_','M':'+',
'N':'`','O':'2','P':'3','Q':'4','R':'5','S':'6','T':'7','U':'8','V':'9',
'W':'0','X':'-','Y':'=','Z':'{','a':'}','b':'|','c':'[','d':']','e':':',
'f':';','g':'"','h':',','i':'.','j':'<','k':'>','l':'/','m':'?','n':'01',
'o':'02','p':'03','q':'04','r':'05','s':'06','t':'07','u':'08','v':'09',
'w':'+=','x':'<>','y':'<3','z':':)',' ':''} 


for x in reader: 
    x = x.strip()
    letters = list(x)

    if x in code: 
        Encryption.write(code[x])

    else: 
        Encryption.write(x)


    
Text.close()

Encryption.close()