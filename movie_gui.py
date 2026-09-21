#*-----* Imports *-----*
from tkinter import *
from tkinter import ttk
import customtkinter as cttk
import parser as psr



#*----* Main *----*
if __name__ == '__main__':


    #*-----* Basic Setup *-----*
    
    #init vars
    RESOLUTION = "700x600"
    
    #tkinter preference stuff
    cttk.set_appearance_mode("dark")  
    cttk.set_default_color_theme("blue")
    
    
    #init base stuff, i.e the root and the main box
    root = cttk.CTk()
    root.title("Movie Search")
    root.geometry(RESOLUTION)
    
    #configure the grid
    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=0)
    
    #add frames for search, and display (and reference)
    search_frame = cttk.CTkFrame(root)
    search_frame.grid(row=0, column=0, padx=10, pady=2, sticky=(N, S))
    
    display_frame = cttk.CTkFrame(root)
    display_frame.grid(row=1, column=0, padx=10, pady=(10, 0), sticky=(N, S))
    
    option_frame = cttk.CTkFrame(root)
    option_frame.grid(row=2, column=0, padx=10, pady=(10, 0), sticky=(N, S))
    
    #*-----* Methods *-----*
    #search method
    def search():
        print(search_box.get())
        result_box.configure(state="normal")
        result_box.insert(END, search_box.get())
        result_box.insert(END, "\n")
        result_box.configure(state="disabled")
        
    def close_app():
        root.destroy()
        
    #*-----*  widgets *-----*

        
    
    #add widgets to frames
        
    #search button
    search_button = cttk.CTkButton(search_frame, text="Search", command=search,
                                   width=200, height=30)
    search_button.grid(row=0,column=1,padx=5,pady=5, sticky=(E, W))

    #search entry box
    search_box = cttk.CTkEntry(search_frame,
                               width=300, height=30)
    search_box.grid(row=0, column=0, padx=5, pady=5, sticky=(E, W))

    #results text box
    result_box= cttk.CTkTextbox(display_frame, width=500, height=300,
                                corner_radius=0)
    result_box.configure(state="disabled")
    result_box.grid(row=0, column=0, sticky=(N,E,S,W))

    #close button
    close_button = cttk.CTkButton(option_frame, text="close",command=close_app)
    close_button.grid(row=0, column=1, padx=5, pady=5, sticky=(E, W))
    
    #*-----* import from parser *-----*
    def user_parsed(_): # user query input goes here
        return psr.parse(self, _)
    
    #*-----* Main Loop *-----*
    root.mainloop()