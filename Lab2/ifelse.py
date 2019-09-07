def grade_average(grade):
    if grade >= 90:
        return "4"
    elif (grade<=89) and (grade>=80):
        return "3"
    elif (grade<=79) and (grade>=70):
        return "2"
    elif (grade<=69) and (grade>=60):
        return "1"
    else:
        return "0"
print(grade_average(92))



