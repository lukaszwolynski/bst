from scipy.io import wavfile
import numpy as np
from random import randint

def decimalToBinary(n):
    n = bin(n).replace("0b", "")
    if len(n) != 16:
        n = (16-len(n))*"0" + n
    if "-" in n:
        n = n.replace("-", "")
        n = "-" + n
    return n

def calculateXor(bit1, bit2, bit3):
    bit1 = True if bit1 == "1" else False
    bit2 = True if bit2 == "1" else False
    bit3 = True if bit3 == "1" else False
    return bit1 ^ bit2 ^ bit3

def generateRandom():
    samplerate, data = wavfile.read('sample.wav')
    channel = data[:, 0]
    combinedBits = []
    S = []

    for byte in channel:
        bits = decimalToBinary(byte)
        combinedBits.append(True & calculateXor(
            bits[-1], bits[-2], bits[-3]))  # returns bool
        if (len(combinedBits) == 8):
            combinedBits = np.array(combinedBits)
            S.append(np.packbits(combinedBits))
            combinedBits = []   

    firstRandomNumber, secondRandomNumber = (
        int(S[randint(0, len(S))]), int(S[randint(0, len(S))]))
    
    return firstRandomNumber, secondRandomNumber
