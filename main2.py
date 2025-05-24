import cv2
import numpy as np
import tkinter as tk
from tkinter import colorchooser
from PIL import Image, ImageTk

class BlackboardApp:
    def __init__(self, window, window_title):
        self.window = window
        self.window.title(window_title)
        
        self.screen_width = self.window.winfo_screenwidth()
        self.screen_height = self.window.winfo_screenheight()
        self.window.geometry(f"{self.screen_width}x{self.screen_height}")
        
        self.camera_width = 200
        self.camera_height = 200
        
        self.canvas = tk.Canvas(window, width=self.screen_width, height=self.screen_height, bg='black', cursor="pencil")
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        self.tool_frame = tk.Frame(window, bg='gray')
        self.tool_frame.place(x=10, y=10)
        
        self.current_tool = "pen"
        self.current_color = "white"
        self.line_width = 2
        
        self.last_x = None
        self.last_y = None
        
        self.setup_tools()
        
        self.canvas.bind("<Button-1>", self.start_draw)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.stop_draw)
        
        self.camera = cv2.VideoCapture(0)
        self.camera_canvas = tk.Canvas(window, width=self.camera_width, height=self.camera_height)
        self.camera_canvas.place(x=self.screen_width-self.camera_width-10, y=self.screen_height-self.camera_height-10)
        self.camera_on = False
        
        self.update_camera()
        self.camera_on = True  # Camera is on by default
        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.window.bind("<Escape>", self.on_closing)
        self.window.bind("<F11>", self.toggle_fullscreen)
        self.window.bind("<F12>", self.toggle_camera)
        self.window.bind("<Control-s>", self.save_canvas)
        self.window.bind("<Control-c>", self.choose_color)
        self.window.bind("<Control-e>", self.toggle_eraser)
        self.window.bind("<Control-p>", self.toggle_pen)
        self.window.bind("<Control-x>", self.toggle_pencil)
        self.window.bind("<Control-r>", self.toggle_rectangle)
        self.window.bind("<Control-o>", self.toggle_oval)
        
        self.window.mainloop()
    
    def setup_tools(self):
        tools = [
            ("Pen", lambda: self.set_tool("pen")),
            ("Pencil", lambda: self.set_tool("pencil")),
            ("Eraser", lambda: self.set_tool("eraser")),
            ("Color", self.choose_color),
            ("Clear", self.clear_canvas),
            ("Save", self.save_canvas),
            ("Camera", self.toggle_camera),
            ("Fullscreen", self.toggle_fullscreen),
            ("Exit", self.on_closing),
            ("Toggle Tools", self.toggle_tools),
            ("Toggle Eraser", self.toggle_eraser),
            ("Toggle Pen", self.toggle_pen),
            ("Toggle Pencil", self.toggle_pencil),
            ("Toggle Rectangle", self.toggle_rectangle),
            ("Toggle Oval", self.toggle_oval),
            ("Toggle Save", self.save_canvas),
            ("Toggle Color", self.choose_color),


        ]
        for text, command in tools:
            tk.Button(self.tool_frame, text=text, command=command, width=10).pack(pady=5)
    
    def set_tool(self, tool):
        self.current_tool = tool
        if tool == "eraser":
            self.line_width = 20
            self.current_color = "black"
            self.canvas.config(cursor="circle")
        elif tool == "pencil":
            self.line_width = 1
            self.canvas.config(cursor="pencil")
        else:  # pen
            self.line_width = 2
            self.canvas.config(cursor="spraycan")
        
        if tool != "eraser":
            self.current_color = self.current_color  # Maintain the current color for pen and pencil
    
    def choose_color(self):
        color = colorchooser.askcolor(title="Choose color")[1]
        if color:
            self.current_color = color
            if self.current_tool == "eraser":
                self.set_tool("pen")  # Switch back to pen after choosing a color
    
    def start_draw(self, event):
        self.last_x = event.x
        self.last_y = event.y
    
    def draw(self, event):
        if self.last_x and self.last_y:
            x, y = event.x, event.y
            if self.current_tool == "eraser":
                self.canvas.create_rectangle(x-self.line_width, y-self.line_width, x+self.line_width, y+self.line_width, 
                                             fill='black', outline='black')
            else:
                self.canvas.create_line(self.last_x, self.last_y, x, y, 
                                        fill=self.current_color, width=self.line_width, 
                                        capstyle=tk.ROUND, smooth=tk.TRUE)
            self.last_x, self.last_y = x, y
    
    def stop_draw(self, event):
        self.last_x = None
        self.last_y = None
    
    def clear_canvas(self):
        self.canvas.delete("all")
    
    def update_camera(self):
      if self.camera_on:
        ret, frame = self.camera.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = cv2.resize(frame, (self.camera_width, self.camera_height))
            photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
            self.camera_canvas.create_image(0, 0, image=photo, anchor=tk.NW)
            self.camera_canvas.image = photo
      else:
        self.camera_canvas.delete("all")
      self.window.after(10, self.update_camera)


    def toggle_camera(self, event=None):
     if self.camera_on:
        self.camera.release()
        self.camera_on = False
        self.camera_canvas.delete("all")
     else:
        self.camera = cv2.VideoCapture(0)
        self.camera_on = True

    def toggle_fullscreen(self, event=None):
        self.window.attributes("-fullscreen", not self.window.attributes("-fullscreen"))

    def on_closing(self, event=None):
        if self.camera_on:
            self.camera.release()
        self.window.destroy()

    def toggle_tools(self, event=None):
        if self.tool_frame.winfo_ismapped():
            self.tool_frame.place_forget()
        else:
            self.tool_frame.place(x=10, y=10)
    
    def save_canvas(self, event=None):
      self.canvas.postscript(file="drawing.eps")
      print("Canvas saved as drawing.eps")


BlackboardApp(tk.Tk(), "Blackboard with Camera")