from turtle import Turtle, Screen
import random

is_race_on = False
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle_objects = []

screen = Screen()
#
# def move_forwards():
#     tim.forward(10)
#
# def move_backwards():
#     tim.backward(10)
#
# def move_right():
#     tim.right(10)
#
# def move_left():
#     tim.left(10)
#
# def clear():
#     tim.penup()
#     tim.clear()
#     tim.home()
#     tim.pendown()
#
#
# #유저의 키보드 이벤트를 받아들일 수 있도록 .listen
# screen.listen()
# # tim.hideturtle()
# #유저의 특정 키보드 이벤트를 method '.onkey()'에  binding 함
# screen.onkey(key= 'w', fun= move_forwards) ##어떤 함수를 다른 함수의 argument로 사용할 때는, ()를 붙이지 않는다.## 괄호를 사용하면 그 자리에서 함수가 실행된다는 의미
# screen.onkey(key= 's', fun= move_backwards)
# screen.onkey(key= 'a', fun= move_right)
# screen.onkey(key= 'd', fun= move_left)
# screen.onkey(key= 'c', fun= clear)
# #onkey()은 arguments가 없는 함수만을 인풋으로 받을 수 있음(documentation 참고)
#Adjusting the screen size
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? Enter the color: ")

if user_bet:
    is_race_on = True
# tim = Turtle(shape="turtle")
# tim.penup()
# tim.goto(x= -240, y=-100)

for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=-90 + (30 * i))    #혹은 y좌표 리스트를 만들어 공통된 인덱스(i)를 iterating 해도 된다.
    turtle_objects.append(new_turtle)

while is_race_on:
    for turtle in turtle_objects:
        # x좌표가 (최초로) 230을 넘어가는 터틀은 무조건 우승하게 됨.
        if turtle.xcor() > 220:
            is_race_on = False
            if user_bet == turtle.fillcolor():
                print("Congrats!")
            else:
                print(f"Your {user_bet} turtle lose.")
            print(f"The {turtle.fillcolor()} turtle won the race.")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()
