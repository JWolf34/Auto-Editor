from moviepy.editor import *
from tkinter import filedialog
from tkinter import *
from tkinter.ttk import *
import os
import random

#Global Variables
#audio = AudioFileClip("../resources/Audio/In the End.mp3")

OFFSET = 10
MIN_SECONDS = 100
MAX_SECONDS = 1280 - OFFSET
directory = ''



def edit(files):
    clipList = []
    
    for i in range(0, 10):
        start = random.randint(MIN_SECONDS, MAX_SECONDS)
        end = start + random.randint(2, 6)
        clip = VideoFileClip(files[random.randint(0, len(files)-1)]).subclip(start, end)
        clip = clip.volumex(0.0)
        clipList.append(clip)
        print("Clips appended: " + str(i + 1))

    
    finalClip = concatenate_videoclips(clipList)
    #finalClip.set_audio(audio)
    finalClip = finalClip.volumex(1.0)

    finalClip.write_videofile("AMV.mp4")


class MainApp:

    def __init__(self):

        #Variables
        self.fileList = []
        self.selectedFiles = []

        # Create UI Window
        self.window = Tk()
        self.window.title("AMV Editor Wizard")
        self.window.geometry('800x500')
        self.dirButton = Button(self.window, text='Select directory', command=self.getDir)
        self.dirButton.grid(column=0, row=0)
        self.dirLabel = Label(self.window, text=directory, font=("Arial", 10))
        self.dirLabel.grid(column=1, row=0)
        self.fileSelect =  Listbox(self.window, selectmode='extended', width=50)
        self.fileSelect.grid(column=0, row=1)
        self.selectAllButton = Button(self.window, text='Select all', command=self.selectAllFiles)
        self.selectAllButton.grid(column=1, row=1)
        self.editButton = Button(self.window, text='Edit', command=self.editClicked)
        self.editButton.grid(column = 0, row = 8)
    
        self.window.mainloop()

    def editClicked(self):
        for index in (self.fileSelect.curselection()):
            self.selectedFiles.append(self.fileSelect.get(index))
        edit(self.selectedFiles)

    def getDir(self):
        global directory
        directory = filedialog.askdirectory()
        self.updateLabel(self.dirLabel, directory) 
        self.updateFileList(directory)
    

    def updateLabel(self, label, content):
        label.configure(text=content)

    def updateFileList(self, fileDir):
        self.fileSelect.delete(0, END)
        self.fileList = []
        for file in os.listdir(fileDir):
            path = os.path.join(fileDir, file)
            if os.path.isdir(path):
                continue
            else:
                self.fileList.append(fileDir + "/" + file)
        for i in range(len(self.fileList)):
            self.fileSelect.insert(i, self.fileList[i])

    def selectAllFiles(self):
        self.fileSelect.selection_set(0, END)
    





    


    
    



if __name__ == "__main__":
    app = MainApp()

    #edit()




