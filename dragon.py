from tkinter import *
window = Tk()
window.title('silass hi')
def click():
    print("hello!!!!")

window = Canvas(window, width= 800, height = 2000)
window.pack()
image = PhotoImage(file = 'C:\\Users\\Jason Burchard\\Pictures\\dragon2.0.PNG')
window.create_image(0, 0, anchor = NW, image = image)
window.mainloop()
