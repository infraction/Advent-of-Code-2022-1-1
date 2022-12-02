test = open('input.txt','r')



def Find_Highest_Calorie(file):
    highest_sum = 0
    check_sum = 0
    for line in file:
        if line.startswith('\n'):
            if check_sum > highest_sum:
                highest_sum = check_sum
            check_sum = 0
        else:
            check_sum += int(line)
    return highest_sum

print(Find_Highest_Calorie(test))