

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