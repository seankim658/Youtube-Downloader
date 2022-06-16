import tkinter as tk
from tkinter import ttk
from matplotlib import widgets
from API import API

class App(tk.Frame):
    def __init__(self):
        super(App, self).__init__()
        self.widgets = []
        self.result_widgets = []
        self.grid()
        self.create_widgets()
        self.first_run = True 
        self.api = API()
    
    def create_widgets(self):
        url = tk.Entry(self, font = ('Courier New', 12), width = 50)
        url.grid()
        self.widgets.append(url)
        self.download_video_button = tk.Button(self, text = 'Download Video', command = lambda : self.download('video'))
        self.download_video_button.grid(row = 0, column = 1)
        self.download_audio_button = tk.Button(self, text = 'Download Audio', command = lambda : self.download('audio'))
        self.download_audio_button.grid(row = 0, column = 2)
        self.clone_button = tk.Button(self, text='Add Download', command = lambda : self.clone())
        self.clone_button.grid(row = 0, column = 3)
    
    def clone(self):
        if self.first_run == True:
            self.remove_button = tk.Button(self, text = 'Remove Download', command = lambda : self.remove())
            self.remove_button.grid(row = 0, column = 4)
            self.first_run = False
        widget = tk.Entry(self, font = ('Courier New', 12), width = 50)
        widget.grid()
        self.widgets.append(widget)
    
    def remove(self):
        if len(self.widgets) == 1:
            self.remove_button.destroy()
            self.first_run = True
        if len(self.widgets) >= 1:
            widget = self.widgets.pop(len(self.widgets) - 1)
            widget.destroy()

    def download(self, mode):
        videos = []
        for widget in self.widgets:
            url = widget.get()
            print(url)
            current_vid = self.api.get_video(url)
            self.show_results(current_vid)
        self.clear_text()
    
    def show_results(self, current_vid):
        if current_vid[0] == 0:
            result = tk.Label(self, text = f'Found video {current_vid.title}')
            result.grid()
            self.result_widgets.append(result)
        else:
            result = tk.Label(self, text = f'Could not find video {current_vid[1]}')
            result.grid()
            self.result_widgets.append(result) 

    def clear_text(self):
        for widget in self.widgets:
            widget.delete(0, 'end')
        


