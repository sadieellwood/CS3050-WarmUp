# *-----* Imports *-----*
from tkinter import *
from tkinter import ttk
import customtkinter as cttk
import parser as psr

# *----* Main *----*
if __name__ == "__main__":

    # *-----* Basic Setup *-----*

    # init vars
    RESOLUTION = "700x600"

    # tkinter preference stuff
    cttk.set_appearance_mode("dark")
    cttk.set_default_color_theme("blue")

    # init base stuff, i.e the root and the main box
    root = cttk.CTk()
    root.title("Movie Search")
    root.geometry(RESOLUTION)

    # configure the grid
    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=0)

    # add frames for search, and display (and reference)
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
        #user_q(search_box.get())
        fill_results(['1', '2', '3', '4', '5', search_box.get()])
        
        
    def user_q(user_search_input):
        parse_results = psr.parse(user_serach_input)
        results = do_query(parse_results)
        fill_results(results)

    def fill_results(results):
        result_box.configure(state="normal")
        result_box.delete(1.0 ,END)
        for line in results:
            result_box.insert(END, line)
            result_box.insert(END, "\n")
        result_box.configure(state="disabled")
        
    def close_app():
        root.destroy()
        
    # *-----* import from parser *-----*
    def user_parsed(_):  # user query input goes here
        return psr.parse(self, _)

    # *-----*  widgets *-----*
    #*-----* top help window *-----*
#     def open_help_window():
#         help_window = Toplevel()
#         help_window.geometry(HELPRESOLUTION)
#         
#         help_window.label = cttk.CTkLabel(text = "Parser Information:")
#         help_information = ["help info starts here",
#                             "random information",
#                             "help info ends here"]
#         
#         
#         help_frame = cttk.CTkFrame(help_window)
#         help_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky=(N, S))
#         
#         help_box = cttk.CTkEntry(help_frame, width=300, height=30)
#         help_box.grid(row=1, column=0, padx=10, pady=(10, 0), sticky=(N,S))
#         
#         top_close_button = cttk.CTkButton(help_window,
#                 text = "close", command = help_window.destroy)
#         top_close_button.grid(row=2, column=0, padx=10, pady=(10, 0),
#                               sticky=(N,S))
#         i = 0
#         for text in help_information:
#             help_box.insert(i, text)
#             help_box.insert(i, "\n")
#             i += 1
#             
#         help_box.configure(state='disabled')
#         
#         help_box.mainloop()
    
    # add widgets to frames

    # search button
    search_button = cttk.CTkButton(
        search_frame, text="Search", command=search, width=200, height=30
    )
    search_button.grid(row=0, column=1, padx=5, pady=5, sticky=(E, W))

    # search entry box
    search_box = cttk.CTkEntry(search_frame, width=300, height=30)
    search_box.grid(row=0, column=0, padx=5, pady=5, sticky=(E, W))

    # results text box
    result_box = cttk.CTkTextbox(display_frame, width=500, height=300, corner_radius=0)
    result_box.configure(state="disabled")
    result_box.grid(row=0, column=0, sticky=(N, E, S, W))

    # close button
    close_button = cttk.CTkButton(option_frame, text="close", command=close_app)
    close_button.grid(row=0, column=1, padx=5, pady=5, sticky=(E, W))

    # *-----* Main Loop *-----*
    root.mainloop()
