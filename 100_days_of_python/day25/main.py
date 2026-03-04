import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image) # adding such image to shape in screen
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
#data.state this is get me a data series of state column
all_states = data.state.to_list() # from data->state column series->turn into list
guessed_states = []

# get x y coordinate on click python turtle
# print(answer_state)

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state name").title()

    #if answer_state is one of the states in all the states of the 50_states.csv
    if answer_state == "Exit":
        # missing_states = [state for state in all_states if state not in guessed_states]
        #list and below loop and append both are work
        missing_state = []
        for state in all_states:
            if state not in guessed_states: # mean the missed state
                missing_state.append(state)
        # print(missing_state) # console the all missing states in list
        # saving the missing states to a .csv
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("missing_states_learn.csv")
        break

        
    if answer_state in all_states: #if they got it right:
        guessed_states.append(answer_state)
        # create a turtle to write the name of the state at the state's x and y coordinate
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state] # pull out the row where the state is equal to answer_state
        t.goto(state_data.x.item(), state_data.y.item()) # state_data in corresponding x y
        # t.write(state_data.state) did this write state with other details in map
        # t.write(state_data.state.item()) # write state
        t.write(answer_state)

