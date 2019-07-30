from time import sleep
from datetime import datetime
from sh import gphoto2 as gp 
import signal, os, subprocess

def killgphoto2process():
    """
    Function resets communication to camera 
    """
    p = subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE)
    out, err = p.communicate ()

    for line in out.splitlines ():
        if b'gvfsd-gphoto2' in line:
            pid = int(line.split(None,1)[0])
            os.kill(pid, signal.SIGKILL)
            
shot_time = datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
filename = 'filename'

triggerCommand = str("--capture-image-and-download --filename " + shot_time)

def captureImages():
    """
    Generate image capture command
    """
    gp(triggerCommand)
    sleep(12)
    
sleep(3)
killgphoto2process()
captureImages()
print ('#####     Copy file name for auto capture     #####')
killgphoto2process()
