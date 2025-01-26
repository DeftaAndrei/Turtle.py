import turtle
import time

screen = turtle.Screen()
screen.title("Funcția treaptă unitară")
screen.bgcolor("#2e2e2e")
screen.setup(width=1200, height=800)

drawer = turtle.Turtle()
drawer.speed(0)
drawer.pensize(2)
drawer.color("white")

axes = turtle.Turtle()
axes.hideturtle()
axes.speed(0)
axes.color("gray")

# Draw axes with arrows
axes.penup()
axes.goto(-550, 0)
axes.pendown()
axes.forward(1100)
axes.penup()
axes.goto(545, -5)
axes.setheading(90)
axes.pendown()
axes.forward(10)
axes.penup()
axes.goto(545, 5)
axes.setheading(270)
axes.pendown()
axes.forward(10)

axes.penup()
axes.goto(0, -400)
axes.pendown()
axes.setheading(90)
axes.forward(800)
axes.penup()
axes.goto(-5, 395)
axes.setheading(0)
axes.pendown()
axes.forward(10)
axes.penup()
axes.goto(5, 395)
axes.setheading(180)
axes.pendown()
axes.forward(10)

# Timer display
timer = turtle.Turtle()
timer.hideturtle()
timer.color("white")
timer.penup()
timer.goto(-500, 300)

def draw_unit_step():
    start_time = time.time()
    drawer.penup()
    drawer.goto(-550, 0)
    drawer.pendown()
    for x in range(-550, 0, 5):
        drawer.goto(x, 0)
        elapsed_time = time.time() - start_time
        timer.clear()
        timer.write(f"Time: {elapsed_time:.2f} s", font=("Courier", 14, "normal"))
        time.sleep(0.008)  # Adjust speed for 8 seconds total
    drawer.goto(0, 200)
    for x in range(0, 550, 5):
        drawer.goto(x, 200)
        elapsed_time = time.time() - start_time
        timer.clear()
        timer.write(f"Time: {elapsed_time:.2f} s", font=("Courier", 14, "normal"))
        time.sleep(0.008)
    timer.write(f"Final Time: {elapsed_time:.2f} s", font=("Courier", 14, "normal"))

# Header

def add_header():
    header = turtle.Turtle()
    header.hideturtle()
    header.color("white")         
    header.penup()
    header.goto(-500, 350)
    header.write(
        """
Funcția treaptă unitară
i(t) = { 0, t < 0
         1/2, t = 0
         1, t > 0
""",
        font=("Courier", 18, "normal"),
    )

add_header()
draw_unit_step()
screen.mainloop()
