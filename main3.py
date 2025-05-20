import tkinter as tk
from tkinter import colorchooser, filedialog
from PIL import Image, ImageGrab

class BlackboardApp:
    def __init__(self, window, window_title):
        self.window = window
        self.window.title(window_title)
        
        # Set up the canvas
        self.canvas = tk.Canvas(window, bg='white', width=800, height=600)
        self.canvas.pack()

        # Set up drawing variables
        self.last_x = None
        self.last_y = None
        self.pen_color = 'black'

        # Bind mouse events
        self.canvas.bind("<Button-1>", self.start_draw)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.reset)

        # Set up menu
        self.setup_menu()

    def setup_menu(self):
        menu = tk.Menu(self.window)
        self.window.config(menu=menu)

        file_menu = tk.Menu(menu)
        menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Save", command=self.save_canvas)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.window.quit)

    def start_draw(self, event):
        self.last_x = event.x
        self.last_y = event.y

    def draw(self, event):
        if self.last_x is not None and self.last_y is not None:
            self.canvas.create_line(self.last_x, self.last_y, event.x, event.y, fill=self.pen_color, width=2)
            self.last_x = event.x
            self.last_y = event.y

    def reset(self, event):
        self.last_x = None
        self.last_y = None

    def save_canvas(self):
        # Open a file dialog to ask for the save location and filename
        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG files", "*.png"), ("All files", "*.*")]
        )
        if file_path:  # Check if the user selected a file path
            # Get the coordinates of the canvas to capture
            x = self.window.winfo_rootx() + self.canvas.winfo_x()
            y = self.window.winfo_rooty() + self.canvas.winfo_y()
            x1 = x + self.canvas.winfo_width()
            y1 = y + self.canvas.winfo_height()
            
            # Use ImageGrab to capture the canvas area
            ImageGrab.grab().crop((x, y, x1, y1)).save(file_path)

if __name__ == "__main__":
    window = tk.Tk()
    app = BlackboardApp(window, "Blackboard App")
    window.mainloop()