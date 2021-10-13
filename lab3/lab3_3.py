import re

Test1 ='Классное слово – Обороноспособность, которое должно идти после слов: трава и молоко.'
Test2 = 'На самом деле я абсолютно не знаю. Что здесь писать?'
Test3 = ''
Test4 = '123 123 123'
Test5 = 'Я.Абсолютно.Не.Имею.фантазии.дЛя.таках.дЕл.'
Massiv = []
Massiv.append(Test1)
Massiv.append(Test2)
Massiv.append(Test3)
Massiv.append(Test4)
Massiv.append(Test5)
count = 1
for chto in Massiv:
	test = ''
	for i in chto:
		if ord(i) >= 1040 and ord(i) <= 1071:
			i = chr(ord(i) + 32)
		test += i
	result = re.findall(r'\b(\w*[аиеёоуыэюя]\w*)\b',test)
	result_regex = []
	for i in result:
		p = re.search(r'а|и|е|ё|о|у|ы|э|ю|я',i).group(0)
		p = re.sub(p,'',i)
		p = re.findall(r'\b(\w*[аиеёоуыэюя]\w*)',p)
		if len(p) == 0:
			result_regex.append(i)
	counter = 1 
	for k in range(len(result_regex)):
		for j in range(k,(len(result_regex))):
			if len(result_regex[j]) < len(result_regex[k]):
				result_regex[j],result_regex[k]=result_regex[k],result_regex[j]
	#проверка обычными средствами путхона
	massiv_obichn = []
	result_python = []
	a = ''
	for i in test:
		for j in i:
			if ord(j) >= 1072 and ord(j) <= 1103:
				a += j
			else:
				if a != '':
					if (a.count('а') + a.count('и') + a.count('е') + a.count('ё') + a.count('о') + a.count('у') + a.count('ы') + a.count('э') + a.count('ю') + a.count('я')) >= 1:
							massiv_obichn.append(a)
				a = ''
	for i in range(len(massiv_obichn)):
		for j in massiv_obichn[i]:
			temp = massiv_obichn[i]
			if (j == 'а' or j == 'и' or j == 'е' or j == 'ё' or j == 'о' or j == 'у' or j == 'ы' or j == 'э' or j == 'ю' or j == 'я'):
				temp = temp.replace(j,'')
				if (temp.count('а') + temp.count('и') + temp.count('е') + temp.count('ё') + temp.count('о') + temp.count('у') + temp.count('ы') + temp.count('э') + temp.count('ю') + temp.count('я')) == 0:
					result_python.append(massiv_obichn[i])
				break
	for k in range(len(result_python)):
		for j in range(k,(len(result_python))):
			if len(result_python[j]) < len(result_python[k]):
				result_python[j],result_python[k]=result_python[k],result_python[j]
	if result_python == result_regex and len(result_python) != 0:
		print(f'Test{count} прошёл успешно, автор молодец!')
		print('Ответ:',result_python)
	elif result_regex == result_python and len(result_python) == 0:
		print(f'Test{count} прошёл успешно, ответ - пустая строка.')
	else:
		print(f'Test{count} лоханулся, переделывать пора.')
		print('Обычный ответ:', result_python)
		print('Ответ через регулярки:',result_regex)
	count += 1