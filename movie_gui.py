# *-----* Imports *-----*
from tkinter import *
from tkinter import ttk
import customtkinter as cttk

from parser import Parser
from movie import Movie, do_query

# *----* Main *----*
if __name__ == "__main__":

    # *-----* Basic Setup *-----*

    # init vars
    RESOLUTION = "700x600"
    HELPRESOLUTION = "500x500"

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

    # *-----* Methods *-----*
    # search method
    def search():
        search_input = search_box.get()

        #if user search is empty, keep previously display results out
        if search_input == "":
            pass
            
        #otherwise pass user search to the query function
        else:
            user_q(search_input)

    #check if parse is valid, then pass to query
    #check if query is valid then pass to be inserted if so
    def user_q(user_search_input):

        # returns a tuple containing (True or False, results)
        parse_results = user_parsed(user_search_input)

        #if true then parser had no errors
        if parse_results[0]:

            print_results = []

            #send parse results to query
            query_results = do_query(parse_results[1])

            #if query returns no error put results in a list
            #and send to fillout the textbox
            if query_results[0]:
                for value in query_results[1]:
                    print_results.append(str(value))
            #otherwise print error
            else:
                print_results = [query_results[1]]

        #otherwise parse was invalid, print error message to textbox
        else:
            print_results = [parse_results[1]]

        #send result, (good or bad to be filled out)
        fill_results(print_results)

    #fill textbox with given list of results
    def fill_results(results):

        #reopen the text box to be editable
        #and clear
        result_box.configure(state="normal")
        result_box.delete(1.0, END)

        #insert all results and format
        for line in results:
            result_box.insert(END, line)
            result_box.insert(END, "\n---------------- \n")

        #disable box to no longer be edit-able
        result_box.configure(state="disabled")

    #close app
    def close_app():
        root.destroy()

    #parse the user
    def user_parsed(user_search_input):
        psr = Parser()
        return psr.parse(user_search_input)

    # *-----*  widgets *-----*
    # *-----* top help window *-----*
    def open_help_window():
        help_window = Toplevel()
        help_window.geometry(HELPRESOLUTION)

        help_information2 = [
            "SEARCH KEYWORDS",
            "",
            "Date",
            "\t must be formatted YYYY-MM-DD",
            "\t can be used with ==, >=, <=, >, and <",
            "\t example query: Date > 2010-01-01",
            "-----------",
            "Title",
            "\t can only be used with ==",
            "\t example query: title == Toy Story",
            "-----------",
            "Rating",
            "\t must be a number between 0 and 10",
            "\t can be used with ==, >=, <=, >, and <",
            "\t example query: rating <= 6.0",
            "-----------",
            "Series:",
            "\tcan only be used with ==",
            "\tto search for movies not a part of a series,",
            "\tuse 'None'",
            "\texample query: series == The Toy Story Collection",
            "",
            "Search keywords are not case sensitive,",
            "but title and series names are!",
            "",
            "LOGICAL OPERATORS:",
            "You can specify up to 2 conditions in your query using",
            "'AND' and 'OR'",
            "\t example queries:",
            "\t\tseries == None OR rating == 0.0",
            "\t\trating > 3 AND rating < 7",
            "",
            "-----------",
            "MORE EXAMPLES:",
            "series == 'Divergent Collection'",  # handles quoted + unquoted strings
            "Date > 2010-01-01",
            "TITLE == The Hills Have Eyes",
            "rating <= 6.0",
            "rating > 3 AND rating < 7",  # conjoined statement ex.
            "series == None OR rating == 0.0",  # NULL series ex. (optional field)
        ]


        #innit frames for putting widgets in
        help_frame = cttk.CTkFrame(help_window)
        help_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky=(N, S))

        #innit widgets and put them in frame
        help_box = cttk.CTkTextbox(help_frame, width=425, height=300)
        help_box.grid(row=1, column=0, padx=10, pady=(10, 0), sticky=(N, S))

        top_close_button = cttk.CTkButton(help_window, text="close", command=help_window.destroy)
        top_close_button.grid(row=2, column=0, padx=10, pady=(10, 0), sticky=(N, S))

        for text in help_information2:
            help_box.insert(END, text)
            help_box.insert(END, "\n")

        help_box.configure(state="disabled")

        help_box.mainloop()

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

    # help button
    help_button = cttk.CTkButton(option_frame, text="help", command=open_help_window)
    help_button.grid(row=0, column=0, padx=5, pady=5, sticky=(E, W))

    # *-----* Main Loop *-----*
    root.mainloop()
