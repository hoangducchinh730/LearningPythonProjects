import tkinter as tk
from logic.stopwatch import Stopwatch

class StopwatchGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("⏱ Stopwatch")
        self.root.geometry("300x200")
        self.root.resizable(False, False)

        self.stopwatch = Stopwatch()

        self.time_label = tk.Label(root, text = "00:00:00", font = ("Helvetica", 36))
        self.time_label.pack(pady=20)

        self.start_btn = tk.Button(root, text = "Start", command=self.start)
        self.pause_btn = tk.Button(root, text = "Pause", command=self.pause)
        self.reset_btn = tk.Button(root, text = "Reset", command=self.reset)

        self.start_btn.pack(side=tk.LEFT, padx=15, pady=10)
        self.pause_btn.pack(side=tk.LEFT, padx=15, pady=10)
        self.reset_btn.pack(side=tk.LEFT, padx=15, pady=10)

        self.update_display()

    def format_time(self, seconds):
        hrs = int(seconds // 3600)
        mins = int((seconds % 3600) // 60)
        secs = int(seconds % 60)
        return f"{hrs:02}:{mins:02}:{secs:02}"

    def update_display(self):
        current_time = self.stopwatch.get_time()
        self.time_label.config(text=self.format_time(current_time))
        self.root.after(1000, self.update_display)

    def start(self):
        self.stopwatch.start()
    
    def pause(self):
        self.stopwatch.pause()

    def reset(self):
        self.stopwatch.reset()
        self.time_label.config(text="00:00:00")
        

