#roll the dice game in python
import random
roll_die='yes'
min_value=1
max_value=6
while roll_die=='yes' or roll_die=='y':
    value1=random.randint(min_value,max_value)
    value2=random.randint(min_value,max_value)
    print('value of the dice:',value1," ",value2)
    roll_die=input("wish to play again? type yes or y ")
    
