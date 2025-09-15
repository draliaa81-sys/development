# Author Sana Alyaseri
# class: software development 
# Example 4 :Accessing a global variable
count = 0
def increment():
    global count #declare'count' as global
    count += 1
    print(f"count inside function: {count}")

#call the function
increment()
increment()

#Access the global variable
print(f"count outside function:{count}")