x = input("Enter text: ")

alphabet_lc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

alphabet_uc = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']


ret = ""
for i in range(len(x)):

    
    try:
        index = alphabet_lc.index(x[i])
        index = index + 13
        if (index>25):
            index = index - 26
        ret = ret + alphabet_lc[index]
        continue
    except ValueError:
        try:
            index = alphabet_uc.index(x[i])
            
            index = index + 13
            if (index>25):
                index = index - 26
            ret = ret + alphabet_uc[index]
            continue
        except ValueError:
            ret = ret + x[i]
            continue
    

print(ret)

    
    
