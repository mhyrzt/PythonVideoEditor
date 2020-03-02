from moviepy.editor import *

def GetSecond(MessageString):
    Array   = list(map(lambda x: int(x), input(MessageString).split()))
    Time    = 0
    for index in range(0, len(Array)):
        Time += Array[index] * (60 ** (len(Array) - 1 - index)) 
    return Time

VideoFile   = input('Enter Video Address: ')
StartTime   = GetSecond('Enter Start Time: ')
StopTime    = GetSecond('Enter Stop Time: ')
video       = VideoFileClip(VideoFile).subclip(StartTime, StopTime)
video.write_videofile("export.mp4")