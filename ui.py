from tkinter.filedialog import askopenfilename
from tkinter import *
from tkinter import messagebox
from detection2 import process_Video

# Window Characteristics
top = Tk()
top.title("Canny Edge Detection")
top.geometry("300x300")

def import_video():
    global input_path
    input_path = askopenfilename()
    process_Video(input_path)
    print (input_path)

def export_video():
    global output_path
    output_path = filedialog.askdirectory()
    print (output_path)

import_button = Button(top, text = "Import Video", command = import_video)
import_button.place(x = 10,y = 10)
export_button = Button(top, text = "Export Directory", command = export_video)
export_button.place(x = 500,y = 10)

top.mainloop()