# Crtl+/ (TO UNCOMMENT AND COMMENT BLOCKS OF TEXT)
print('Hello World')
print('What is your name?')
myName = input();
print('It is good to meet you, ' + myName);
print('The length of your name is: ')
print(len(myName))
print('What is your age?')
myAge = input();
print('You will be '+str(int(myAge) + 1) + ' in a year.')

if (int(myAge) >= 25):
    print('You are old!')
else:
    print('You are young!')
