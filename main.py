numbers = [1,2,3]
new_numbers = [n + 1 for n in numbers]
print(new_numbers)

#Square each number from list
squared_numbers = [n * n for n in numbers]
print(squared_numbers)

#Converts list of string arr to int arr 
#and then finds even numbers
numbersStr = ['1','2','3','4','5']
con_to_int = [int(n) for n in numbersStr]
print(con_to_int)
result = [n for n in con_to_int if n % 2 == 0]
print(result)

#Square each number from list
squared_numbers = [n * n for n in numbers]
print(squared_numbers)

#Ouput names.len less than 5
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
short_names = [name for name in names if len(name) < 5]
print(short_names)

#Uppercase names.len longer than 5
long_names = [name.upper() for name in names if len(name) > 5]
print(long_names)
