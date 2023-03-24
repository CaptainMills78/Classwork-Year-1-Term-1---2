def encode(input_string):
    count = 1
    prev = ""
    lst = []
    for char in input_string:
        if char != prev:
            entry = (prev, count)
            lst.append(entry)
            count = 1
            prev = char
        else:
            count += 1
    else:
        try:
            entry = (char, count)
            lst.append(entry)
            return (lst, 0)
        except Exception as e:
            print("Exception encountered (e)".format(e=e))
            return (e, 1)

def decode(lst):
    q = ""
    for char, count in lst:
        q += char*count
    return q


if __name__ == "__main__":
    image = []
    line_num = int(input("How many lines are there in your image?"))
    line_width = int(input("How many bits per line?"))
    for x in range(line_num):
        line = ""
        while len(line) != line_width:
            line = input("Enter the line ")
            if len(line) != line_width:
                print("Incorrect width, reenter the line ")
        image.append(line)
    for x in image:
        plain = ""
        for y in x:
            plain += y
        value = encode(plain)
        if value[1] == 0:
            orig = decode(value[0])
            if len(orig) > len(str(value)):
                print("Compressed line is shorter")
                print(value[0])
            else:
                print("Original line is shorter")
                print(orig)
                print(value[0])