import re
import pygame

# =<| - смайлик
print('Номер ИСУ = 335989')
print('335989 % 5 =',335989%5,';','335989 % 4 =',335989%4,';','3354989 % 7 =',335989%7)
print('Мой смайлик - "=<|"')
Test1 = '=<|=<|=<|=<|=<|=<|=<|=<|=<|=<|=<|=<|=<|=<|=<|=<|=<|=<|=<|=<|=<|'
Test2 = '=<|=<|:-)=<X|=<|'
Test3 = 'X-{O8<{P=<|=<'
Test4 = ''
Test5 = '12341235123049878123047123074123087410237401923874-12375r01347059124091237084517230846'
Mass = []
k = 1
Mass.append(Test1)
Mass.append(Test2)
Mass.append(Test3)
Mass.append(Test4)
Mass.append(Test5)
for i in Mass:
	result_regex = len(re.findall(r'=<\|', i))
	result_python = i.count('=<|')
	counter = result_regex
	if result_regex == result_python:
		if counter % 100 >= 11 and counter % 100 < 20:
			print(f'Test{k} прошёл успешно, в тексте всего {result_regex} смайликов "=<|".')
		elif counter % 10 == 1:
			print(f'Test{k} прошёл успешно, в тексте всего {result_regex} смайлик "=<|".')
		elif counter % 10 == 2 or counter % 10 == 3 or counter % 10 == 4:
			print(f'Test{k} прошёл успешно, в тексте всего {result_regex} смайликa "=<|".')
		else:
			print(f'Test{k} прошёл успешно, в тексте всего {result_regex} смайликов "=<|".')
	else:
		print(f'Test{k} не прошёл, автор сделал что-то не так, исправляй.')
	k += 1
print('Для рисовалки смайлика тыкните Enter')
_ = input()
s = 1
while s:
	pygame.init()
	keys = pygame.key.get_pressed()
	pygame.display.set_caption('Рисовалка смайлика')
	win = pygame.display.set_mode((700,500))
	pygame.draw.line(win,(255,255,255),(100,210),(250,210),7)
	pygame.draw.line(win,(255,255,255),(100,230),(250,230),7)
	pygame.draw.line(win,(255,255,255),(270,220),(420,150),7)
	pygame.draw.line(win,(255,255,255),(270,220),(420,290),7)
	pygame.draw.line(win,(255,255,255),(470,110),(470,330),7)
	for k in pygame.event.get():
		if k.type == pygame.QUIT:
			s = False
	if keys[pygame.K_ESCAPE]:
		s = False
	pygame.display.update()
