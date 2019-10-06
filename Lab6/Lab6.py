x = False
a = 0
while not x :
    print(a)
    a+=5
    if a ==55:
        x = True
    else:
        continue

c = False
string = "Count the spaces in this sentence"
counter = 0
while not c :
    for i in string:
        if i == ' ' or i == '\n':
            counter += 1
print(counter)

count = 0
total = 0
Grade = "y"
while Grade != "n":
    grade = int(input("Enter grades here.: "))
    for eachPass in range(grade):
        count = count + 1
        total = total + grade
        print('eachPass: {}, total: {}'.format(eachPass, total))
    Grade = input ("Are there any more grades to enter, if not then enter stop ")
    if Grade == "stop":
        print("The average is", round(total / count, 1))
        break


S = input("Input a word: ")

def isPalindrome(S):
    for i in range(0, len(S)):
        if S[0 + i] == S[len(S) - 1]:
            return "True"
        else:
            return "False"
print(isPalindrome(S))


