
def main():

    SetSensorColorFull(S3)

    while True:
        sColor = ""
        nColor = Sensor(S3)

        if nColor == 1:
            sColor = "Black"
        elif nColor == 2:
            sColor = "Blue"
        elif nColor == 3:
            sColor = "Green"
        elif nColor == 4:
            sColor = "Yellow"
        elif nColor == 5:
            sColor = "Red"
        elif nColor == 6:
            sColor = "White"
        else:
            sColor = "???"

        lcd_clear()
        TextOut(0, 56, NumToStr(nColor) + ". " + sColor)

        while(Sensor(S3) == nColor):
            pass
