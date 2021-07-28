# program for sorting 3 numbers
# Isaac D. 29/05/2021

# The first method uses the inbuilt function sorted() to achieve the request
first_num = input("Enter the first number: ")
second_num = input("Enter the second number: ")
third_num = input("Enter the third number: ")

first_num = int(first_num)
second_num = int (second_num)
third_num = int (third_num)

list_numbers = [first_num,second_num,third_num]
print (sorted(list_numbers,reverse=True))


# The second method doesnt make use of sorted() but rather uses a while and if function
new_list = []

while list_numbers: # While list_numbers means that while items still remains in list numbers
    # continue to run the iteration, you will notice that for every iteration we remove a value
    # called minimum from list_numbers
    
    minimum = list_numbers[0]  # arbitrary number in list, we initial set the minimum value in the
    # list as the first item.
    for x in list_numbers: 
        if x < minimum:
            minimum = x
    new_list.append(minimum)
    list_numbers.remove(minimum)    

print (new_list)
