import math

def freq2midi(freq):
    f_A4 = 440.0
    p = 69.0 + (12.0 * math.log (freq / f_A4)) / (math.log(2))
    return int(p)

m = freq2midi(765.0)
print(m)

