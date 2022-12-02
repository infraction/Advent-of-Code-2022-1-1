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

def Find_Top_3(file):
    highest_sums = [0,0,0]
    check_sum = 0

    for line in file:
        if line.startswith('\n'):
            if check_sum > highest_sums[0]:
                highest_sums[0] = check_sum
                highest_sums.sort()
            check_sum = 0
        else:
            check_sum += int(line)
    top3 = highest_sums[0]+highest_sums[1]+highest_sums[2]
    return top3

print(Find_Top_3(test))