import tkinter as tk
from tkinter import messagebox
import turtle

# ------------------ FUNCTION TO DRAW ATOM ------------------

def show_element():
    try:
        e = int(entry_atomic.get())
    except:
        messagebox.showerror("Error", "Please enter a valid number!")
        return

    # Clear previous drawing
    t.clear()
    t.home()
    t.setheading(0)

    if e == 1:
        result_label.config(text="VALENCY: 1\nELEMENT: HYDROGEN\nELEC CONF: 1,0,0,0")
        draw_shells(1, 0)

    elif e == 2:
        result_label.config(text="VALENCY: 0\nELEMENT: HELIUM\nELEC CONF: 2,0,0,0")
        draw_shells(2, 0)

    elif e == 3:
        result_label.config(text="VALENCY: 1\nELEMENT: LITHIUM\nELEC CONF: 2,1,0,0")
        draw_shells(2, 1)

    elif e == 4:
        result_label.config(text="VALENCY: 2\nELEMENT: BERYLLIUM\nELEC CONF: 2,2,0,0")
        draw_shells(2, 2)

    else:
        messagebox.showinfo("Info", "Element not added yet!")

# ------------------ FUNCTION TO DRAW SHELLS ------------------

def draw_shells(first_shell, second_shell):

    radius1 = 75
    radius2 = 120

    # Draw nucleus (center dot)
    t.penup()
    t.goto(0, 0)
    t.dot(30, "red")

    t.goto(0, -radius1)
    t.pendown()
    t.circle(radius1)
    t.penup()

    for i in range(first_shell):
        angle = 360 / first_shell * i
        t.goto(0, 0)
        t.setheading(angle)
        t.forward(radius1)
        t.dot(15, "blue")

    if second_shell > 0:
        t.goto(0, -radius2)
        t.setheading(0)
        t.pendown()
        t.circle(radius2)
        t.penup()

        for i in range(second_shell):
            angle = 360 / second_shell * i
            t.goto(0, 0)
            t.setheading(angle)
            t.forward(radius2)
            t.dot(15, "green")


root = tk.Tk()
root.title("Elementor App")
root.geometry("500x650")

tk.Label(root, text="Enter Your Name:", font=("Arial", 12)).pack(pady=5)
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="Enter Atomic Number:", font=("Arial", 12)).pack(pady=5)
entry_atomic = tk.Entry(root)
entry_atomic.pack()

tk.Button(root, text="Show Element", command=show_element).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

# ------------------ TURTLE CANVAS ------------------

canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

screen = turtle.TurtleScreen(canvas)
screen.bgcolor("white")

t = turtle.RawTurtle(screen)
t.speed(3)
t.hideturtle()

root.mainloop()