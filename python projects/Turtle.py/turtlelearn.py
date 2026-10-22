# from turtle import Turtle,Screen
# import random
# import turtle as t
# tim=Turtle()
# # for _ in range(15):
# #     tim.forward(10)
# #     tim.penup()
# #     tim.forward(10)
# #     tim.pendown
# # colors=["red","green","blue","yellow","orange","purple"]


# t.colormode(255)


# def random_color():
  
#   r=random.randint(0,255)
#   g=random.randint(0,255)
#   b=random.randint(0,255)

#   random_color=(r,g,b)
#   return random_color

# tim.pensize(1)
# tim.speed("fastest")

# # for _ in range(150):
# #   tim.color(random_color())
# #   tim.forward(10)    
# #   tim.setheading(random.choice([0, 90, 180, 270]))


# def draw_spirograph(size_of_gap):
#   for _ in range(int(360/size_of_gap)):
#     tim.color(random_color())
#     tim.circle(100)
#     tim.setheading(tim.heading()+size_of_gap)


# draw_spirograph(5)



# import colorgram


# rgb_colors=[]
# colors=colorgram.extract('download.jpg',30)
# for color in colors:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
#     new_color =(r,g,b)
#     rgb_colors.append(new_colors)




# print(rgb_colors)

# import turtle as turtle_module
# import random

# turtle_module.colormode(255)
# tim = turtle_module.Turtle()
# tim.speed("fastest")
# tim.penup()
# tim.hideturtle()
# color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]
# tim.setheading(225)
# tim.forward(300)
# tim.setheading(0)
# number_of_dots = 100

# for dot_count in range(1, number_of_dots + 1):
#     tim.dot(20, random.choice(color_list))
#     tim.forward(50)

#     if dot_count % 10 == 0:
#         tim.setheading(90)
#         tim.forward(50)
#         tim.setheading(180)
#         tim.forward(500)
#         tim.setheading(0)


from turtle import Turtle,Screen
import random
import turtle
is_race_on=False
screen=Screen()
screen.setup(width=500,height=400)
user_text=screen.textinput(title="Make a bet",prompt="Enter your color")

y_position=[-70,-40,-10,20,50,80]
color=["red", "green", "blue", "yellow", "orange", "purple"]
all_turtles=[]
for turtle_index in range(0,6):
    
    new_turtle=Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=-230,y=y_position[turtle_index])
    new_turtle.color(color[turtle_index])
    all_turtles.append(new_turtle)

if user_text:
    is_race_on=True

while is_race_on:
   for turtle in all_turtles:
        
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_text:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")


        random_distance=random.randint(0,10)

        turtle.forward(random_distance)







screen.exitonclick()