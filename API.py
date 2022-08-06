from pytube import YouTube
import pytube 
import os

class API():
    def __init__(self):
        self.youtube_objects = []
    
    def get_video(self, url):
        try:
            video = YouTube(url)
        except pytube.exceptions.VideoUnavailable:
            return (1, url)
        except pytube.exceptions.RegexMatchError:
            return (1, url)
        return (0, video)
    
    def download(self, video, mode):
        print('downloading ' + mode)
        streams = video[1].streams
        if mode == 'video':
            print('vid')
        elif mode == 'audio':
            print('aud')


'''
[<Stream: itag="17" mime_type="video/3gpp" res="144p" fps="6fps" vcodec="mp4v.20.3" acodec="mp4a.40.2" progressive="True" type="video">, 
<Stream: itag="18" mime_type="video/mp4" res="360p" fps="25fps" vcodec="avc1.42001E" acodec="mp4a.40.2" progressive="True" type="video">,
<Stream: itag="22" mime_type="video/mp4" res="720p" fps="25fps" vcodec="avc1.64001F" acodec="mp4a.40.2" progressive="True" type="video">, 
<Stream: itag="299" mime_type="video/mp4" res="1080p" fps="50fps" vcodec="avc1.64002a" progressive="False" type="video">, 
<Stream: itag="303" mime_type="video/webm" res="1080p" fps="50fps" vcodec="vp9" progressive="False" type="video">, 
<Stream: itag="399" mime_type="video/mp4" res="1080p" fps="50fps" vcodec="av01.0.09M.08" progressive="False" type="video">, 
<Stream: itag="298" mime_type="video/mp4" res="720p" fps="50fps" vcodec="avc1.4d4020" progressive="False" type="video">, 
<Stream: itag="302" mime_type="video/webm" res="720p" fps="50fps" vcodec="vp9" progressive="False" type="video">, 
<Stream: itag="398" mime_type="video/mp4" res="720p" fps="50fps" vcodec="av01.0.08M.08" progressive="False" type="video">, 
<Stream: itag="135" mime_type="video/mp4" res="480p" fps="25fps" vcodec="avc1.4d401e" progressive="False" type="video">, 
<Stream: itag="244" mime_type="video/webm" res="480p" fps="25fps" vcodec="vp9" progressive="False" type="video">, 
<Stream: itag="397" mime_type="video/mp4" res="480p" fps="25fps" vcodec="av01.0.04M.08" progressive="False" type="video">, 
<Stream: itag="134" mime_type="video/mp4" res="360p" fps="25fps" vcodec="avc1.4d401e" progressive="False" type="video">, 
<Stream: itag="243" mime_type="video/webm" res="360p" fps="25fps" vcodec="vp9" progressive="False" type="video">, 
<Stream: itag="396" mime_type="video/mp4" res="360p" fps="25fps" vcodec="av01.0.01M.08" progressive="False" type="video">, 
<Stream: itag="133" mime_type="video/mp4" res="240p" fps="25fps" vcodec="avc1.4d4015" progressive="False" type="video">, 
<Stream: itag="242" mime_type="video/webm" res="240p" fps="25fps" vcodec="vp9" progressive="False" type="video">, 
<Stream: itag="395" mime_type="video/mp4" res="240p" fps="25fps" vcodec="av01.0.00M.08" progressive="False" type="video">, 
<Stream: itag="160" mime_type="video/mp4" res="144p" fps="25fps" vcodec="avc1.4d400c" progressive="False" type="video">, 
<Stream: itag="278" mime_type="video/webm" res="144p" fps="25fps" vcodec="vp9" progressive="False" type="video">, 
<Stream: itag="394" mime_type="video/mp4" res="144p" fps="25fps" vcodec="av01.0.00M.08" progressive="False" type="video">, 
<Stream: itag="139" mime_type="audio/mp4" abr="48kbps" acodec="mp4a.40.5" progressive="False" type="audio">, 
<Stream: itag="140" mime_type="audio/mp4" abr="128kbps" acodec="mp4a.40.2" progressive="False" type="audio">, 
<Stream: itag="249" mime_type="audio/webm" abr="50kbps" acodec="opus" progressive="False" type="audio">, 
<Stream: itag="250" mime_type="audio/webm" abr="70kbps" acodec="opus" progressive="False" type="audio">, 
<Stream: itag="251" mime_type="audio/webm" abr="160kbps" acodec="opus" progressive="False" type="audio">]'''

