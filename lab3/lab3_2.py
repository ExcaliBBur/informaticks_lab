import re

Test1 = 'Довольно распространённая ошибка ошибка – это лишний повтор повтор слова слова. Смешно, не не правда ли? Не нужно портить хор хоровод.'
Test2 = 'orange red blue green orange green blue'
Test3 = 'pirates ninjas cowboys ninjas pirates'
Test4 = 'привет привет как как дела дела. У меня нормально нормально, а у тебя?'
Test5 = '1234 1234 kak kak kak 1234 ghbdtn'
Massiv = []
Massiv.append(Test1)
Massiv.append(Test2)
Massiv.append(Test3)
Massiv.append(Test4)
Massiv.append(Test5)
k = 1
for p in Massiv:
	if len(p) != 0:
		p_regex = p
		p_python = p
		result = re.findall(r'\b(\w+)\s\1\b',p_regex)
		for i in result:
			p_regex = re.sub(i,'',p_regex,1)
			p_regex = re.sub(r'\s{2}',' ',p_regex)
			p_regex = re.sub(r'^\s','',p_regex)
		massiv = p_python.split(' ')
		flag = 0
		for i in range(len(massiv)-1):
			if massiv[i][-1] in '.?!,-' and len(massiv[i]) >= 2:
				temp = massiv[i][:-1]
				flag = 1
			if massiv[i] == massiv[i+1]:
				massiv.pop(i)
				massiv.append(' ')
			if flag == 1 and massiv[i-1] == temp:
				massiv.pop(i-1)
				massiv.append(' ')
				flag = 0
		a = ''
		for i in massiv:
			if i != ' ':
				a += i + ' '
		if (a == p_regex + ' '):
			print(f'Test{k} прошёл успешно, автор молодец.')
			print(a)
		else:
			print(f'Test{k} прошёл некруто, автор переделывай.')
			print(a)
			print(p_regex)
		k += 1
	else:
		print('Ты меня не обманешь!(строки нет)')
		k += 1