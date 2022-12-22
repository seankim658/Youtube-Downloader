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
    
    def download(self, video, mode, download_path):
        print(f'\n---------- Downloading {mode.upper()} ----------')
        print(f'Download Path: {download_path}')
        streams = video[1].streams
        vid_streams = streams.filter(only_video = True)
        audio_streams = streams.filter(only_audio = True)
        if mode == 'video':
            print(f'--- VID: {vid_streams.first().title} ---')
            vid_streams = vid_streams.filter(progressive = False)
            print(vid_streams.first())
            try:
                vid_streams.first().download(output_path = download_path)
            except:
                print('Error downloading video')
            print('Download complete')
            print(f'Resolution: {vid_streams.first().resolution}')
            vfile_type = vid_streams.first().mime_type.split('/')[1]
            print(f'Type: {vfile_type}')
            print(f'Codec: {vid_streams.first().video_codec}')
            print(f'File Size (GBs): {vid_streams.first().filesize / 1_000_000_000}')

        # download audio regardless of mode 
        audio_streams = audio_streams.filter(file_extension = vfile_type)
        print(f'--- AUDIO: {audio_streams.first().title} ---')
        print(audio_streams.first())
        try:
            audio_streams.first().download(output_path = download_path, filename_prefix = 'Aud-')
        except:
            print('Error downloading audio')
        print('Audio download complete')
        print(f'ABR: {audio_streams.first().abr}')
        afile_type = audio_streams.first().mime_type.split('/')[1]
        print(f'Type: {afile_type}')
        print(f'Codec: {audio_streams.first().audio_codec}')
        print(f'File Size (GBs): {audio_streams.first().filesize / 1_000_000_000}')