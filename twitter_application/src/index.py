
from tkinter import Tk
from ui.ui import UI
from initialize_db import initialize_database

def main():
    """Main function which initialized tkinter and database.
    """    
    initialize_database()
    window = Tk()
    window.attributes('-fullscreen', True)
    window.geometry("900x700")
    window.title("Twitter app")
    ui_view = UI(window)
    ui_view.start()
    window.mainloop()

if __name__ == "__main__":
    main()
