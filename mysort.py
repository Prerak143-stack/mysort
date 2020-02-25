# I am Prerak Patel and I have designed this program by myself and I haven't share
# my program with anyone. My professor's name is Tiffany, Anotopoloski

myList = input("Please enter the unsorted list to sort it : ")

number_count = 0
comma_count = 0
real_list = []
for number in myList :
    if number.isdecimal():

        if number_count == comma_count:
            number_count += 1
            real_list += [number]
        
        else:
            real_list[number_count - 1] += number


    elif number is ",":
        comma_count += 1



while number_count > 0 :
    counter2 = 1
    while counter2 < number_count :

        if int(real_list[counter2 - 1]) > int(real_list[counter2]):
            temp = real_list[counter2 - 1]
            real_list[counter2 - 1] = real_list[counter2]
            real_list[counter2] = temp
            
        counter2 += 1
        
    number_count -= 1

print(real_list)
            
