import client

id_user = '1234'
id_playlist = '111'

deezer = Deezer()
user = deezer.user(id=id)
albums = user.albums

playlist = user.create_playlist()

for album in albums:
    for track in album.tracks:
        playlist.add_track(track)

