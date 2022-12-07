# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    marks = []
    i=0
    while i < len(grades):
        if grades[i] >= 38 and grades[i] % 5 > 2:
            grades[i] += 5 - (grades[i] % 5)
            marks.append(grades[i])
        elif (grades[i] < 38) or (grades[i] >= 38 and grades[i] % 5 < 3):
            marks.append(grades[i])
        i+=1
    return marks
