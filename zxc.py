
def game():
    progress = True
    word = ['orange']
    lifes=3

    word_in_play = get_word(word)
    template = start_template(word_in_play)
    welcome_speech(list_to_string_convert(template))
def welcome_speech(t):
    pass
def start_template(w):
    return list(w)

    
def list_to_string_convert(t):
    pass
def get_word(w):
    return w[0]

print(game())
print(start_template())

