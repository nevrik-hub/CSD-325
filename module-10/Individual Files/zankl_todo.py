"""
Course: CSD-325
Module: 10.2 Assignment - GUI ToDo
Description: Modified Tkinter GUI To-Do List application.
"""

import tkinter as tk


class TodoList(tk.Tk):
    """Main application window for the GUI To-Do List."""

    def __init__(self):
        super().__init__()

        # Window Configuration
        self.title("Zankl-ToDo")
        self.geometry("320x450")

        # Menu Bar Setup
        menu_bar = tk.Menu(self)
        self.config(menu=menu_bar)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Exit", command=self.destroy)
        menu_bar.add_cascade(label="File", menu=file_menu)

        # Instruction Header Label
        instruction_label = tk.Label(
            self,
            text="Items Added --- ** Right Click Item to Delete **",
            bg="#8A2BE2",
            fg="#FFFFFF",
            font=("Arial", 10, "bold"),
            pady=8
        )
        instruction_label.pack(fill="x")

        # Task Entry Widget
        self.task_create = tk.Entry(self, font=("Arial", 11))
        self.task_create.pack(pady=10, padx=10, fill="x")
        self.task_create.focus_set()
        self.task_create.bind("<Return>", self.add_task)

        # Canvas & Scrollbar Setup
        self.tasks_canvas = tk.Canvas(self, highlightthickness=0)
        self.tasks_frame = tk.Frame(self.tasks_canvas)
        scrollbar = tk.Scrollbar(
            self, orient="vertical", command=self.tasks_canvas.yview
        )

        self.tasks_canvas.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        self.tasks_canvas.pack(side="left", fill="both", expand=True)

        self.canvas_frame = self.tasks_canvas.create_window(
            (0, 0), window=self.tasks_frame, anchor="nw"
        )

        self.tasks_frame.bind("<Configure>", self.on_frame_configure)
        self.tasks_canvas.bind("<Configure>", self.on_canvas_configure)

        self.colour_schemes = [
            {"bg": "#EAB308", "fg": "#000000"},
            {"bg": "#8A2BE2", "fg": "#FFFFFF"}
        ]

    def add_task(self, event=None):
        """Adds a new task label to the scrollable frame."""
        _ = event  # Silence unused-argument
        task_text = self.task_create.get().strip()
        if not task_text:
            return

        colour_scheme = self.colour_schemes[
            len(self.tasks_frame.winfo_children()) % 2
        ]

        task_label = tk.Label(
            self.tasks_frame,
            text=task_text,
            bg=colour_scheme["bg"],
            fg=colour_scheme["fg"],
            font=("Arial", 11, "bold"),
            pady=12,
            anchor="center"
        )

        task_label.bind("<Button-2>", self.remove_task)
        task_label.bind("<Button-3>", self.remove_task)

        task_label.pack(side="top", fill="x", expand=True)
        self.task_create.delete(0, tk.END)

    def remove_task(self, event):
        """Removes the clicked task label from the GUI."""
        event.widget.destroy()

    def on_frame_configure(self, event=None):
        """Updates scrollable region based on the frame size."""
        _ = event  # Silence unused-argument
        self.tasks_canvas.configure(
            scrollregion=self.tasks_canvas.bbox("all")
        )

    def on_canvas_configure(self, event):
        """Resizes the inner canvas frame when window resizes."""
        self.tasks_canvas.itemconfig(self.canvas_frame, width=event.width)


if __name__ == "__main__":
    app = TodoList()
    app.mainloop()
