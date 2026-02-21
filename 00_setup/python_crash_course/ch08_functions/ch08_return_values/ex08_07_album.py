def make_album(artist,album,tracks=''):
  musician_info = {'artist':artist,'album':album, 'tracks':tracks}
  return musician_info

star = make_album("Jorge","Seu")

star = make_album("Jorge","Seu",3)
print(star)