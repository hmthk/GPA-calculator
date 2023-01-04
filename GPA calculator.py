GPA_lst = {'A+': 4.3, 'A': 4.0, 'A-': 3.7, 'B+': 3.3, 'B': 3.0, 'B-': 2.7, 'C+': 2.3, 'C': 2.0, 'C-': 1.7, 'D+': 1.3,'D': 1.0, 'F': 0.0}
input_data = 0
divisor = 0
dividend = 0

print('This program is a GPA calculator especially designed for Hong Kong Polytechnic Univeristy students.\nPlease input your grade, the number of credits of the coures, and the weighting of each course.')
print('(For weighting, if the course code begins with \'1XXX\' or \'2XXX\', please input \'2\'. If it begins with \'3XXX\' or \'4XXX\', please input \'3\'.)')
print('For example, if you obtained an \'A\' in ENG2002 (3 credits), please input \'A, 3, 2\'(grade, credits, weighting).\n')

while input_data != 'done':
    input_data = input('Enter your grade, credits-bearing, and weighting of a course: ')
    if input_data == 'done': break
    try:
        grade, credits, weighting = input_data.split(', ' and ',' and ' ')
        weighting = float(weighting)
        credits = float(credits)
        grade = grade.upper()
        dividend += GPA_lst.get(grade) * credits * weighting
        divisor += credits * weighting
    except: print('Opps! It seems your input isn\'t compatible.')

total_GPA = dividend / divisor

try: print('Your weighted GPA is {}.'.format(total_GPA))
except: pass

if total_GPA >= 3.6 and total_GPA <= 4.30:
    print('With {} GPA, you will graduate with first-class honours.'.format(total_GPA))
elif total_GPA >= 3.0 and total_GPA <= 3.59:
    print('With {} GPA, you will graduate with second-class (division I) honours.'.format(total_GPA))
elif total_GPA >= 2.4 and total_GPA <= 2.99:
    print('With {} GPA, you will graduate with second-class (division II) honours.'.format(total_GPA))
elif total_GPA >= 1.70 and total_GPA <= 2.39:
    print('With {} GPA, you will graduate with third-class honours.'.format(total_GPA))
else:
    print('How did you get this level of GPA????????')

ans = input('Do you want to calculate the the minimum GPA required in the following courses to achieve a certain level of GPA? (Yes/No): ')
if ans == 'yes' or 'Yes':
    target_GPA = float(input('Enter your target GPA: '))
    remaining_weighting = float(input('Please add up the products of credits and weighting in each remaining course.\n(credits of course A * weighting of course A + credits of course B * weighting of course B + ...)\nEnter the calculated sum: '))
    future_GPA = (target_GPA * (divisor + remaining_weighting) - dividend) / remaining_weighting
    print('You need to obtain {} GPA in the remaining courses so as to get {} GPA'.format(future_GPA, target_GPA))