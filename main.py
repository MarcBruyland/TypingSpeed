from tkinter import *
import time

MIN_WINDOW_WIDTH = 1366
MIN_WINDOW_HEIGHT = 768
PADDING = 50

#Define the function for the timer
def countdowntimer():
    cnt_seconds = int(sec.get())
    while cnt_seconds > -1:
      window.update()
      time.sleep(1)
      sec.set(str(cnt_seconds))
      cnt_seconds -= 1
    print("timer ended")
    txt = text_to_write.get("1.0", END)
    cnt_characters = len(txt)
    txt_lst = txt.split(" ")
    cnt_words = len(txt_lst)
    lbl_result["text"] = f"Result: {cnt_characters} chars/min, {cnt_words} words/min"

# ---------------------------------------------------------------------------------
# Create a window
window = Tk()
window.title("Typing Speed Test")                   # set title
window.minsize(MIN_WINDOW_WIDTH, MIN_WINDOW_HEIGHT) # set the resolution of window
window.config(padx=PADDING, pady=PADDING)           # set the padding of the window
window.resizable(width=True, height=True)           # Allow Window to be resizable

#Create Entry Widgets for SS
sec = StringVar()
entry_s = Entry(window, textvariable=sec, width=2, font='Helvetica 14')
entry_s.pack()
sec.set('60')

btn_start_timer = Button(window, text='Start timer', bd='2', bg='IndianRed1', font=('Helvetica bold', 10), command=countdowntimer)
btn_start_timer.pack()

# Text to read
text_to_read = Text(height=10, width=750)
with open("read.txt", "r", encoding="utf-8") as f:
    text = f.read()
text_to_read.insert(END, text)
text_to_read.pack()

# Text to write
text_to_write = Text(height=10, width=750)
text_to_write.focus()   # Puts cursor in textbox.
print(text_to_write.get("1.0", END)) # 1.0 = start at first line, character 0
text_to_write.pack()

# Label with result
lbl_result = Label(window, text="")
lbl_result.pack()

window.mainloop()
