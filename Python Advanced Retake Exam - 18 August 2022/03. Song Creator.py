
def add_songs(*args):
    songs_dict = {}
    for song, text in args:
        if song not in songs_dict:
            songs_dict[song] = []
        songs_dict[song]+=text

    result = ""
    for k,v in songs_dict.items():
        result += f'- {k}\n' + "\n".join(v)
        if v:
            result += "\n"

    return result
print(add_songs(
    ("Bohemian Rhapsody", []),
    ("Just in Time",
     ["Just in time, I found you just in time",
      "Before you came, my time was running low",
      "I was lost, the losing dice were tossed",
      "My bridges all were crossed, nowhere to go"])
))
