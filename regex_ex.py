import re
'''
match
search
findall
split
sub
compile - finditer
'''
line='pet:cat i love cat pet:dog i love dog'
# matches=re.match('.{3}:CAT',line,re.I)
# print(matches.group())

# matches=re.search('pet:...',line)
# print(matches)

# matches=re.findall('pet:.{3}',line)
# print(matches)

#print(re.split(' ',line))
#print(re.sub('love','like', line))

mystr='''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMOPQRSTUVWXYZ
1234567890

~!@#$%^&*()_+

https://www.google.com
http://www.amazon.com
https://ford.com
https://www.gs.co.in

438-245-3214
435_566_5466
754.324.2311
233 545 6334

raghulramesh@gmail.com
raghul.ramesh@gmail.com
raghul_ramesh@gmail.com
raghul@gmail.co.in

Ha HaHa

'''
#pattern=re.compile(r'.')
#pattern=re.compile(r'https?://(www.)?\w+.com?(.in)?')
#pattern=re.compile(r'\d{3}[\-\.\s]\d{3}[\-\.\s]\d{4}')
#pattern=re.compile(r'(\w+\.)?\w+@gmail\.com?(\.in)?')
# pattern=re.compile(r'\bHa\b')
# result=pattern.finditer(mystr)
# for x in result:
#     print(x.group())

mobile='''
+91-9939952599
9939952599
99399525999
993995259
8939952599
7939952599
6939952599
5939952599
4939952599
3939952599
2939952599
1939952599
'''
pattern=re.compile(r'(\+91\-)?\b[6-9]\d{9}\b')
res=pattern.finditer(mobile)
for x in res:
    print(x.group())