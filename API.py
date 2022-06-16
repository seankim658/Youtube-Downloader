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
        return (0, video)