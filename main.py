from pytube import YouTube
from sys import argv


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# link = argv[1]
def youtube():
    YouTube('https://youtu.be/9bZkp7q19f0').streams.first().download()
    yt = YouTube('http://youtube.com/watch?v=9bZkp7q19f0')

    yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
    print("Title: ", yt.title)

    print("View: ", yt.views)

    yd = yt.streams.get_highest_resolution()

    # ADD FOLDER HERE
    yd.download(".\\D:\\Disco D\\Scripts\\Python\\test")


def Download():
    link = "https://youtube.com/watch?v=9bZkp7q19f0"
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("Ocurrio un error")
    print("Descarga completada satisfactoriamente")







if __name__ == '__main__':
    print_hi('PyCharm')

    Download()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
