import tkinter as tk
import keyboard

class SubtitlesBlocker:
    def __init__(self, root):
        self.root = root
        self.root.title("Subtitles Blocker")
        self.root.attributes("-topmost", True)
        self.root.configure(bg="black")
        self.root.geometry("800x100")
        self.locked = False

        self.frame = tk.Frame(root, bg="black")
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.label = tk.Label(self.frame, text="Subtitles Blocker", bg="black", fg="white")
        self.label.pack(pady=20)

        keyboard.add_hotkey("ctrl+alt+x", self.toggle_lock)

        self.root.bind("<Button-1>", self.on_click)

    def toggle_lock(self):
        self.locked = not self.locked
        if self.locked:
            self.root.overrideredirect(True)  # Remove window decorations
        else:
            self.root.overrideredirect(False)  # Add window decorations

    def on_click(self, event):
        if self.locked:
            return "break"

if __name__ == "__main__":
    root = tk.Tk()
    app = SubtitlesBlocker(root)
    root.mainloop()
