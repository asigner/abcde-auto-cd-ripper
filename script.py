import subprocess
import time
from multiprocessing import Process
from os import path

# Rip drive to FLAC and MP3 using abcde
def begin_rip(directory):
    drive_loc = '/dev/' + directory.split('=')[-1]

    # Continuous loop to search for newly entered discs
    while True:
        if path.exists(directory): # Checks if an audio disc has been entered
            print('Found disc in drive ', drive_loc)
            subprocess.call(['abcde','-d', drive_loc]) # Run abcde with drive
            print('Finished processing disc in drive ', drive_loc)
        time.sleep(5)

# Create processes to be run simulatenously
# These will scan the directory they are pointed to, which is where the
# audio cd will mount. When the directory exists, the drive at the specified
# location will be run through abcde

# These directories will need to change based on where your cd's mount
d1 = Process(target=begin_rip, args=('/run/user/1000/gvfs/cdda:host=sr0',))
d2 = Process(target=begin_rip, args=('/run/user/1000/gvfs/cdda:host=sr1',))
d3 = Process(target=begin_rip, args=('/run/user/1000/gvfs/cdda:host=sr2',))

d1.start()
d2.start()
d3.start()
