import turtle
import pandas
screen = turtle.Screen() #created a screen using turtle module
screen.title("U.S. States Game") #screen ko title diya
image = "blank_states_img.gif" #image ke path ko liye
screen.addshape(image) #and turtle module ki screen ko image se replace kiye
turtle.shape(image) #uk

data = pandas.read_csv("50_states.csv") #using pandas here we read the 50states csv file and stored it in variable data
all_states = data.state.to_list() #from data variable, i.e. 50 states csv file basically, we targated the states and extracted those state names using pandas in a list
guessed_states = [] #empty list for user


while len(guessed_states) < 50: #there r total 50 states therf we compare len(GS) with 50 ukuk
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States correct", prompt="Whats the name of state").title() #using turtle, screen module here we take input from user on screen
    if answer_state == "Exit": #if users input is exit game stops
        #using list comprehension
        #missing_states = [state for state in all_states if state not in guessed_states] or nornally using for loop as above
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states) #here after user says exit we create a new csv file inside which we give user all missing states data
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states: #now if users input is a state n not just exit then this part of prog gets executed
        guessed_states.append(answer_state) #append guessed_states list with user input state
        t = turtle.Turtle() #created a turtle t using turtlw module
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state] #this is part using which names of state appears on the screen
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        
#states to learn csv


