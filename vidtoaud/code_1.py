import moviepy.editor
s = input('Enter the video name:')
video = moviepy.editor.VideoFileClip(s)
audio = video.audio
a = input('Enter the audio file name :')
audio.write_audiofile(a)
