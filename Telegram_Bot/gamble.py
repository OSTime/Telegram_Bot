import random

points = 1000

def bet(msg):
    
    #0 -- !bet
    #1 -- amount (int)
    #2 -- high or low
    split = msg.split()
    if len(split) < 2:
        error = 'Invalid Command \n Try: !bet amount high/low'
        return error
    else:
        if split[0] == '!bet':
            try:
                int(split[1])
            except:
                return error
            if split[2] == 'high' or split[2] == 'low':
                msg = 'success'
                
                msg = roll(split[1], split[2])
                return msg
	#roll = random.randint(1, 100)
	#print(roll)

def roll(amount, high_low):
    is_high = False
    
    if high_low == 'high':
        is_high = True
    
    roll = random.randint(1,100)
    msg = 'Rolled: ' + str(roll) + '\n\n'
    if is_high and roll >= 50:
        msg += 'You won: ' + str(amount) + '!'
    else:
        msg += 'You lost: ' + str(amount) + ' :('
    
    return msg
