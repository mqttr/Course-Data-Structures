# Name: Matthew Roland
# NUID: 98210287
# NETID: mroland

import sys
import time

from sorting import *
from datetime import datetime

class TimingValues():
    LASTSEND = time.time()
    FIRSTSEND = time.time()

def log(st: str) -> None:
    currentSend = time.time()
    print(f'{datetime.fromtimestamp(currentSend).strftime('%Y-%m-%d %H:%M:%S'):<20}{currentSend - TimingValues.LASTSEND:<10.3f} TOTAL PROGRAM RUN: {currentSend - TimingValues.FIRSTSEND:<20.3f}{st}')
    TimingValues.LASTSEND = currentSend


if __name__ == "__main__":
    if len(sys.argv) == 1:
        log("Zero Arguments given entering Auto Graphing Mode")