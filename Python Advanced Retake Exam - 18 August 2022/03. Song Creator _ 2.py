def add_songs(*args):
    songs = {}
    for song, lyrics in args:
        if song not in songs:
            songs[song] = []
        if lyrics:
            for line in lyrics:
                songs[song].append(line)

    result = ""

    for song, lyrics in songs.items():
        result += f'- {song}\n'
        for lyric in lyrics:
            result += lyric + '\n'

    return result

print(add_songs(
    ("Bohemian Rhapsody", []),
    ("Just in Time",
     ["Just in time, I found you just in time",
      "Before you came, my time was running low",
      "I was lost, the losing dice were tossed",
      "My bridges all were crossed, nowhere to go"])
))