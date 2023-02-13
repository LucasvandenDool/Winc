# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
ruud = 'Ruud Gullit'
bast = 'Marco van Basten'
goal_0 = 32
goal_1 = 54

scorers = 'Ruud Gullit' + ' ' + str(goal_0) + ', Marco van Basten' + ' ' + str(goal_1)
print(scorers)

report = f"{ruud} scored in the {str(goal_0)}nd minute\n{bast} scored in the {str(goal_1)}th minute"
print(report)

player = 'Ruud Gullit'
first_name = player[:player.find(' ')]
last_name = (player[player.find(' '):]) [1:]
last_name_len = len(last_name)
name_short = f"{first_name[0]}. {last_name}"


first_name_len = len(first_name)
chant = (f"{first_name}! " * first_name_len) [:-1]
print(chant)

good_chant = chant[-1] != ' '
print(good_chant)








