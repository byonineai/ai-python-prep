# 8-8. User Albums

def make_album(artist, title, tracks=None):
    album = {"artist": artist.title(), "title": title.title()}
    if tracks is not None:
        album["tracks"] = tracks
    return album


while True:
    print("\nEnter album information (type 'q' to quit).")

    artist = input("Artist: ")
    if artist.lower() == "q":
        break

    title = input("Album title: ")
    if title.lower() == "q":
        break

    album = make_album(artist, title)
    print(album)