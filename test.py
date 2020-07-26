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

text = "It sportsman earnestly ye preserved an on. Moment led family sooner cannot her window pulled any. Or raillery if improved landlord to speaking hastened differed he. Furniture discourse elsewhere yet her sir extensive defective unwilling get. Why resolution one motionless you him thoroughly. Noise is round to in it quick timed doors. Written address greatly get attacks inhabit pursuit our but. Lasted hunted enough an up seeing in lively letter. Had judgment out opinions property the supplied."
text = text.replace(" ","").lower()
most_popular = None
qty_most_popular = 0

for symbol in text:
	qty = text.count(symbol)
	if qty > qty_most_popular:
		qty_most_popular = qty
		most_popular = symbol

print(f'Наиболее встречаемая буква {most_popular} имеет {qty_most_popular} вхождений')



