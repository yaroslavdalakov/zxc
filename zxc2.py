names = ['Firewey', 'Dewedor', 'Silverde', 'StupidNames']
classes = ['amazon', 'necromancer', 'paladin', 'druid']
levels = [2, 2, 3, 4]

def get_stats(name, name_list, class_list, level_list):
    i = name_list.index(name)
    char_class = class_list[i]
    char_level = level_list[i]
    return char_class, char_level



player_3 = get_stats('Silverde', names, classes, levels)
print(player_3)

player_1={}

player_stats = {'Firewey': 'Amazon', 'Dewedor': 'necromancer'}
name = player_stats['Firewey'] = 'barbarian'

print(player_stats)

player_stats['Mark'] = 'Bard'
print(player_stats)

del player_stats['Firewey']
print(player_stats)

print(player_stats.keys())
print(player_stats.values())

for key in player_stats.keys():
    print(key)