class shapes():
    # Constructor
    def __init__(self, FillC, OutC, OutT):
        self.fillColour = FillC
        self.outlineColour = OutC
        self.outlineThickness = OutT

    # Methods

    def rotate(self, angle):
        print("Rotated by " + str(angle))

    def copy(self):
        print("Copied")

    def enlarge(self, percentage):
        print("Enlarged by "+ str(percentage) + "%")

    def outputComFeatures(self):
        print(self.fillColour)
        print(self.outlineColour)
        print(self.outlineThickness)


class circle(shapes):
    # Constructor
    def __init__(self, FillC, OutC, OutT, rad, cent):
        self.radius = rad
        self.centre = cent
        super().__init__(FillC, OutC, OutT)

    def changeOutlineColour(self, new):
        self.outlineColour = new

    def outputCirFeatures(self):
        self.outputComFeatures()
        print(self.radius)
        print(self.centre)


class rectangle(shapes):
    def __init__(self, FillC, OutC, OutT, Len, wid):
        self.length = Len
        self.width = wid
        super().__init__(FillC, OutC, OutT)

    def addText(self, text):
        print(text)

    def outputRecFeatures(self):
        self.outputComFeatures()
        print(self.length)
        print(self.width)


circle_1 = circle("green", "red", 10, 3, (0,0))
circle_2 = circle("blue", "pink", 4, 5, (0,5))
rectangle_1 = rectangle("green", "yellow", 6, 5, 3)
rectangle_2 = rectangle("brown", "blue", 3, 10, 5)
circle_1.enlarge(50)
rectangle_1.rotate(30)
rectangle_1.addText("I am using OOP")
circle_2.changeOutlineColour("Purple")
print("Circle1 features:")
circle_1.outputCirFeatures()
print()
print("Circle2 features:")
circle_2.outputCirFeatures()
print()
print("Rectangle1 Features:")
rectangle_1.outputRecFeatures()
print()
print("Rectangle1 Features:")
rectangle_1.outputRecFeatures()
