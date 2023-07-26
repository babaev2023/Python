from pytube import YouTube
import ffmpeg



URL = 'https://www.youtube.com/watch?v=Iv5-5R5jxCw'
DOWNLOAD_DIR = 'Downloads'

def download_video(url):
    yt = YouTube(url)
    #for stream in yt.streams:
       # print(stream)
    #yt.streams.get_highest_resolution().download(DOWNLOAD_DIR) # Можно по простому

    # Если хочешь максимальное качество
    video = yt.streams.filter(file_extension='mp4').order_by('resolution').desc().first()
    video.download(DOWNLOAD_DIR, 'video.mp4')
    if not video.is_progressive:
        stream_audio =  yt.streams.get_audio_only()
        stream_audio.download(DOWNLOAD_DIR, 'audio.mp4')
        combine(DOWNLOAD_DIR + '/video.mp4', DOWNLOAD_DIR + '/audio.mp4')


def combine (video, audio):
    audio_stream = ffmpeg.input(audio)
    video_stream = ffmpeg.input(video)
    ffmpeg.output(video_stream,audio_stream, DOWNLOAD_DIR + '/result.mp4').run()





if __name__ == '__main__':
    download_video(URL)

