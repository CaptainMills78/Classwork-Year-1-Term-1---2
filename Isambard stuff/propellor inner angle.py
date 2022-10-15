def calculateAngle(np):
    angle = 360/np
    return angle


def detail():
    prop = int(input("How many propellers are there?"))
    ang = calculateAngle(prop)
    print("The inner angle of the propeller is: "+str(ang)+" degrees.")
    return


detail()
