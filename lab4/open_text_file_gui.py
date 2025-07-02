import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def open_file():
    file_path = filedialog.askopenfilename(
        title="Open Text File",
        filetypes=[("Text Files", "*.txt")]
    )
    
    if file_path:
        try:
            with open(file_path, "r") as file:
                content = file.read()
                text_area.delete(1.0, tk.END)
                text_area.insert(tk.END, content)
        except Exception as e:
            messagebox.showerror("Error", f"Could not open file: {e}")

root = tk.Tk()
root.title("Text File Viewer")
root.geometry("600x400")

top_label = tk.Label(root, text="Text File Viewer", bg="red", fg="white", font=("Arial", 16, "bold"))
top_label.pack(fill=tk.X)

open_button = tk.Button(root, text="Open Text File", command=open_file)
open_button.pack(pady=10)

text_area = tk.Text(root, wrap=tk.WORD)
text_area.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

root.mainloop()

