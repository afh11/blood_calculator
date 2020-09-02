def return_y(x1, y1, x2, y2, x3):
    Slope = (y2-y1) / (x2-x1)
    B = y1 - (Slope * x1)
    y4 = (Slope * x3) + B
    return y4
