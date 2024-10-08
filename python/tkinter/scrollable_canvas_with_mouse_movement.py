import tkinter as tk
from tkinter import ttk
import platform

class ScrollableCanvas(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.canvas = tk.Canvas(self, width=400, height=300)
        self.scrollbar_x = ttk.Scrollbar(self, orient="horizontal", command=self.canvas.xview)
        self.scrollbar_y = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas)

        self.canvas.configure(xscrollcommand=self.scrollbar_x.set, yscrollcommand=self.scrollbar_y.set)

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        self.canvas.grid(row=0, column=0, sticky="nsew")
        self.scrollbar_x.grid(row=1, column=0, sticky="ew")
        self.scrollbar_y.grid(row=0, column=1, sticky="ns")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.scrollable_frame.bind("<Configure>", self.on_frame_configure)
        self.canvas.bind("<ButtonPress-1>", self.on_mouse_press)
        self.canvas.bind("<B1-Motion>", self.on_mouse_drag)

        # Bind scrolling events
        if platform.system() == "Darwin":  # macOS
            self.canvas.bind("<MouseWheel>", self.on_mousewheel)
            self.canvas.bind("<Option-MouseWheel>", self.on_mousewheel_horizontal)
        else:  # Windows and Linux
            self.canvas.bind("<MouseWheel>", self.on_mousewheel)
            self.canvas.bind("<Shift-MouseWheel>", self.on_shift_mousewheel)

        # Add content that requires both vertical and horizontal scrolling
        for i in range(50):
            frame = tk.Frame(self.scrollable_frame)
            frame.pack(fill="x")
            for j in range(20):
                label = tk.Label(frame, text=f"Label {i},{j}", width=10, borderwidth=1, relief="solid")
                label.pack(side="left")

    def on_frame_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def on_mouse_press(self, event):
        self.canvas.scan_mark(event.x, event.y)

    def on_mouse_drag(self, event):
        self.canvas.scan_dragto(event.x, event.y, gain=1)

    def on_mousewheel(self, event):
        if platform.system() == "Darwin":  # macOS
            self.canvas.yview_scroll(-1 * event.delta, "units")
        else:  # Windows and Linux
            self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def on_mousewheel_horizontal(self, event):
        if platform.system() == "Darwin":  # macOS
            self.canvas.xview_scroll(-1 * event.delta, "units")

    def on_shift_mousewheel(self, event):
        if platform.system() != "Darwin":  # Windows and Linux
            self.canvas.xview_scroll(int(-1 * (event.delta / 120)), "units")

root = tk.Tk()
scrollable_canvas = ScrollableCanvas(root)
scrollable_canvas.pack(fill="both", expand=True)

# macOS specific event handling
if platform.system() == "Darwin":
    def handle_trackpad_scroll(event):
        if event.num == 4:  # Scroll down
            scrollable_canvas.canvas.yview_scroll(1, "units")
        elif event.num == 5:  # Scroll up
            scrollable_canvas.canvas.yview_scroll(-1, "units")
    
    root.bind("<Button-4>", handle_trackpad_scroll)
    root.bind("<Button-5>", handle_trackpad_scroll)
    root.bind("<Control-Button-4>", lambda event: scrollable_canvas.canvas.xview_scroll(1, "units"))
    root.bind("<Control-Button-5>", lambda event: scrollable_canvas.canvas.xview_scroll(-1, "units"))

root.mainloop()