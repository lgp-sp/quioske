#!/usr/bin/env python3
import webview
import os
import tkinter as tk
from tkinter import filedialog, ttk
import gc
import sys
import threading
import time

def memory_manager():
    while True:
        gc.collect()  # Force garbage collection
        time.sleep(300)  # Run every 5 minutes

def start_webview():
    file_path = path_label.cget("text")
    if file_path and os.path.exists(file_path):
        root.destroy()
        
        # Start memory management thread
        memory_thread = threading.Thread(target=memory_manager, daemon=True)
        memory_thread.start()
        
        # Get screen dimensions from the webview
        screen_info = webview.screens[0]
        window = webview.create_window(
            'Quiz Application',
            'file://' + file_path.replace('\\', '/'),
            fullscreen=True,
            frameless=True,
            text_select=False,
            transparent=False,
            on_top=True,
            min_size=(screen_info.width, screen_info.height)
        )
        
        # Force fullscreen and always on top
        window.events.shown += lambda: window.toggle_fullscreen()
        window.events.shown += lambda: window.move_to_front()
        
        # Clear memory before starting webview
        gc.collect()
        
        webview.start()
    else:
        path_label.config(text="Please select a valid HTML file")

def select_file():
    file_path = filedialog.askopenfilename(
        title="Select HTML file",
        filetypes=[("HTML files", "*.html")]
    )
    if file_path:
        path_label.config(text=file_path)
        return file_path
    return None

# Create file selector window
root = tk.Tk()
root.title("Select Quiz File")
root.geometry("600x350")

# Create and pack widgets
frame = ttk.Frame(root, padding="20")
frame.pack(fill=tk.BOTH, expand=True)

browse_button = ttk.Button(frame, text="Browse HTML File", command=select_file)
browse_button.pack(pady=10)

path_label = ttk.Label(frame, text="No file selected", wraplength=550)
path_label.pack(pady=10)

start_button = ttk.Button(frame, text="Start Quiz", command=start_webview)
start_button.pack(pady=10)

root.mainloop()