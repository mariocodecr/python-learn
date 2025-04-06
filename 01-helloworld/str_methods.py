

name = 'Mario Araya'
course = 'Python course'
name_upper = name.upper()
print(name == name_upper)  # Check if name is equal to uppercase name
print(name_upper)  # Print the uppercase name

print(name)
print(course.lower())  # Convert to lowercase

words = 'this is a course of python'
print(words.capitalize())
print(words.title())

words = '   Helllo Mario   '
print(words.strip())
print(words.lstrip())
print(words.rstrip())

text = 'Hello Java'
new_text = text.replace('Java', 'Python')
print(text)
print(new_text)  # Replace Java with Python

text = 'Mario, Araya, Python, Next, Nest'
data_list = text.split(',')
print(data_list[4])

data = ['Mario2, Araya2, Python2, Next2, Nest2']
text = ' '.join(data)
print(text)

text = 'Hello Mario, how are you?'
print(text.find('Mario'))
print(text.index('how'))

print(text.startswith('Hello'))
print(text.endswith('you?'))

number = '1234'
decimal = '1234.45'
text = 'Python'
mix = 'Python3'

print(number.isnumeric())
print(decimal.isdecimal())
print(mix.isalnum())
print(text.isalpha())

text = '   hello Mario how are you, welcome to the python course   '
text_clean = text.strip().capitalize().title()
print(text_clean)


new_text = text_clean.replace('Python Course', 'Python3 Course')
print(new_text)


words = new_text.split()
print(words)