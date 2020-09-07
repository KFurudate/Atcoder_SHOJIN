n, m = map(int, input().split())

def CalcAngle(hour, min):
    if hour >= 12: hour -= 12
    rShort = (hour * 360/12) + (min * 180/360)
    rLong =  min * (360/60)
    angle = abs(rLong - rShort)
    if angle > 360-angle:
      print(360-angle)
    else:
      print(angle)

CalcAngle(n, m)
