# my_file = open('someInfo','w')
# massive = [1, 2, 3]
# my_file.write('d;d;qwd;')
# # lis_t = file.readlines()

# print('file contains', file = my_file)


# with open('', 'wb') as fobject:
# 	

# Reading JSON-files 
import json


# with open('example.json', encoding = 'utf-8') as f:
# 	info = json.load(f)
# print(info)


# Writing in JSON-files
template = {
	'firstname': 'Ivan',
	'lastname': 'Komelkov',
	'isAlive': 'True',
	'age': 32,
	'address':{
		'streetaddress': 'Fontanka 20',
		'city': 'Saint-Petersburg',
		'country': 'Russian Federation',
		'postalcode': 'zip'
	},
	'phonenumbers': [
		{
			'type': 'mob',
			'number': '+7 923 023 2344'
		}
	],
	'spouse': None
}
with open('example.json', 'w', encoding = 'utf-8') as f:
	json.dump(template, f, ensure_ascii = False, indent = 4)
with open('example.json', encoding = 'utf-8') as f:
	info = json.load(f)
print(info['phonenumbers'][:]['number'])
