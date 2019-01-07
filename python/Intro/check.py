def which_prize(points):
    #noprize=1
    if 0<=points<=50:
        prize= "wooden rabbit"
        no_prize=0
    elif 151<=points<=180:
        prize="wafer-thin mint"
        no_prize=0
    elif 181<=points<=200:
        prize="penguin"
        no_prize=0
    else:
        no_prize=1

    if no_prize==1:
        messege='"Oh dear, no prize this time."'
    elif no_prize==0:
        messege='"Congratulations! you have won a {}!"'.format(prize)
    return messege


print(which_prize(12))
print(which_prize(149))
print(which_prize(169))
print(which_prize(194))
