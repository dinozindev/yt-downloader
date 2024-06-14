import re
from pytube import YouTube
from pytube import Playlist

def baixar_audio(url):
    yt = YouTube(url)
    streamAudio = yt.streams.get_by_itag(140)
    streamAudio.download()
    print("Download realizado com sucesso!")

def baixar_video(url):
    yt = YouTube(url)
    streamVideo = yt.streams.get_by_itag(22)
    streamVideo.download()
    print("Download realizado com sucesso!")

def baixar_playlist_musicas(url):
    p = Playlist(url)
    print(p)
    for musica in p:
        musicaYT = YouTube(musica)
        musicaYT.streams.get_by_itag(140).download()




url = input("Qual o URL do vídeo que deseja baixar?: ")
while True:
    print("Opção de download: ")
    print("1 - Áudio")
    print("2 - Vídeo")
    print("3 - Playlist de Músicas")
    opt = input("Qual opção deseja baixar?: ")
    if not opt.isdigit() or int(opt) > 3 or int(opt) < 1:
        print("Insira uma opção válida.")
        continue
    opt = int(opt)
    match opt:
        case 1:  
            baixar_audio(url)
            break
        case 2:
            baixar_video(url)
            break
        case 3: 
            baixar_playlist_musicas(url)
            break


