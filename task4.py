# Author Sana Alyaseri
# class: software development 
# Example 6 : functions where one fuction calls anther to take the result and do further processing.

def add(a,b):
    return a + b

def multiply(x,y):
    return x * y

def add_and_multiply(a, b ,c):
    sum_result = add(a, b) #calling the add function
    product_result = multiply(sum_result, c) # calling the multiply function
    return product_result

    
result = add_and_multiply(2, 3, 4)
print(result)#output:20