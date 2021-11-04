from codecs import open
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
  teg = massiv[0].replace('\t','')
  if teg[0] == '"':
    soderjimoe = massiv[1]
    if soderjimoe[-4] + soderjimoe[-3] != '],':
      xml += '<' + teg[1:len(teg)-1] + '>'
    if soderjimoe[1] == '"' and soderjimoe[-4] + soderjimoe[-3] != '],':
      xml += soderjimoe[2:len(soderjimoe)-4] + '</' + teg[1:len(teg)-1] + '>' + "\n" + "\t"
    if ord(soderjimoe[1]) >= 47 and ord(soderjimoe[1]) <= 58:
    	xml += soderjimoe[1:len(soderjimoe)-3] + '</' + teg[1:len(teg)-1] + '>' + "\n" + "\t"
    if soderjimoe[1] == '[':
      if line[-3] == '[':
        xml += "\n" + "\t"
        const_teg = teg[1:len(teg)-1]
      else:
        weeks = soderjimoe[2:len(soderjimoe)-4].split(',')
        for c in weeks:
          xml += '<' + teg[1:len(teg)-1] + '>' + c + '</' + teg[1:len(teg)-1] + '>' + '\n' + '\t'
  if '},' in line:
    xml += '</' + const_teg + '>' + '\n' + '\t'
    xml += '<' + const_teg + '>' + '\n' + '\t'
  if '}' in line:
    if line [0] != '}' and line[-3] == '}':
      xml += '</' + const_teg + '>' + '\n'
file = open("raspisanie.xml",'w','utf_8_sig')
file.write(xml)
file.close()