from Tkinter import *
import winsound
from index_class import *
import webbrowser

class Application(Frame):
    """GUI App with buttone"""
    
    def __init__(self, master):

        Frame.__init__(self,master)
        self.grid()
        self.create_widgets()
        self.executioner=MainExecutioner()

    def create_widgets(self):
        """ create buttons """

        self.button1 = Button(self, height = 5, width = 50 , text = "Start")
       
        self.button1["command"] = self.start #binding even
        self.button1.grid()

        self.button2 = Button(self, height = 5, width = 50 , text = "Open Search")
       
        self.button2["command"] =self.open_window #binding even
        self.button2.grid()

    def make_sound(self):
        winsound.PlaySound("SystemHand", winsound.SND_ASYNC)

    def start(self):
        self.executioner.trainSurf()
        self.executioner.start_surveillance()

    def open_window(self):
        webbrowser.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open_new_tab('http://localhost/logger/index.php')
        
        
        
root = Tk()
root.title("Smart Surveillance")

root.geometry("400x400") #width x height

app = Application(root)

root.mainloop()
