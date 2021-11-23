# Q1)
# Already installed python


#------------------------------------------

# Q2)

a=5**9
print(a)

a=3//2
print(a)


a=7//3
print(a)


a=7/3
print(a)

print(6==6)


a=20
a+=30
a%=3
print(a)


print(True*False)
print(True & False)
print(True and False)
print((6>3) and (7<4) or (18==3) and (9>3))
print(True is False)

# print(False in 'False')                           #Type error-left operand should be of <string>


print((True==False) or  (False>True)) and (False <=True)

# Q3)


s1="Nice to have it"
s2="here"
print(s1,s2)


#Q4)

a=[1,2,[3,4],[5,[100,200,['Hello']],23,11],1,7]
print(a[3][1][2][0])


#Q5)



a.insert(0,s1)
a.append(s2)
print(a)


#Q6)


numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 
953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 
687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 
742, 717, 958,743, 527]
for i in numbers:
    if i < 238 and i%2==0:
        print(i)
            
                


#Q7)
            

color_list_1 = set(["White", "Black", "Red"]) 
color_list_2 = set(["Red", "Green"])

print(color_list_1 - color_list_2)


# Q9)

n=int(input('Enter the value of n:' ))
num1 = str(n)
num2 = num1 + num1
num3 = num2 + num1
print(int(num1) + int(num2) + int(num3))




# Q11)
phrase = input("Input words: ")
phrase_list = phrase.split(",")
phrase_list.sort()
print((', ').join(phrase_list))



# Q12)
phrase=input("Enter the phrase:")
phrase=list(phrase)
l=d=0
for i in phrase:
    if i.isalpha():
        l=l+1
    elif i.isdigit():
        d=d+1
    else:
        pass
print("The number of letters are:",l)
print("The number of digits are:",d)



# Q13)


string3=(input("enter the sentence"))
letters=0
digits=0
for i in string3:
    if(i.isalpha()):
        letters+=1
    if(i.isdigit()):
        digits+=1
print("LETTERS",letters)
print("DIGITS",digits)



# Q14)

string3=(input("enter the sentence"))
letters=0
digits=0
for i in string3:
    if(i.isalpha()):
        letters+=1
    if(i.isdigit()):
        digits+=1
print("LETTERS",letters)
print("DIGITS",digits)
      

            
