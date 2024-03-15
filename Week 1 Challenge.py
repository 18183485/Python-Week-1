#Num is assigned value 9
num = 9 
#Iterate through numbers from 1 to 'num' (inclusive)
for i in range(1, num+1):
    #'i' will be adjusted by subtracting half of num plus 1
    i = i - (num//2 + 1)
    #if 'i' is negative make it positive
    if i < 0:
        i = -i
    #print spaces 'i' times, then '*' characters, then spaces 'i' times.
    print(" " * i + "#" * (num - i * 2) + " " * i)