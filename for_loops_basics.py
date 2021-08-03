# Basic - Print all integers from 0 to 150. 
for x in range(0,151):
    print(x)

# Multiples of five - Print all the multiples of 5 from 5 to 1,000
num = 5
while num <= 1000:
    print(num)
    num = num + 5

# Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
for num in range(1,101):
    if num % 10 == 0:
        print("Coding Dojo")
    elif num % 5 == 0:
        print("Coding")
    else:
        print(num)

# Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000 and print the final sum. 
sum = 0
num = 500000
for num in range(0, num+1):
    if num % 2 == 1:
        sum += num
print("sum of odd numbers is " + str(sum))

# Countdown by fours - Print positive numbers starting at 2018, counting down by fours 
for x in range(2018,0,-4):
    print(x)

# Flexible Counter - Set thre variable: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a mult. FOr example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
lowNum = 12
highNum = 78
mult = 4
for count in range(lowNum,highNum+1,mult):
    if highNum % mult == 0:
        print(count)
    elif lowNum % mult == 0:
        print(count)