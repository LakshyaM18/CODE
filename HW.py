from graphics import *
import random
import time

class Car(Rectangle):
    def __init__(self, win, x, y, unit):
        self.color = random.choice(['red', 'green', 'blue', 'yellow', 'black', 'white'])
        self.unit = unit
        p1 = Point(x, y - unit * 5)
        p2 = Point(x + unit * 10, y)
        super().__init__(p1, p2)
        self.setFill(self.color)
        self.draw(win)

    def draw(self, win):
        self.body = Rectangle(self.p1, self.p2)
        self.body.setFill(self.color)
        self.body.draw(win)
        
        # Calculate points for tires
        tire_radius = self.unit
        left_tire_center = Point(self.p1.getX() + 2 * tire_radius, self.p2.getY())
        right_tire_center = Point(self.p2.getX() - 2 * tire_radius, self.p2.getY())

        # Draw tires
        self.left_tire = Circle(left_tire_center, tire_radius)
        self.left_tire.setFill("black")
        self.left_tire.draw(win)

        self.right_tire = Circle(right_tire_center, tire_radius)
        self.right_tire.setFill("black")
        self.right_tire.draw(win)

    def move(self, dx, dy):
        self.body.move(dx, dy)
        self.left_tire.move(dx, dy)
        self.right_tire.move(dx, dy)
        super().move(dx, dy)

    def undraw(self):
        self.body.undraw()
        self.left_tire.undraw()
        self.right_tire.undraw()
        super().undraw()

    def getColor(self):
        return self.color

    def getScore(self):
        return int(self.unit * 10)

def isClicked(item, point):
    return point.getX() > item.getP1().getX() and point.getX() < item.getP2().getX() and \
           point.getY() > item.getP1().getY() and point.getY() < item.getP2().getY()

def draw_buildings(win, p1_x,p1_y,p2_x,p2_y,color):
    shape=Rectangle(Point(p1_x,p1_y),Point(p2_x,p2_y))
    shape.setFill(color)
    shape.draw(win)
def main():
    win = GraphWin("Car Clicking Game", 800, 600)
    win.setBackground("lightblue")
    bg = Rectangle(Point(0,25), Point(40, 40))
    bg.setFill("light blue")
    bg.draw(win)

    ground = Rectangle(Point(0,6) , Point(40, 24))
    ground.setFill("light grey")
    ground.draw(win)
    temp=4
    
    while temp<40:
        gnd_lines1= Line(Point(temp,10),Point(temp+4,10))
        gnd_lines1.setWidth(5)
        gnd_lines1.setFill("white")
        gnd_lines2= Line(Point(temp,15),Point(temp+4,15))
        gnd_lines2.setWidth(5)
        gnd_lines2.setFill("white")
        gnd_lines3= Line(Point(temp,20),Point(temp+4,20))
        gnd_lines3.setWidth(5)
        gnd_lines3.setFill("white")
        temp=temp+10
        gnd_lines1.draw(win)
        gnd_lines2.draw(win)
        gnd_lines3.draw(win)

    sun = Circle(Point(37,38), 1.5)
    sun.setFill("yellow")
    sun.setOutline("yellow")
    sun.draw(win)

    with open('hw5_input.txt','r') as file:
     # reading each line
        for line in file:
            coordinates=[]
            # reading each word
            for word in line.split():
             # displaying the words
                coordinates.append(word)
            draw_buildings(win,coordinates[0],coordinates[1],coordinates[2],coordinates[3],coordinates[4])

    global button
    button = Rectangle(Point(2,2), Point(6, 4))
    button.setFill("gray")
    button.draw(win)
    label = Text(Point(4, 3), "Start")
    label.setStyle("bold")
    label.setTextColor("white")
    label.draw(win)

    bottom_message = Text(Point(12, 5), "Please click the Start button to begin")
    bottom_message.setStyle("bold")
    bottom_message.setTextColor("green")
    bottom_message.draw(win)
    car_on_screen_message = Text(Point(15, 27), "")
    car_on_screen_message.setStyle("bold")
    car_on_screen_message.setTextColor("purple")
    car_on_screen_message.draw(win)
    score_title = Text(Point(15, 3), "Current Score: ")
    score_title.setStyle("bold")
    score_title.setSize(18)
    score_title.setTextColor("blue")
    score_title.draw(win)
    score_message = Text(Point(21, 3), "0")
    score_message.setStyle("bold")
    score_message.setSize(18)
    score_message.setTextColor("blue")
    score_message.draw(win)
    clicked_colors_message = Text(Point(29, 5), "")
    clicked_colors_message.setStyle("bold")
    clicked_colors_message.setTextColor("black")
    clicked_colors_message.draw(win)

    exit_bg = Rectangle(Point(10,5), Point(30, 20))
    exit_bg.setFill("light gray")
    exit_message = Text(Point(20, 15), "Click Exit to stop \n or Resume to continue")
    exit_message.setSize(18)
    exit_message.setStyle("bold")
    exit_message.setTextColor("red")
    global confirm_button
    confirm_button = Rectangle(Point(13, 7), Point(17, 9))
    confirm_button.setFill("gray")
    confirm_label = Text(Point(15, 8), "Exit")
    confirm_label.setStyle("bold")
    confirm_label.setTextColor("white")
    global go_back_button
    go_back_button = Rectangle(Point(23, 7), Point(27, 9))
    go_back_button.setFill("gray")
    go_back_label = Text(Point(25, 8), "Resume")
    go_back_label.setStyle("bold")
    go_back_label.setTextColor("white")

    mylabel=Text(Point(26,3),"Clicked Color:")
    mylabel.setStyle("bold")
    mylabel.draw(win)
    myrectangle=Rectangle(Point(29,2),Point(31,4))
    myrectangle.draw(win)

    pixel_per_second =10
    refresh_sec = 0.05
    gameState = 0 # 0 for initial mode, 1 for start mode, 2 for pause mode
    total_score = 0
    car_list = []
    clicked_colors = {}
    start_time1 = 0
    start_time2 = 0
    

    

    
    start_button = Rectangle(Point(10, 550), Point(90, 580))
    start_button.setFill("lightgreen")
    start_button.draw(win)
    start_text = Text(start_button.getCenter(), "Start")
    start_text.draw(win)

    pause_button = Rectangle(Point(110, 550), Point(190, 580))
    pause_button.setFill("lightcoral")
    pause_button.draw(win)
    pause_text = Text(pause_button.getCenter(), "Pause")
    pause_text.draw(win)

    score_text = Text(Point(700, 20), "Score: 0")
    score_text.draw(win)

    cars = []
    score = 0
    game_state = 0

    while True:
        if game_state == 0:
            # Wait for Start button to be clicked
            click = win.checkMouse()
            if click and isClicked(start_button, click):
                game_state = 1
                start_text.setText("Running")

        elif game_state == 1:
            # Generate and move cars
            if random.random() < 0.1:  # Adjust frequency as needed
                x = -100
                y = random.randint(100, 500)
                unit = random.uniform(0.5, 1.5)
                car = Car(win, x, y, unit)
                cars.append(car)

            for car in cars:
                car.move(5, 0)  # Adjust speed as needed

            # Check for clicks on cars
            click = win.checkMouse()
            if click:
                for car in cars:
                    if isClicked(car, click):
                        score += car.getScore()
                        score_text.setText(f"Score: {score}")
                        car.undraw()
                        cars.remove(car)

            # Check for Pause button
            if click and isClicked(pause_button, click):
                game_state = 2
                pause_text.setText("Paused")

        elif game_state == 2:
            # Wait for Resume or Exit
            click = win.checkMouse()
            if click and isClicked(start_button, click):
                game_state = 1
                start_text.setText("Running")
            elif click and isClicked(pause_button, click):
                break

    win.close()

if __name__ == "__main__":
    main()
