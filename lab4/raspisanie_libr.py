from json2xml import json2xml
from json2xml.utils import readfromstring
from codecs import open
f = open('raspisanie.json','r','utf_8_sig').read()
data = readfromstring(f)
xml = json2xml.Json2xml(data).to_xml()
file = open('raspisanie_libr.xml','w','utf_8_sig')
file.write(xml)
file.close()