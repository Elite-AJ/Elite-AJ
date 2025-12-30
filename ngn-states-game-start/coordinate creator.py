import turtle
import pandas

sc = turtle.Screen()
image = "C:/Users/HP-PC/Desktop/100DOC/Day 25/ngn-states-game-start/map-of-nig.gif"
sc.addshape(image)
turtle.shape(image)

states_names = []
state_cords = []

def get_mouse_click_coor(x, y):
    state_coordinate = (x, y)
    answer = sc.textinput(title="State Name", prompt="Enter State Name").title()
    states_names.append(answer)
    state_cords.append(state_coordinate)
    print (states_names, state_cords)

    #generate csv
    x_coords = [coord[0] for coord in state_cords]
    y_coords = [coord[1] for coord in state_cords]

    data = pandas.DataFrame({
        "Name": states_names,
        "x": x_coords,
        "y": y_coords,
    })

    data.to_csv("Need to Practice.csv")


turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop()