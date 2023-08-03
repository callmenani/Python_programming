import math
def paint_calc(height,width,cover):
    area = math.ceil((height*width)/cover)
    print(f"The Total Cans of Paint needed : {area}")



test_h = float(input("Height of wall: "))
test_w = float(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)