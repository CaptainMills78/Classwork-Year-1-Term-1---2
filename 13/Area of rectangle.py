def calc_area(width, height):

    # Calculate area - store
    a = width * height
    # return area
    return a


# Main code
# Enter width of rectangle - store
w = int(input("Please enter width:"))
# Enter height - store
h = int(input("Please enter height:"))
area = calc_area(w, h)
print("Area is: "+str(area))
