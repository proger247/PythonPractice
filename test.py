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

amount = float(input("Введите сумму займа"))
months = float(input("Введите срок займа(мес.)"))

percent = 2.15  # годовая процентная ставка 
percent_for_month = 2.15 / 12
profit = 0
years = months % 12  # перевод количества месяцев в количество лет 


while months > 0:
	profit  = amount * percent_for_month / 100 + profit
	amount += profit
	months -= 1
else:
	print ("Ваш доход по вкладу:", profit)



