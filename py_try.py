import random
import turtle
import pandas as pd
page=turtle.Screen()
page.title("Course")
page.addshape('py_try.gif')
turtle.shape('py_try.gif')
print(turtle.xcor(), turtle.ycor())
df=pd.read_csv('50_states.csv')
states=df.state.to_list()
count=0
while count<51:
    guess=page.textinput(f"Input! {count}/50", 'Guess the state')
    if guess==None:
        turtle.bye()
    if guess.title() in states:
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        match=df[df.state==guess.title()]
        t.goto(float(match.x), float(match.y))
        t.write(guess)
        count=count+1
        print(guess.title())
turtle.mainloop()