import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from matplotlib import widgets
from API import API

class App(tk.Frame):
    def __init__(self):
        ''' App constructor 
        '''
        super(App, self).__init__()
        self.main_widgets = []
        self.result_widgets = []
        self.widget_row = 1
        self.grid()
        self.create_widgets()
        self.first_run = True 
        self.api = API()
        # default download location is main drive root folder 
        self.download_destination_string = 'C:\\'
    
    def create_widgets(self):
        ''' Creates the home screen widgets 
        '''
        # first url entry bar 
        url = tk.Entry(self, font = ('Courier New', 12), width = 50)
        url.grid()
        self.main_widgets.append(url)
        # download video button 
        self.download_video_button = tk.Button(self, text = 'Download Video', command = lambda : self.download('video'))
        self.download_video_button.grid(row = 0, column = 1)
        # download audio button 
        self.download_audio_button = tk.Button(self, text = 'Download Audio', command = lambda : self.download('audio'))
        self.download_audio_button.grid(row = 0, column = 2)
        # set download destination 
        self.download_destination_button = tk.Button(self, text = 'Download Destination', command = lambda : self.download_destination())
        self.download_destination_button.grid(row = 0, column = 3)
        # clear results button 
        self.clear_results_button = tk.Button(self, text = 'Clear', command = lambda : self.clear_results())
        self.clear_results_button.grid(row = 0, column = 4)
        # add download button 
        self.clone_button = tk.Button(self, text = 'Add Download', command = lambda : self.clone())
        self.clone_button.grid(row = 0, column = 5)
    
    def download_destination(self):
        ''' Set the download destination 
        '''
        self.download_destination_string = filedialog.askdirectory()
        print(self.download_destination_string)
    
    def clone(self):
        ''' Add new download entry 
        '''
        if self.first_run == True:
            # if adding a second entry bar create a remove button 
            self.remove_button = tk.Button(self, text = 'Remove Download', command = lambda : self.remove_entry())
            self.remove_button.grid(row = 0, column = 6)
            self.first_run = False
        # create the new entry bar 
        widget = tk.Entry(self, font = ('Courier New', 12), width = 50)
        widget.grid(row = self.widget_row, column = 0)
        self.widget_row += 1
        self.main_widgets.append(widget)
    
    def remove_entry(self):
        ''' Remove excess download entries 
        '''
        if len(self.main_widgets) == 2:
            self.remove_button.destroy()
            self.first_run = True
        if len(self.main_widgets) >= 1:
            widget = self.main_widgets.pop(len(self.main_widgets) - 1)
            widget.destroy()
            self.widget_row -= 1

    def download(self, mode):
        videos = []
        for widget in self.main_widgets:
            url = widget.get()
            current_vid = self.api.get_video(url)
            self.show_results(current_vid)
            self.api.download(current_vid, mode, self.download_destination_string)
        self.clear_text()
    
    def show_results(self, current_vid):
        if current_vid[0] == 0:
            result = tk.Label(self, text = f'Found video: {current_vid[1].title}')
            result.grid(row = self.widget_row, column = 0)
            self.widget_row += 1
            self.result_widgets.append(result)
        else:
            result = tk.Label(self, text = f'Could not find video: {current_vid[1]}')
            result.grid(row = self.widget_row, column = 0)
            self.widget_row += 1
            self.result_widgets.append(result) 

    def clear_results(self):
        ''' Clear the result labels and progress bars 
        '''
        for widget in self.result_widgets:
            widget.destroy()
        self.result_widgets = []

    def clear_text(self):
        ''' Clear the entry bars 
        '''
        for widget in self.main_widgets:
            widget.delete(0, 'end')
        


