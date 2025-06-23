import tkinter as tk
from tkinter import messagebox
from playsound import playsound
import os
import winsound

class PomodoroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pomodoro Timer")
        self.root.geometry("450x400")
        self.root.resizable(False, False)
        self.root.configure(bg="#2C3E50")

        self.work_time = 25 * 60
        self.short_break = 5 * 60
        self.long_break = 15 * 60
        self.remaining = self.work_time
        self.current_stage = 0  
        self.cycles = 0
        self.paused = True

        self.create_settings_frame()
        self.create_timer_display()
        self.create_buttons()

    def create_settings_frame(self):
        settings_frame = tk.Frame(self.root, bg="#2C3E50")
        settings_frame.pack(pady=10)

        tk.Label(settings_frame, text="Работа (мин):", bg="#2C3E50", fg="white").grid(row=0, column=0, padx=5)
        self.work_entry = tk.Entry(settings_frame, width=5)
        self.work_entry.grid(row=0, column=1, padx=5)
        self.work_entry.insert(0, "25")

        tk.Label(settings_frame, text="Перерыв (мин):", bg="#2C3E50", fg="white").grid(row=0, column=2, padx=5)
        self.break_entry = tk.Entry(settings_frame, width=5)
        self.break_entry.grid(row=0, column=3, padx=5)
        self.break_entry.insert(0, "5")

        tk.Label(settings_frame, text="Длинный перерыв (мин):", bg="#2C3E50", fg="white").grid(row=1, column=0, padx=5)
        self.long_break_entry = tk.Entry(settings_frame, width=5)
        self.long_break_entry.grid(row=1, column=1, padx=5)
        self.long_break_entry.insert(0, "15")

        self.save_button = tk.Button(settings_frame, text="Сохранить", command=self.save_settings, width=10, bg="#3498DB", fg="white")
        self.save_button.grid(row=1, column=2, columnspan=2, padx=5)

    def create_timer_display(self):
        self.stage_label = tk.Label(self.root, text="Работа", font=("Helvetica", 24), bg="#2C3E50", fg="white")
        self.stage_label.pack(pady=10)

        self.time_label = tk.Label(self.root, text="25:00", font=("Helvetica", 48), bg="#2C3E50", fg="#E74C3C")
        self.time_label.pack()

    def create_buttons(self):
        button_frame = tk.Frame(self.root, bg="#2C3E50")
        button_frame.pack(pady=20)

        self.start_button = tk.Button(button_frame, text="▶ Start", width=8, command=self.start_timer, bg="#2ECC71", fg="white")
        self.start_button.grid(row=0, column=0, padx=5)

        self.pause_button = tk.Button(button_frame, text="⏸ Pause", width=8, command=self.pause_timer, bg="#F39C12", fg="white")
        self.pause_button.grid(row=0, column=1, padx=5)

        self.reset_button = tk.Button(button_frame, text="🔄 Reset", width=8, command=self.reset_timer, bg="#E74C3C", fg="white")
        self.reset_button.grid(row=0, column=2, padx=5)

    def save_settings(self):
        try:
            work = int(self.work_entry.get())
            short_break = int(self.break_entry.get())
            long_break = int(self.long_break_entry.get())

            if work <= 0 or short_break <= 0 or long_break <= 0:
                raise ValueError("Все значения должны быть положительными числами.")

            self.work_time = work * 60
            self.short_break = short_break * 60
            self.long_break = long_break * 60
            self.reset_timer()
            messagebox.showinfo("Настройки", "Время успешно обновлено!")

        except ValueError as e:
            messagebox.showerror("Ошибка", str(e))

    def start_timer(self):
        if self.remaining <= 0:
            self.reset_timer()
        self.paused = False
        self.run_timer()

    def pause_timer(self):
        self.paused = True

    def reset_timer(self):
        self.paused = True
        self.remaining = self.work_time
        self.cycles = 0
        self.current_stage = 0
        self.stage_label.config(text="Работа")
        self.update_time_label()

    def run_timer(self):
        if self.paused:
            return

        if self.remaining > 0:
            self.remaining -= 1
            self.update_time_label()
            self.root.after(1000, self.run_timer)
        else:
            self.play_sound()
            self.cycles += 1

            if self.cycles % 4 == 0:
                self.current_stage = 2
                self.remaining = self.long_break
                self.stage_label.config(text="Длинный перерыв")
            elif self.cycles % 2 == 1:
                self.current_stage = 1
                self.remaining = self.short_break
                self.stage_label.config(text="Перерыв")
            else:
                self.current_stage = 0
                self.remaining = self.work_time
                self.stage_label.config(text="Работа")

            self.update_time_label()
            self.root.after(1000, self.run_timer)

    def update_time_label(self):
        minutes, seconds = divmod(self.remaining, 60)
        self.time_label.config(text=f"{minutes:02}:{seconds:02}")

    def play_sound(self):
        try:
            playsound(os.path.join(os.path.dirname(__file__), "Atom.mp3"))
        except Exception:
            winsound.Beep(1000, 1000)

if __name__ == "__main__":
    root = tk.Tk()
    app = PomodoroApp(root)
    root.mainloop()