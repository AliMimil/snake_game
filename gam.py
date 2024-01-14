import tkinter
import random

rows = 25
cols =25
tile_size = 25

window_width = tile_size*rows
window_height = tile_size*cols


class tile:
    def __init__(self,x,y):
        self.x=x
        self.y=y

#game windw

window=tkinter.Tk()
window.title("snake")
window.resizable(False,False)


canvas=tkinter.Canvas(window,bg='black',width=window_width,height=window_height,borderwidth= 0,highlightthickness = 0 )
canvas.pack()
window.update()
#center thz window
window_width=window.winfo_width()
window_height=window.winfo_height()
screen_width=window.winfo_screenwidth()
screen_height=window.winfo_screenheight()

window_x=int((screen_width/2 )-(window_width/2))
window_y = int((screen_height/2)-(window_height/2))

window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")



#initialize game
snake=tile(5*tile_size,5*tile_size)
food=tile(10*tile_size,10*tile_size)
snake_body=[]

velocityx=0
velocityy=0
game_over=False
score=0
def change_direction(e):
    #print(e)
    #print(e.keysym)
    global velocityy,velocityx,game_over

    if(game_over):
        return
    if(e.keysym=="Up" and velocityy !=1):
        velocityx=0
        velocityy=-1
    elif(e.keysym=="Down" and velocityy !=-1):
        velocityx=0
        velocityy=1
    elif(e.keysym=="Left" and velocityx !=1):
        velocityx=-1
        velocityy=0
    elif(e.keysym=="Right" and velocityx !=-1):
        velocityx=1
        velocityy=0
    
def move():
    global snake,game_over,score

    if(game_over):
        return
    
    if(snake.x<0 or snake.x>= window_width or snake.y<0 or snake.y>=window_height):
        game_over=True
        return
    for t in snake_body:
        if(snake.x==t.x and snake.y ==t.y):
            game_over=True
            return
    if (snake.x==food.x)and(snake.y==food.y):
        snake_body.append(tile(food.x,food.y))
        food.x=random.randint(0,cols-1)*tile_size
        food.y=random.randint(0,rows-1)*tile_size
        score+=1

    for i in range(len(snake_body)-1,-1,-1):
        til=snake_body[i]
        if(i==0):
            til.x=snake.x
            til.y=snake.y
        else:
            prev_tile=snake_body[i-1]
            til.x =prev_tile.x
            til.y =prev_tile.y

    
    snake.x +=velocityx*tile_size
    snake.y +=velocityy*tile_size
def draw():
    global snake,food,score,snake_body,game_over
    move()

    canvas.delete("all")
    canvas.create_rectangle(food.x,food.y,food.x+tile_size,food.y+tile_size,fill="red")

    canvas.create_rectangle(snake.x,snake.y,snake.x+tile_size,snake.y+tile_size,fill="lime green")
    for tile in snake_body:
        canvas.create_rectangle(tile.x,tile.y,tile.x+tile_size,tile.y+tile_size,fill="lime green")
    if (game_over):
        canvas.create_text(window_width/2,window_height/2,font="Arial 20", text=f"Game over: {score}",fill="white")        

    else:
        canvas.create_text(30,20,font="Arial 10",text=f"score:{score}",fill="white")
    window.after(100,draw)

draw()    

window.bind("<KeyRelease>",change_direction)
window.mainloop()
