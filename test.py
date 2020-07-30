# a = float(input('Введите два значения'))
# b = float(input('Введите два значения'))
# c = float(input('Введите два значения'))

# p = (a + b + c) / 2
# print ('Значение периметра',p)

# def square_func(a,b,c,p):

# 	square = (p * (p - a) * (p - b) * (p - c)) ** (1 / 2)

# 	print("Значение площади",round(square,10))

# square_func(a,b,c,p)

# a = 'dsfsfdsfdsfsdsdf'
# print(a.find('stringw'))


# # Калькулятор прибыли по вкладу 
# amount = float(input("Введите сумму займа"))
# months = float(input("Введите срок займа(мес.)"))

# percent = 4.18  # годовая процентная ставка 
# percent_for_month = 2.15 / 12
# profit = 0
# years = months % 12  # перевод количества месяцев в количество лет 


# while months > 0:
# 	profit  = amount * percent_for_month / 100 + profit
# 	amount += profit
# 	months -= 1
# else:
# 	print ("Ваш доход по вкладу:", profit)
 
# # Working with lists 

# a = []
# t = 1 

# for i in range(4):
# 	b = []
# 	for j in range(3):
# 		b.append(t+j)
# 	t += 3
# 	a.append(b)
# print(a) 


# searching most popular letter in text 

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum eget tempus est. Phasellus sit amet tristique neque. Sed luctus mi ut nisi suscipit placerat. Nunc nec diam dapibus, fermentum risus ut, ultrices orci. Integer non magna molestie nibh dapibus tincidunt. Quisque quis est quam. Sed dictum mi sit amet magna pretium blandit. Nulla tortor turpis, maximus vitae lobortis quis, varius sed metus. Nullam at congue metus. Pellentesque scelerisque, dui et luctus semper, odio diam scelerisque justo, nec tempor ex metus et enim. Praesent rhoncus nisl eget risus elementum ornare. Praesent tellus mauris, viverra vitae malesuada at, ornare id nisi. Vestibulum."

text = text.replace(" ", "").lower().replace(".", "")
text_set = set(text)
most_popular = None
second_popular  = None
qty_most_popular = 0
qty_second = 0

# for symbol in text:
# 	qty = text.count(symbol)
# 	print(f"{symbol} --- {qty}")
# 	if qty > qty_most_popular:
# 		qty_most_popular = qty
# 		most_popular = symbol
# 	else: 
# 		qty > qty_second
# 		second_popular = symbol
# 		qty_second = qty
# 	text = text.replace(f"{symbol}", "")

for symbol in text_set:
	qty = text.count(symbol)
	print(f"{symbol} --- {qty}")
	if qty > qty_most_popular:
		qty_most_popular = qty
		most_popular = symbol
		if qty_second > qty_most_popular:

			qty_most_popular = qty_second
			most_popular = symbol
		else: 
		
			second_popular = symbol
			qty_second = qty
	# text = text.replace(f"{symbol}", "")

print(f'Наиболее встречаемая буква {most_popular} имеет {qty_most_popular} вхождений')
print(f'Вторая наиболее встречаемая буква {second_popular} имеет {qty_second} вхождений')
# 




