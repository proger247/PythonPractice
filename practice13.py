list_len = int(input('Введите длину ряда!'))
my_list = []
summary = 0

while list_len > 0:
	my_list.append(list_len)
	list_len -= 1

for number in my_list:
	if number % 2 != 0:
		summary += number
print(summary)
