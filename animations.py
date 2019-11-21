
def anim_slowWipe(strip, color, wait_ms):
    for x in range(LED_COLS):
        for y in range(LED_ROWS):
            setPX(strip,x,y,color)
            push(strip)
            time.sleep(wait_ms/1000.0)

def anim_biFlash(strip, color1, color2, numLoops, wait_ms):
    for i in range(numLoops):
        for x in range(LED_COLS):
            for y in range(LED_ROWS):
                if ((x+y+i)%2==0):
                    setPX(strip,x,y,color1)
                else:
                    setPX(strip,x,y,color2)
        push(strip)
        time.sleep(wait_ms/1000.0)

def anim_pulseInterp(strip, color1, color2, numLoops, loopTime):
    pi = 3.14159
    pos = 0
    pos2 = -pi/2.0
    numSteps=1000.0
    numSteps1=1000
    diff = pi/numSteps
    for i in range(numLoops):
        for j in range (numSteps1):
            print("-")
            bri1 = math.sin(pos) * math.sin(pos)
            bri2 = 1.0-(math.sin(pos) * math.sin(pos))
            print(bri1)
            print(bri2)
            col1 = bri1*color1
            col2 = bri2*color2
            print(col1)
            print(col2)
            combinedColor = int(col1+col2)
            print(combinedColor)
            wipe(strip, combinedColor)
            pos+=diff
            pos2+=diff
            time.sleep(1000.0/1000.0)

def anim_pulse(strip, color, numLoops, loopTime):
    anim_pulseInterp(strip, Color(0,0,0), color,numLoops, loopTime)
