first_name='hania'
last_name='ahmer'
full_name='hania_ahmer'
year='2024'
age='24'
is_true='yes'
is_married='false'
is_light_on ='true'
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
    'firstname':'hania', 
    'lastname':'ahmer', 
    'country':'pk',
    'city':'islamabad'
    }
print(first_name)
print(last_name)
print(full_name,age)
first_name_to_list = list(first_name)
print(first_name_to_list)   
# int to float
num_int = 10
print('num_int',num_int)         # 10
num_float = float(num_int)
print('num_float:', num_float)   # 10.0

# float to int
gravity = 9.81
print(int(gravity))             # 9

# int to str
num_int = 10
print(num_int)                  # 10
num_str = str(num_int)
print(num_str)                  # '10'

# str to int or float
num_str ='10'
print('num_int',int(num_str))      # 10
print('num_float',float(num_str))  # 10.6
print(first_name, last_name, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Age:', age)
print('Married: ', is_married)
#multiple varibles in one line

first_name, last_name, country, age, is_married = 'hania', 'ahmer', 'pk', 24, False
#use of length
print('First name length:', len(first_name))
print('Last name: ', len(last_name))
print('Skills: ', skills)
print('Person information: ', person_info)


#convert from int to float:
x = float(1)

#convert from float to int:
y = int(2.8)

#convert from int to complex:
z = complex(1)

print(x)
print(y)
print(z)

print(type(x))
print(type(y))
print(type(z))