#class Telegram_Profiles():
def __init__(self, name):
    self.points = 1000
    self.name = name

#adds 100 points to everyone once every 24 hours
def daily_points(profile_list):
    for profile in profile_list:
        p.points += 100
    
    return profile_list

#returns how many points the person who called this command has
def get_points(f_name, points):
    #print('You have ' + str(points) + ' Points!')
    if f_name == 'Layne':
        f_name = 'Dirt'
    elif f_name == 'Britton':
        f_name = 'Brit'
    elif f_name == 'Sick':
        f_name = 'Nick'
    return str(f_name) + ' has ' + str(points) + ' Points'

#converts real names into nick names
#changes names to respective keys in dictionary
def name_converter(f_name):
    if f_name == 'Layne':
        f_name = 'Dirt'
    elif f_name == 'Britton':
        f_name = 'Brit'
    elif f_name == 'Sick':
        f_name = 'Nick'
    return f_name
    
#resets everyones points to 1000
#returns a dictionary
def restart_points():
    profile_dict = {
        'Daniel' : 1000, 
        'Dirt' : 1000, 
        'John' : 1000, 
        'Brit' : 1001, 
        'Sam' : 1000, 
        'Luke' : 1000, 
        'Josh' : 1000, 
        'Nick' : 0.0001,
        'Mickenley' : 1000, 
        'Ethan' : 1000, 
        'Jack' : 1000
    }
    
    
    return profile_dict

#returns how many points everyone has
def get_all_points(profile_dict):
    msg = ''
    for name, points in profile_dict.items():
        #print('Name: ' + name + ' Points: ' + str(points))
        msg += (name + ' Points: ' + str(points) + '\n')
    return msg

#Gives a sorted dictionary of peoples' names and their points descending
#returns a msg string
def get_leaderboard(profile_dict):
    rank_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    name_list = []
    point_list = []
    
    msg = 'EZ420 LEADERBOARD:\n\n'
    
    while len(point_list) < len(profile_dict):
        
        best_score = 0
        best_profile = 'e'
        
        for name, points in profile_dict.items():
            #print('Name: ' + name + ' Points: ' + str(points))
            if points > best_score and name not in name_list and 'e' != name:
                best_score = points
                best_profile = name
                
        name_list.append(best_profile)
        point_list.append(best_score)
    
    leaderboard_dict = {}
    
    i = 0
    
    while i < len(name_list):
        leaderboard_dict[name_list[i]] = point_list[i]
        j = i + 1
        msg += str(j) + '. ' + name_list[i] + ' ' + str(point_list[i]) + '\n'
        i+=1
    return msg
    
    
        
    