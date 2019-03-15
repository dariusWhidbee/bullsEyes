from graphics import *

def draw_cir(cirX, cirY, size, color, cWin):
    circle = Circle(Point(cirX, cirY), size)
    circle.setFill(color)
    circle.draw(cWin)
    
def draw_be(bX, bY, rings, width, bColor1, bColor2, bWin):
    bSize = rings * width
    for j in range(rings):
        if (j) % 2 == 0:
            cColor = bColor1
        else:
            cColor = bColor2
        draw_cir(bX, bY, bSize - width * j, cColor, bWin)

cirSz = 60

bullWin = GraphWin("bullsEyes", cirSz * 10, cirSz * 10)
bullWin.setCoords(0,0, cirSz * 10, cirSz * 10)

draw_be(cirSz * 5, cirSz * 5, 10, 15, "purple", "black", bullWin)



bullWin.getMouse()
bullWin.close()

