#Creating function

'''Note: 1.For calling function directly we have to use print for result within function
         2.When we use return keyword for output first we have to store function in a variable and then print it '''

def calc_sum(a,b):   #a and b are parameters
    sums = a+b
    print(sums)
    
#calling the function
calc_sum(5,6)  #5 and 6 are arguments



def calc_sum(a,b):
    sums = a+b
    return sums
    
result = calc_sum(3,6)
print(result)



'''Notes:
        1.The variable which we pass in function at time of creation is called parameter
        2.While the values which we pass at time of calling function is called arguments'''


#Facts: The function which does not return any value is called void function and its output is always None
'''For example:
                def hello():
                    print("Hello World")
                result = hello()
                print(eresult)  #Output: None  '''