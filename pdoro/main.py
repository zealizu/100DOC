# Import all tkinter components for GUI creation
from tkinter import *
# Import messagebox for showing notifications
from tkinter import messagebox
# Import sys for system-specific parameters and functions
import sys
# Import os for operating system interface
import os

def resource_path(relative_path):
    """
    Get the absolute path to a resource file.
    
    This function works both during development and when the app is packaged
    with PyInstaller. PyInstaller creates a temporary folder and stores the
    path in _MEIPASS when the app is bundled.
    
    Args:
        relative_path (str): The relative path to the resource file
        
    Returns:
        str: The absolute path to the resource file
    """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        # If not running from PyInstaller bundle, use current directory
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# ---------------------------- CONSTANTS ------------------------------- #
# Color constants for the UI theme
PINK = "#e2979c"        # Light pink color for short break labels
RED = "#e7305b"         # Red color for long break labels
GREEN = "#9bdeac"       # Green color for work labels and checkmarks
YELLOW = "#f7f5dd"      # Background color for the entire application
FONT_NAME = "Courier"   # Font family used throughout the application

# Timer duration constants (in minutes)
WORK_MIN = 25           # Work session duration
SHORT_BREAK_MIN = 5     # Short break duration
LONG_BREAK_MIN = 20     # Long break duration (after every 4 work sessions)

# Global variables to track timer state
reps = 0                # Counter for completed timer sessions
marks = ""              # String to store checkmark symbols for completed work sessions
timer = None            # Variable to store the timer reference for cancellation

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    """
    Reset the timer to its initial state.
    
    This function cancels any running timer, resets all counters and displays,
    and returns the interface to its starting configuration.
    """
    global reps, marks
    # Cancel the currently running timer if it exists
    window.after_cancel(timer)
    # Reset the repetition counter to 0
    reps = 0
    # Clear all checkmarks
    marks = ""
    # Reset timer display to show 00:00
    canvas.itemconfig(timer_text, text = "00:00")
    # Clear the checkmark display
    chk_mark.config(text= marks)
    # Reset the timer label to default state
    timer_label.config(text= "Timer")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    """
    Start the appropriate timer session based on the current repetition count.
    
    The Pomodoro Technique follows this pattern:
    - Work sessions (25 min) on odd repetitions (1, 3, 5, 7)
    - Short breaks (5 min) on even repetitions (2, 4, 6)
    - Long break (20 min) on every 8th repetition
    
    This function also updates the UI labels and shows appropriate notifications.
    """
    global reps
    # Increment the repetition counter
    reps += 1
    # Convert minutes to seconds for countdown
    work_secs = WORK_MIN * 60
    short_break_secs = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60
    
    # Check if it's time for a long break (every 8th repetition)
    if reps % 8 == 0:
        count_down(long_break_secs)
        # Update label to show "Break" in red color
        timer_label.config(text="Break", fg= RED)
        # Show notification popup
        os.system("afplay /System/Library/Sounds/Glass.aiff")
        messagebox.showinfo("Pomodoro Timer", "Time's up! Take a break 🍅")
        
    # Check if it's time for a short break (even repetitions, except 8th)
    elif reps % 2 == 0:
        count_down(short_break_secs)
        # Update label to show "Break" in pink color
        timer_label.config(text="Break", fg= PINK)
        # Show notification popup
        os.system("afplay /System/Library/Sounds/Glass.aiff")
        messagebox.showinfo("Pomodoro Timer", "Time's up! Take a break 🍅")
    # Otherwise, it's a work session (odd repetitions)
    else:
        count_down(work_secs)
        # Update label to show "Work" in green color
        timer_label.config(text="Work", fg=GREEN)
        # Show notification popup
        os.system("afplay /System/Library/Sounds/Glass.aiff")
        messagebox.showinfo("Pomodoro Timer", "Time to get back to work")

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    """
    Handle the countdown mechanism for the timer.
    
    This function converts seconds to MM:SS format, updates the display,
    and recursively calls itself every second until the countdown reaches 0.
    When the countdown finishes, it automatically starts the next timer session.
    
    Args:
        count (int): The number of seconds remaining in the current session
    """
    global marks
    
    # Convert total seconds to minutes and seconds
    count_min = count // 60          # Integer division to get minutes
    count_sec = count % 60           # Modulo to get remaining seconds
    
    # Add leading zero to seconds if it's a single digit (formatting)
    if len(str(count_sec)) == 1:
        count_sec = "0" + str(count_sec)
    
    # Format time as MM:SS string
    time = f"{count_min}:{count_sec}"
    # Update the timer display on the canvas
    canvas.itemconfig(timer_text, text = time)
    
    # If there's still time left, schedule the next countdown call
    if count > 0:
        global timer
        # Schedule this function to run again after 1000ms (1 second) with count-1
        timer = window.after(1000, count_down, count -1)
    # If countdown has finished (count = 0)
    else:
        # Automatically start the next timer session
        start_timer()
        # If this was a work session (even reps after completion), add a checkmark
        if reps % 2 == 0:
            marks += "✔"
            # Update the checkmark display
            chk_mark.config(text= marks)

# ---------------------------- UI SETUP ------------------------------- #
# Create the main window
window = Tk()
# Set window title
window.title("Pomodoro")
# Configure window padding (100px horizontal, 50px vertical) and background color
window.config(padx=100, pady=50, bg=YELLOW)

# Create a canvas widget for drawing the tomato image and timer text
canvas = Canvas(width= 200, height=224, bg= YELLOW, highlightthickness=0)
# Load the tomato image using the resource_path function for PyInstaller compatibility
tomato_img = PhotoImage(file=resource_path("100DOC/pdoro/tomato.png"))
# Draw the tomato image at the center of the canvas (100, 112)
canvas.create_image(100, 112, image= tomato_img)
# Create timer text display on the canvas, positioned over the tomato image
timer_text = canvas.create_text(100,130, text= "00:00", fill= "white", font=(FONT_NAME, 35, "bold"))
# Position the canvas in the grid layout (row 1, column 1)
canvas.grid(row=1, column=1)

# Create and configure the timer label at the top of the interface
timer_label = Label(text= "Timer", font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW)
# Position the timer label in the grid (row 0, column 1, centered above canvas)
timer_label.grid(row=0,column=1)

# Create the Start button with styling to match the theme
start_btn = Button(text="Start", bg=YELLOW, activebackground=YELLOW,highlightthickness=0,bd=0,relief="flat",highlightbackground=YELLOW, command=start_timer)
# Position the start button in the grid (row 2, column 0, bottom left)
start_btn.grid(row=2, column=0)

# Create the Reset button with styling to match the theme
reset_btn = Button(text="Reset",bg=YELLOW, activebackground=YELLOW,highlightthickness=0,bd=0,relief="flat",highlightbackground=YELLOW,command= reset_timer)
# Position the reset button in the grid (row 2, column 2, bottom right)
reset_btn.grid(row=2, column=2)

# Create a label to display checkmarks for completed work sessions
chk_mark = Label(fg=GREEN, bg=YELLOW)
# Position the checkmark label in the grid (row 3, column 1, bottom center)
chk_mark.grid(row=3, column=1)

# Start the GUI event loop - this keeps the window open and responsive
window.mainloop()