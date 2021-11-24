from codecs import open
import re
f = open('raspisanie.json','r','utf_8_sig')
xml = '<?xml version="1.0" encoding="UTF-8" ?>\n<root>\n\t'
while 1:
  line = f.readline()
  if not line:
    xml += '</root>' 
    break
  counter = 0
  teg = ''
  massiv = line.split(':',1)
  teg = re.sub('\t','',massiv[0])
  if teg[0] == '"':
    soderjimoe = massiv[1]
    if soderjimoe[-4] + soderjimoe[-3] != '],':
      xml += '<' + teg[1:len(teg)-1] + '>'
    if soderjimoe[1] == '"' and soderjimoe[-4] + soderjimoe[-3] != '],':
      xml += soderjimoe[2:len(soderjimoe)-4] + '</' + teg[1:len(teg)-1] + '>' + "\n" + "\t"
    if ord(soderjimoe[1]) >= 47 and ord(soderjimoe[1]) <= 58:
        xml += soderjimoe[1:len(soderjimoe)-3] + '</' + teg[1:len(teg)-1] + '>' + "\n" + "\t"
    if soderjimoe[1] == '[' or soderjimoe[1] == '{':
      if line[-3] == '[' or line[-3] == '{':
        xml += "\n" + "\t"
        const_teg = teg[1:len(teg)-1]
      else:
        weeks = soderjimoe[2:len(soderjimoe)-4].split(',')
        for c in weeks:
          xml += '<' + teg[1:len(teg)-1] + '>' + c + '</' + teg[1:len(teg)-1] + '>' + '\n' + '\t'
  p = re.findall('},',line)
  p1 = re.findall(r'}[^,]',line)
  if len(p) != 0:
    xml += '</' + const_teg + '>' + '\n' + '\t'
    xml += '<' + const_teg + '>' + '\n' + '\t'
  if len(p1) != 0:
    xml += '</' + const_teg + '>' + '\n'
file = open("raspisanie_regex.xml",'w','utf_8_sig')
file.write(xml)
file.close()