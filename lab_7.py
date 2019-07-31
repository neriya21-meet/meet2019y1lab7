
import turtle
import random #We'll need this later in the lab


turtle.tracer(1,0) #This helps the turtle move more smoothly

SIZE_X=800
SIZE_Y=500
turtle.setup(SIZE_X, SIZE_Y) #Curious? It's the turtle window  
turtle.bgcolor('GreenYellow')                             #size.    
turtle.penup()
turtle.color('DarkOliveGreen')

SQUARE_SIZE = 20
START_LENGTH = 6
TIME_STEP = 100


#Initialize lists
pos_list = []
stamp_list = []
food_pos = []
food_stamps = []

#Set up positions (x,y) of boxes that make up the snake
snake = turtle.clone()
snake.shape("square")

#Hide the turtle object (it's an arrow - we don't need to see it)
turtle.hideturtle()



def new_stamp():
    snake_pos = snake.pos()
    pos_list.append(snake_pos)
    x = snake.stamp()
    stamp_list.append(x)



for number in range(START_LENGTH):
    x_pos=snake.xcor() #Get x-position with snake.pos()[0]
    y_pos=snake.ycor()

    #Add SQUARE_SIZE to x_pos. Where does x_pos point to now?    
    # You're RIGHT!
    x_pos+=SQUARE_SIZE

    snake.goto(x_pos,y_pos) #Move snake to new (x,y)
   
    #Now draw the new snake part on the screen (hint, you have a 
    #function to do this
    new_stamp()
         
    
def remove_tail():
    old_stamp = stamp_list.pop(0)
    snake.clearstamp(old_stamp)
    pos_list.pop(0)

snake.direction = "Up"

UP_EDGE = 250
DOWN_EDGE = -250
RIGHT_EDGE = 400
LEFT_EDGE = -400

def up():
    snake.direction="Up" #Change direction to up
 #Update the snake drawing 
    print("You pressed the up key!")
def down():
    snake.direction='Down'
    print(' you pressed the down key!')
def left():
    snake.direction= 'Left'
    print(' left, you pressed left')
def right():
    snake.direction= 'Right'
    print(' you pressed right!')

turtle.onkeypress(up, 'Up')
turtle.onkeypress(down, 'Down')
turtle.onkeypress(left, 'Left')
turtle.onkeypress(right, 'Right')

turtle.listen()

turtle.register_shape("trash.gif")
food = turtle.clone()
food.shape("trash.gif")
food_pos = [(100,100), (-100,100), (-100,-100), (100,-100)]
food_stamps = []


for i in range(len(food_pos)):
    food.goto(food_pos[i])
    food_stamp = food.stamp()
    food_stamps.append(food_stamp)

food.hideturtle()
    
def make_food():
    #The screen positions go from -SIZE/2 to +SIZE/2
    #But we need to make food pieces only appear on game squares
    #So we cut up the game board into multiples of SQUARE_SIZE.
    min_x=-int(SIZE_X/2/SQUARE_SIZE)+1
    max_x=int(SIZE_X/2/SQUARE_SIZE)-1
    min_y=-int(SIZE_Y/2/SQUARE_SIZE)+1
    max_y=int(SIZE_Y/2/SQUARE_SIZE)-1
#Pick a position that is a random multiple of SQUARE_SIZE
    food_x = random.randint(min_x,max_x)*SQUARE_SIZE
    food_y = random.randint(min_y,max_y)*SQUARE_SIZE
    food.goto(food_x, food_y)
    ranfood_stamps=food.stamp()
    food_pos.append((food_x,food_y))
    food_stamps.append(ranfood_stamps)
    
   

def move_snake():
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
    if snake.direction == "Up":
        snake.goto(x_pos, y_pos + SQUARE_SIZE)
        print("You moved up!")
    elif snake.direction=="Down":
        snake.goto(x_pos, y_pos - SQUARE_SIZE)
        print("you moved down!")
    elif snake.direction == "Left":
        snake.goto(x_pos - SQUARE_SIZE, y_pos)
        print("you moved to the left!")
    elif snake.direction == "Right":
        snake.goto(x_pos + SQUARE_SIZE, y_pos)
        print("you moved to the right!")
    new_pos = snake.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]
    if new_x_pos >= RIGHT_EDGE:
         print("You hit the right edge! Game over!")
         quit()

    elif new_x_pos <= LEFT_EDGE:
        print("You hit the left edge! Game over!")
        quit()
    elif new_y_pos >= UP_EDGE:
        print("You hit the uppermost edge! Game over!")
        quit()
    elif new_y_pos <= DOWN_EDGE:
        print("You hit the bottom edge! Game over!")
        quit()

    for n in pos_list:
        if n == snake.pos():
            print("You have eaten yourself! Game over!")
            quit()

    
        
    ######## SPECIAL PLACE - Remember it for Part 5#If snake is on top of food item
    if snake.pos() in food_pos:
        food_index=food_pos.index(snake.pos()) #What does this do?
        food.clearstamp(food_stamps[food_index]) #Remove eaten food stamp
        food_pos.pop(food_index) #Remove eaten food position
        food_stamps.pop(food_index) #Remove eaten food stamp
        print("You have eaten the food!")
        new_stamp()
    if len(food_stamps) <= 6 :
        make_food()
    
        

    turtle.ontimer(move_snake,TIME_STEP)

        




#Make the snake stamp a new square on the screen
    #Hint - use a single function to do this
    new_stamp()

    
    

    #remove the last piece of the snake (Hint Functions are FUN!)
    remove_tail()
move_snake()


    


    



turtle.mainloop()
