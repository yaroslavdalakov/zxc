def game():
    progress = True
    word = ['orange']
    lifes=3
    
    word_in_play = get_word(word)
    template = start_template(word_in_play)
    welcome_speech(list_to_string_convert(template))

    
    while progress:
        user_guess = user_input()

        
def build_template(template , word, guess=''):
    for i in range(len(word)):
        if template[i] == '_':
            if word[i] == guess:
                template[i] = word[i]
            else:
                template[i] = '_'
    return template



def welcome_speech(template):
    print(f" Добро пожаловать в игру Hangman 2000.ваша задача угадать загаданное слово за несколько попыток,иначе вас ждет расплата. Загаданное слово состоит из {len(template)} букв {template}")
         
    
          
def start_template(word):
    return list(word)

    
def list_to_string_convert(template):
    s = ''
    return s.join(template)
def get_word(word):
    return word[0]
def start_template(word):
    template = []
    for i in word:
        template.append('_')
    return template
    
        
def user_input():
    return input('введите свое предположение: ')

print(game())

