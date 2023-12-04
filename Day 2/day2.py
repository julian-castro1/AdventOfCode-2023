import re

file_name = "input.txt"

# read each line
# only 12 red cubes, 13 green cubes, and 14 blue cubes

max_vals = {'red':12,'green':13,'blue':14}
games_sum = 0

# Game 93: 4 blue, 1 green, 4 red; 8 red, 4 green, 4 blue; 2 blue, 9 red; 1 blue, 4 red; 4 blue, 2 green, 11 red
with open(file_name, 'r') as file:
    for game in file:
        
        game_str = game.split(':')
        rounds = game_str[1].split(';')
        
        game_ID = int(re.findall(r'\d+', game_str[0])[0])
        cur_max = {}
        
        for round_str in rounds:
            for draw in round_str.split(','):
                cube = draw.strip().split(' ')
                cube_cnt = int(cube[0])
                cube_col = cube[1]
                
                cur_max[cube_col] = max(cur_max.get(cube_col, 0), cube_cnt)
        
        cur_power = 1
        for col, cnt in cur_max.items():
            cur_power = cur_power * cnt
        games_sum = games_sum + cur_power
    
    print(games_sum)
        