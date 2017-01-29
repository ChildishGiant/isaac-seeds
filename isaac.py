import random

__author__ = 'SolarPolarMan'

# https://twitter.com/solarpolarman
# https://www.youtube.com/solarpolarman
# https://steamcommunity.com/id/solarpolarman
# https://www.reddit.com/user/SolarPolarMan/


def getchecksum(seed):
    checksum = 0
    while True:
        checksum = (checksum + (seed & 0xFF)) & 0xFF
        checksum = (2 * checksum + (checksum >> 7)) & 0xFF
        seed >>= 5
        if seed == 0:
            break
    return checksum


def makeseed():
    seed = random.randint(1, 4294967295)
    checksum = getchecksum(seed)
    abc = "ABCDEFGHJKLMNPQRSTWXYZ01234V6789"
    seedsprev = ((seed ^ 0xFEF7FFD) << 8) | checksum
    finalseed = ""
    for loopindex in range(0, 8):
        finalseed = abc[seedsprev & 0x1F] + finalseed
        seedsprev >>= 5
    return finalseed


print(makeseed())
