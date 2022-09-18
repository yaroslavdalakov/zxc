with open('lyrics.txt', encoding="utf8") as f:
    lyrics = f.read()

print(lyrics)
print(type(lyrics))

for w in lyrics:
    print(w)

lyrics_list = []
banned = [' ','.',',','!']
lyrics_word = ''

for w in lyrics:
    w = w.lower()
    if w == '\n':
        if lyrics_word:
            lyrics_list.append(lyrics_word)
            lyrics_word = ''
    elif w not in banned:
        lyrics_word += w
    else:
        if lyrics_word:
            lyrics_list.append(lyrics_word)
        lyrics_word = ''

if lyrics_word:
    lyrics_list.append(lyrics_word)
    lyrics_word = ''
 
print(lyrics_list)