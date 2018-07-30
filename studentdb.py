from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.listview import ListItemButton
import glob, os
import subprocess
 
 
class StudentListButton(ListItemButton):
    pass
 
 
class StudentDB(BoxLayout):
 
    # Connects the value in the TextInput widget to these
    # fields
    student_list = ObjectProperty()
    prog_list = {}

    def loadProgs(self):
        for file in os.listdir("D:\Games\Celeste.v1.2.3.2"):
            if file.endswith(".exe"):
                # Get the student name from the TextInputs
                student_name = file
                self.prog_list[student_name] = os.path.join("D:\Games\Celeste.v1.2.3.2", file)
                # Add the student to the ListView
                self.student_list.adapter.data.extend([student_name])
        
                # Reset the ListView
                self.student_list._trigger_reset_populate()
    def launchProgs(self):
        # If a list item is selected
        if self.student_list.adapter.selection:
 
            # Get the text from the item selected
            selection = self.student_list.adapter.selection[0].text
            subprocess.call([self.prog_list[selection]])
 
class StudentDBApp(App):
    def build(self):
        return StudentDB()
 
 
dbApp = StudentDBApp()
 
dbApp.run()