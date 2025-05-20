import tkinter as tk
from tkinter import colorchooser, filedialog
from PIL import ImageGrab

class BlackboardApp:
    def __init__(self, window, window_title):
        self.window = window
        self.window.title(window_title)

        self.screen_width = self.window.winfo_screenwidth()
        self.screen_height = self.window.winfo_screenheight()
        self.window.geometry(f"{self.screen_width}x{self.screen_height}")

        self.current_color = "white"
        self.line_width = 2
        self.current_tool = "pen"
        self.current_shape = "line"

        self.canvas = tk.Canvas(window, width=self.screen_width, height=self.screen_height, bg='black')
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.setup_menu()
        self.setup_tools()

        self.last_x = None
        self.last_y = None

        self.canvas.bind("<Button-1>", self.start_draw)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.stop_draw)

    def setup_menu(self):
        menubar = tk.Menu(self.window)
        self.window.config(menu=menubar)

        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Save", command=self.save_canvas)
        file_menu.add_command(label="Clear", command=self.clear_canvas)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.window.quit)

        edit_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Choose Color", command=self.choose_color)

    def setup_tools(self):
        tools_frame = tk.Frame(self.window)
        tools_frame.pack(side=tk.LEFT, fill=tk.Y)

        tools = [
            ("Pen", "pen"),
            ("Pencil", "pencil"),
            ("Eraser", "eraser"),
            ("Line", "line"),
            ("Rectangle", "rectangle"),
            ("Oval", "oval"),
            ("Circle", "circle"),
            ("Square", "square")
        ]

        for text, tool in tools:
            btn = tk.Button(tools_frame, text=text, command=lambda t=tool: self.set_tool(t))
            btn.pack(side=tk.TOP, padx=2, pady=2)

    def set_tool(self, tool):
        self.current_tool = tool
        if tool == "eraser":
            self.line_width = 20
            self.current_color = self.canvas['bg']
            self.canvas.config(cursor="circle")
        elif tool in ["pen", "pencil"]:
            self.line_width = 2 if tool == "pen" else 1
            self.current_color = "white"  # Default color for pen/pencil
            self.canvas.config(cursor="pencil")
        else:  # For shapes
            self.line_width = 2
            self.canvas.config(cursor="crosshair")

    def start_draw(self, event):
        self.last_x = event.x
        self.last_y = event.y

    def draw(self, event):
        if self.last_x is not None and self.last_y is not None:
            if self.current_tool in ["pen", "pencil"]:
                self.canvas.create_line(
                    self.last_x, self.last_y, event.x, event.y,
                    fill=self.current_color,
                    width=self.line_width,
                    capstyle=tk.ROUND,
                    smooth=True
                )
            elif self.current_tool == "eraser":
                self.canvas.create_line(
                    self.last_x, self.last_y, event.x, event.y,
                    fill=self.canvas['bg'],
                    width=self.line_width,
                    capstyle=tk.ROUND,
                    smooth=True
                )
            # Add shape drawing logic here if needed

        self.last_x = event.x
        self.last_y = event.y

    def stop_draw(self, event):
        self.last_x = None
        self.last_y = None

    def choose_color(self):
        self.current_color = colorchooser.askcolor()[1]

    def clear_canvas(self):
        self.canvas.delete("all")

    def save_canvas(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".png")
        if file_path:
            x = self.window.winfo_rootx() + self.canvas.winfo_x()
            y = self.window.winfo_rooty() + self.canvas.winfo_y()
            x1 = x + self.canvas.winfo_width()
            y1 = y + self.canvas .winfo_height()
            ImageGrab.grab().crop((x, y, x1, y1)).save(file_path)

if __name__ == "__main__":
    window = tk.Tk()
    app = BlackboardApp(window, "Blackboard App")
    window.mainloop()