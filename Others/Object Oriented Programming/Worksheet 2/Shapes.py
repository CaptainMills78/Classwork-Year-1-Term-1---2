class shapes():
    # Constructor
    def __init__(self, FillC, OutC, OutT):
        self.fillColour = FillC
        self.outlineColour = OutC
        self.outlineThickness = OutT

    # Methods

    def rotate(self, angle):
        print("Rotated by "+angle)

    def copy(self):
        print("Copied")

    def enlarge(self, percentage):
        print("Enlarged by "+ percentage + "%")


class circle(shapes):
    # Constructor
    def __init__(self, FillC, OutC, OutT, rad, cent):
        self.radius = rad
        self.centre = cent
        super().__init__(FillC, OutC, OutT)

    def changeOutlineColour(self, new):
        self.outlineColour = new


class rectangle(shapes):
    def __init__(self, FillC, OutC, OutT, Len, wid):
        self.length = Len
        self.width = wid
        super().__init__(FillC, OutC, OutT)

    def addText(self, text):
        print(text)


circle_1 = circle("green", "red", 10, 3, (0,0))
circle_2 = circle("blue", "pink", 4, 5, (0,5))
rectangle_1 = rectangle("green", "yellow", 6, 5, 3)
rectangle_2 = rectangle("brown", "blue", 3, 10, 5)
