import turtle
import pandas

sc = turtle.Screen()
sc.title("Nigerian States Game")
image = "C:/Users/HP-PC/Desktop/100DOC/Day 25/ngn-states-game-start/map-of-nig.gif"
sc.addshape(image)
turtle.shape(image)

data = pandas.read_csv("C:/Users/HP-PC/Desktop/100DOC/Day 25/ngn-states-game-start/list.csv")
state_name = [state.upper() for state in data.Name.to_list()]

guessed_state = []

while len(guessed_state) < 37:
    answer = sc.textinput(
        title= f"{len(guessed_state)}/37 States Correct", 
                            prompt= "What's another state's name?"
                            )
    
    if answer is None:
        break
    
    answer = answer.upper()
    
    #EXIT CHOICE
    if answer == "EXIT":
        missing_states = [state for state in state_name if state not in guessed_state]
        print(missing_states)
        new_Data = pandas.DataFrame(missing_states)
        new_Data.to_csv("States_to_Learn.csv", index=False)
        break

    #Already Guessed 
    if answer in guessed_state:
        continue

    #CORRECT CHOICE
    if answer in state_name:
        guessed_state.append(answer)

        t = turtle.Turtle()
        t.hideturtle()
        t.penup()

        state_data = data[data.Name.str.upper() == answer]
        t.goto(state_data.x.iloc[0], state_data.y.iloc[0])
        t.write(answer)
   
turtle.mainloop()