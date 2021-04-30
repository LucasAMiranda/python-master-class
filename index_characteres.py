'''
s = input("please type some characteres and press enter: ")
for i in range(len(s)):
    print(s[i])
print("Lucas")
'''
# string in order reverse of characteres lists
'''
s = input("please type some characteres and press enter:")
for i in range(len(s)):
    print(s[i::-1])
print('hello')
'''
'''
s = input("please type some characteres and press enter: ")
for word in s.split():
    print(word)
print('hello, how are you?')
'''

# código que determina se você gosta de algo semelhante
# sophus Lie
'''
activity = input("what do you like to do? ")
liesActivities = ['math', 'hike', 'walk', 'gymnastics']
if activity in liesActivities:
    print('sophus like to do that , too!')
else:
    print('Good for you!')
'''
s = input('please enter a list of integers: ')
lst = s.split()

containsEven = True

for element in lst:
    x = int(element)

    if x % 2 == 0:
        containsEven = True

if containsEven:
    print("The list contained an even number")
else:
    print("The list did not contain an even number")
