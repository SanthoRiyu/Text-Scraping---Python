import re


text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
900-555-199
524-555-199


cat
mat
bat
pat

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net

https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

sentence = 'Start a sentence and then bring it to an end'

# pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
#pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d')
#pattern = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d')
# pattern = re.compile(r'[1-5]')
# pattern = re.compile(r'[a-zA-Z0-9]')
# pattern = re.compile(r'[^a-zA-Z]')
# pattern = re.compile(r'[^b]at')
# pattern = re.compile(r'\d{3}.\d{3}.\d{3,4}')
# pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')
# pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*')
# pattern = re.compile(r'[a-zA-Z0-9_+-.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
# pattern = re.compile(r'https?://(www\.)?\w+\.\w+')
# pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
#
#
# matches = pattern.finditer(text_to_search)
# for match in matches:
#     print(match.group(0))
#     print(match.group(1))
#     print(match.group(2))
#     print(match.group(3))
#
# subbed_urls = pattern.sub(r'\2\3', text_to_search) # \2\3 are group numbers whih will be replaced
# print(subbed_urls)

# print ('\tTab')

# pattern = re.compile(r'\d\d\d\W\d\d\d\W\d\d\d\d')
#pattern = re.compile(r'\d\d\d[-.*]\d\d\d[-.*]\d\d\d\d')
#pattern = re.compile(r'\d\d\d[^-.]\d\d\d[^-.]\d\d\d\d')
# pattern = re.compile(r'[89]00[-.*]\d\d\d[-.*]\d\d\d\d')
# pattern = re.compile(r'[^a-zA-Z]')
# pattern = re.compile(r'[^b]at')
# pattern = re.compile(r'\d{3}[-.*]\d{3}[-.*]\d{4}')
# pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')
# pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*')
# pattern = re.compile(r'[0-9a-zA-Z.-]+@[a-zA-Z-]+\.(com|edu|net)')
# pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
# pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')

# subbed_url = pattern.sub(r'\2\3',text_to_search)
# print (subbed_url)
#
# matches = pattern.finditer(text_to_search)
#
# for match in matches:
#     print(match.group(0))
#     print(match.group(1))
#     print(match.group(2))
#     print(match.group(3))

# matches = pattern.findall(text_to_search)
# for match in matches:
#     print(match)

# pattern = re.compile(r'sentence')
#
# matches = pattern.match(sentence)
#
# print(matches)

pattern = re.compile(r'start', re.IGNORECASE)

matchers = pattern.search(sentence)
print(matchers)
