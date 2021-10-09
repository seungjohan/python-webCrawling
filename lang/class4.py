class Rect:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area = width*height

    def changeWidth(self, width):
        self.width = width
        self.changeArea()

    def changeHeight(self, height):
        self.height = height
        self.changeArea()

    def changeArea(self):
        self.area = self.height*self.width

    def info(self):
        print("width:", self.width, "height:", self.height, "area:", self.area)



rect1 = Rect(3, 4)
rect1.info()
rect1.changeWidth(10)
rect1.info()