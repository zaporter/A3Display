import time
from basicDisp import * 
# Will later be useful for GIF animations

def sleep_ms(strip,time_ms):
    if (strip.previewMode):
        for i in range (int(time_ms/66.6)):
            push(strip)
    else:
        time.sleep(time_ms/1000.0);
