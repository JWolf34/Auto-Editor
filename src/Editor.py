from moviepy.editor import *
from tkinter import filedialog
from tkinter import *
from tkinter.ttk import *
from mutagen.mp3 import MP3
import os
import random

#Global Variables
OFFSET = 10
MIN_SECONDS = 100
MAX_SECONDS = 1280 - OFFSET





def edit(videos, audio):

    clipList = []
    runtime = 0
    maxtime = MP3(audio).info.length
    while(runtime < maxtime):
        start = random.randint(MIN_SECONDS, MAX_SECONDS)
        end = start + random.randint(2, 6)
        clip = VideoFileClip(videos[random.randint(0, len(videos)-1)]).subclip(start, end)
        clipList.append(clip)
        runtime += end - start
        currtime = str(runtime//60) + ":" + str(runtime % 60)
        app.updateOutput("Editing..." + currtime)
        print("Editing..." + currtime)

    
    finalClip = concatenate_videoclips(clipList)
    #finalClip.set_audio(audio)
    
    finalClip.write_videofile("AMV.mp4", codec='mpeg4', audio=AudioFileClip(audio))


class MainApp:

    def __init__(self):

        #Variables
        self.fileList = []
        self.selectedFiles = []
        self.audioDirectory = ''
        self.fileDirectory = ''

    def createMenu(self):
        self.window = Tk()
        self.window.title("Auto-Editor Wizard")
        self.window.geometry('800x600')
        self.audioButton = Button(self.window, text='Select music', command=self.getAudioDir)
        self.audioButton.pack(pady=5)
        self.audioLabel = Label(self.window, text=self.audioDirectory, font=("Arial", 10))
        self.audioLabel.pack(padx=3)
        self.dirButton = Button(self.window, text='Select video folder', command=self.getFileDir)
        self.dirButton.pack(pady=5)
        self.dirLabel = Label(self.window, text=self.fileDirectory, font=("Arial", 10))
        self.dirLabel.pack(padx=3)
        self.selectAllButton = Button(self.window, text='Select all', command=self.selectAllFiles)
        self.selectAllButton.pack(pady=5)
        self.fileSelect =  Listbox(self.window, selectmode='extended', height=15)
        self.fileSelect.pack(fill=X, padx=20)
        
        self.editButton = Button(self.window, text='Edit', command=self.editClicked)
        self.editButton.pack(fill=X, pady=10, padx=50, ipady=12)

        self.outputLabel = Label(self.window, text='')
        self.outputLabel.pack(pady=15)
    
        self.window.mainloop()

    def editClicked(self):
        if(not self.audioDirectory):
            self.popupmsg('No audio was selected! Please select a file to continue.')
        elif(not self.fileDirectory):
            self.popupmsg('No video folder was selected! Please select a folder to continue.')
        elif(not self.fileSelect.curselection()):
            self.popupmsg('No files were selected! Please select at least one file to continue.')
        for index in (self.fileSelect.curselection()):
            self.selectedFiles.append(self.fileSelect.get(index))
        edit(self.selectedFiles, self.audioDirectory)

    def getFileDir(self):
        self.fileDirectory = filedialog.askdirectory()
        self.updateLabel(self.dirLabel, self.fileDirectory) 
        self.updateFileList(self.fileDirectory)
    
    def getAudioDir(self):
        self.audioDirectory = filedialog.askopenfilename()
        self.updateLabel(self.audioLabel, self.audioDirectory)

    def updateLabel(self, label, content):
        label.configure(text=content)
    
    def updateOutput(self, content):
        self.outputLabel.configure(text=content)

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

    def popupmsg(self, msg):
        popup = Tk()
        popup.title("!")
        label = Label(popup, text=msg)
        label.pack(side="top", fill="x", pady=10)
        B1 = Button(popup, text="Okay", command = popup.destroy)
        B1.pack()
        popup.mainloop()

    def write(self, string):
        self.updateOutput(string)
    





    



    
    

#global app
app = MainApp()
#sys.stdout=app.write()

if __name__ == "__main__":
    app.createMenu()




