#Create a function called factorial, argument num
def factorial(num):
    #res variable stores the factorial value
    res = 1
    #loop iterates over a range of numbers from 2 to num
    for i in range(2, num+1):
        #Multiplis current value of res by loop variable I
        #Assign it back to res 
        res *= i
    #Returns final calculated factorial value 
    return res

num = 5
print(factorial(num))