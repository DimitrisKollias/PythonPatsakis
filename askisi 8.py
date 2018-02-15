import random

numbers = []

strings_f =[]
final_out =[]


ans = int(input("press 1 to use random int or press 2 to use random float"))
entered = False
if (ans == 1 or ans == 2):
    entered = True

while (entered == False):
    ans = input("wrong\n")
    if (ans == 1 or ans == 2):
        entered = True
    


for i in range(30):


    if (ans == 1):
        numbers.append(random.randint(-30,30))

    elif (ans == 2):
        numbers.append(random.uniform(-30,30))




for i in range(30):
    for j in range(1+1,30):

        for k in range(1+2,30):
            suM = numbers[i]+numbers[j]+numbers[k]
            
            if (suM == 30):
                
                text2 = str(numbers[i]) + " + " + str(numbers[j]) + " + " + str(numbers[k]) + " = " + str(suM)
                strings_f.append(text2)
                    

size = len(strings_f)

exists = []
for i in range(size):
    exists.append(0)

for i in range(size-1):
    for j in range(i+1, size):
        if (strings_f[i] == strings_f[j]):
            exists[j] = 1
        
not_found = True
for i in range(size):
    if (exists[i]==0):
        print(strings_f[i])
        not_found = False

if (not_found == True):
    print("den yparxei tetoios syndiasmos")

