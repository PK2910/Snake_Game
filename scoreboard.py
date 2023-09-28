from turtle import Turtle,Screen
class Score(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.score=0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.write(f"Score is:{self.score}",align='center',font=('Arial',24,'normal'))
        self.hideturtle()
    def increase(self):
        self.score+=1
        self.clear()
        self.write(f"Score is:{self.score}",align='center',font=('Arial',24,'normal'))
    def over(self):
        self.clear()
        self.write(f"Game over.Your score is {self.score}",align='center',font=('Arial',24,'normal'))
