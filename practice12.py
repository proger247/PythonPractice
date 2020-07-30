# Задание 12.6.1

x = (67 + 33) * (25 - 20) / 25
print(f'Значение {x}')

print('--'*40)


# Задание 12.6.2

matrix = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
matrix[3][1] = 6
print(matrix)

print('--'*40)


# Задание 12.6.3

a1 = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
a2 = {1, 2}
a3 = {6, 7, 8}
a4 = {1}
a5 = {3, 4, 5, 6}

print(a2 | a4)
print(a1 - a5)
print(a2 ^ a3)
print(a1 & a2 & a3 & a4 & a5)

print('--'*40)


# Задание 12.6.5

word = input("Enter any word!\n")

if word == word[::-1]:
	print(f'The word {word} is polindrome.')
else:
	print(f"The word {word} isn't polindrome.")

print('--'*40)


# Задание 12.6.5

email = input('Enter an email adress!').split()
email_output = {}

for i in email:
	print(i)

	if i.count('@') != 1: 
		result = False
	elif len(i[0 : i.find("@")]) < 2:
		result = False
	elif ("." in i[i.find("@") + 1 : ]) == False :
		result = False
	elif len(i[i.find("@") + 1 : i.find(".")]) < 2 :
		result = False
	elif len(i[i.find(".") + 1 : ]) < 2 :
		result = False
	else:
		result = True
		
	email_output[i] = result

print(email_output)


