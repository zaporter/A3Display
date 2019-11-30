import time
from basicDisp import * 
# Will later be useful for GIF animations

def sleep_ms(time_ms):
    if (strip.previewMode):
        for i in range (int(time_ms/66.6)):
            push()
    else:
        time.sleep(time_ms/1000.0);
