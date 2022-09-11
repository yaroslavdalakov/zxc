import pickle

game_data = [
    ('Name','Mike'),
    ('Class',"Barbarian"),
    ('Items', ['club','shield']),
    ('xp', 9000)
]

with open('save.dat','wb') as sf:
    pickle.dump(game_data, sf)

with open('save.dat','rb') as lf:
    load_data = pickle.load(lf)

    print(load_data)