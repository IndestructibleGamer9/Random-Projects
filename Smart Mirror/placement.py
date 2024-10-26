import tkinter as tk
from tkinter import font as tkfont

HEIGHT = 1080
WIDTH = 1920

class Display:
    def __init__(self):
        self.root = tk.Tk()
        self.root.attributes('-fullscreen', True)
        self.root.bind("<Escape>", self.end_fullscreen)
        self.root.configure(bg='black')
        
        self.control_window = None
        self.day_x_position = 1400  # Initial x position
        self.day_y_position = 200   # Initial y position
        self.days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        self.current_day_index = 0

    def setup(self):
        self.dt_info = {
            'day': self.days_of_week[self.current_day_index],  # Example placeholder
            'date': '2023-06-19',  # Example placeholder
            'time': '12:00PM'  # Example placeholder
        }
        self.build_display()
        self.update()
        self.create_control_window()

    def build_display(self):
        self.day_display = tk.Label(self.root, 
                                    text=self.dt_info['day'].upper(), 
                                    fg='white', bg='black', font=('Anurati', 40))
        
        self.date_display = tk.Label(self.root, 
                                     text=self.dt_info['date'], 
                                     fg='white', bg='black', font=('Exan', 30))
        
        self.time_display = tk.Label(self.root,
                                     text=self.dt_info['time'], 
                                     fg='white', bg='black', font=('Exan', 80))   

        self.time_display.place(x=1400, y=25)
        self.date_display.place(x=1650, y=280)
        self.update_day_display_position()

    def update_day_display_position(self):
        self.day_display.place(x=self.day_x_position, y=self.day_y_position)

    def end_fullscreen(self, event=None):
        self.root.attributes('-fullscreen', False)
        self.root.destroy()
        return "break"

    def update_times(self, new_times):
        self.day_display.config(text=new_times['day'].upper())
        self.date_display.config(text=new_times['date'])
        self.time_display.config(text=new_times['time'])
        self.update_day_display_position()

    def update(self):
        new_time = {
            'day': self.days_of_week[self.current_day_index],  # Example placeholder
            'date': '2023-06-19',  # Example placeholder
            'time': '12:00 PM'  # Example placeholder
        }
        if new_time != self.dt_info:
            self.update_times(new_time)
            self.dt_info = new_time
        self.root.after(1000, self.update)

    def create_control_window(self):
        self.control_window = tk.Toplevel(self.root)
        self.control_window.title("Control Panel")

        tk.Label(self.control_window, text="Day Display X Position:").pack()
        self.x_entry = tk.Entry(self.control_window)
        self.x_entry.pack()
        self.x_entry.insert(0, str(self.day_x_position))

        tk.Label(self.control_window, text="Day Display Y Position:").pack()
        self.y_entry = tk.Entry(self.control_window)
        self.y_entry.pack()
        self.y_entry.insert(0, str(self.day_y_position))

        update_button = tk.Button(self.control_window, text="Update Position", command=self.update_position)
        update_button.pack()

        next_day_button = tk.Button(self.control_window, text="Next Day", command=self.cycle_day)
        next_day_button.pack()

        self.control_window.protocol("WM_DELETE_WINDOW", self.on_control_window_close)

    def update_position(self):
        try:
            self.day_x_position = int(self.x_entry.get())
            self.day_y_position = int(self.y_entry.get())
            self.update_day_display_position()
        except ValueError:
            print("Please enter valid integer values for x and y positions.")

    def cycle_day(self):
        self.current_day_index = (self.current_day_index + 1) % len(self.days_of_week)
        new_day = self.days_of_week[self.current_day_index]
        self.dt_info['day'] = new_day
        self.day_display.config(text=new_day.upper())
        self.update_day_display_position()

    def on_control_window_close(self):
        print(f"Day Display X Position: {self.day_x_position}")
        print(f"Day Display Y Position: {self.day_y_position}")
        self.control_window.destroy()

    def main(self):
        self.setup()
        self.root.mainloop()

if __name__ == "__main__":
    disp = Display()
    disp.main()


x = [
    1595, #monday tuesday 
    1463, # wednesday
    1540, #thursday, saturday
    1652, #friday
    1605, #sunday
]
y = [
    170,
]
