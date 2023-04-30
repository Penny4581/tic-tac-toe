import turtle

# Function to draw the game board
def draw_board():
    turtle.speed(0)
    turtle.pensize(10)
    turtle.penup()
    turtle.goto(-150, 150)
    turtle.pendown()
    for i in range(4):
        turtle.forward(300)
        turtle.right(90)
    turtle.penup()
    turtle.goto(0, 150)
    turtle.right(90)
    turtle.pendown()
    turtle.forward(300)
    turtle.right(180)
    turtle.penup()
    turtle.goto(-150, 50)
    turtle.pendown()
    turtle.forward(300)
    turtle.penup()
    turtle.goto(-150, -50)
    turtle.pendown()
    turtle.forward(300)
    turtle.penup()
    turtle.goto(0, -150)
    turtle.right(90)
    turtle.pendown()
    turtle.forward(300)

# Function to draw an X in a given square
def draw_x(x, y):
    turtle.pencolor('red')
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.setheading(45)
    for i in range(4):
        turtle.forward(75)
        turtle.right(90)
    turtle.penup()

# Function to draw an O in a given square
def draw_o(x, y):
    turtle.pencolor('blue')
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.circle(37.5)
    turtle.penup()

# Main game loop
def play_game():
    turtle.setup(500, 500)
    draw_board()
    turn = 'X'
    x_positions = []
    o_positions = []
    while True:
        if turn == 'X':
            print("Player X's turn")
        else:
            print("Player O's turn")
        x = int(input("Enter a row (0-2): "))
        y = int(input("Enter a column (0-2): "))
        if (x, y) in x_positions or (x, y) in o_positions:
            print("That square is already taken. Please choose another square.")
        else:
            if turn == 'X':
                draw_x(-100 + (y * 100), 100 - (x * 100))
                x_positions.append((x, y))
                turn = 'O'
            else:
                draw_o(-100 + (y * 100), 100 - (x * 100))
                o_positions.append((x, y))
                turn = 'X'
        if check_win(x_positions):
            print("Player X wins!")
            break
        elif check_win(o_positions):
            print("Player O wins!")
            break
        elif len(x_positions) + len(o_positions) == 9:
            print("It's a tie!")
            break
    turtle.done()

# Function to check if a player has won
def check_win(positions):
    rows = [[(i, j) for j in range(3)] for i in range(3)]
    cols = [[(i, j) for i in range(3)] for j in range(3)]
    diags = [[(i, i) for i in range(3)], [(i, 2-i) for i in range(3)]]
    for line in rows + cols + diags:
        if all(position in positions for position in line):
            return True
    return False

# Start the game
play_game()
