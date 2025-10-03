def art_find(i):
    song_artist=["ra ra rakamma-aswin","naa ready-lognath","oo antava-anachi","jingucha-praveen"]
    for song in song_artist:
        if i.lower() in song:
            artist=song.replace(i.lower(),"").replace("-","").strip()
            return artist
res=art_find("OO ANTAVA")
print(res)