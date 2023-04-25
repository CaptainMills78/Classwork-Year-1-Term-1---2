class Cars():
    def __init__(self, plateNo, Colour, engineSize):
        self.plate = plateNo
        self.colour = Colour
        self.engine = engineSize
        self.__price = 1000

    def start(self):
        print("Starting car...")

    def stop(self):
        print("Stopping car... ")

    def accelerate(self):
        print("Moving faster... ")

    def set_price(self, newPrice):
        self.__price = newPrice

    def get_price(self):
        return self.__price


class Sports(Cars):
    def __init__(self, plateNo, Colour, engineSize, Diffuser):
        super().__init__(plateNo, Colour, engineSize)
        self.diffuser = Diffuser

    def spin(self):
        print("Spinning!!!! WOOOOOOOO!")


class Convertible(Cars):
    def __init__(self, plateNo, Colour, engineSize, Retractable, Roof):
        super().__init__(plateNo, Colour, engineSize)
        self.retractable = Retractable
        self.roof = Roof

    def retract_roof(self):
        print("Retracting roof... ")


class Estate(Cars):
    def __init__(self, plateNo, Colour, engineSize, boxyRearEnd):
        super().__init__(plateNo, Colour, engineSize)
        self.boxy_rear_end = boxyRearEnd

    def carryLoad(self):
        print("Carrying load... ")


sports = [Sports("DF45 KJH", "Red", "200cc", "Model1"), Sports("MA03 GHM", "Green", "150cc", "Model2")]

convertable = [Convertible("FG56 YNH", "Blue", "150cc", True, "Model1"), Convertible("FE12 ZSD", "Peppermint", "250cc", True, "Model4")]

estate = [Estate("YT78 FVG", "White", "100cc", "Model2"), Estate("HJ45 GBH", "Black", "200cc", "Model3")]

# Good to use lists as easier to organise objects


sports[0].start()
sports[1].stop()
sports[0].accelerate()

convertable[0].retract_roof()
estate[1].carryLoad()

sports[0].set_price(56000)

print(estate[0].get_price())
