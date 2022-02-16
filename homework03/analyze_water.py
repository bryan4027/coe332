import json
import math
import random

#def calculate_turbidity():

#def caclulate_minimum_time():

def calculate_turbidity(datavec):
    x = -5
    global lastfivedicts
    lastfivedicts = []
    for i in range(0,5):
        lastfivedicts.append(datavec[x])
        x = x+1
    global avgturb
    avgturb = 0
    for i in range(0,5):
        calibration_const = float(lastfivedicts[i]['calibration_constant'])
        current = float(lastfivedicts[i]['detector_current'])
        avgturb = avgturb + (calibration_const*current)
    avgturb = avgturb/(len(lastfivedicts))
    print(avgturb)
    return avgturb

with open('turbidity_data.json', 'r') as f:
    datavec = json.load(f)

calculate_turbidity(datavec['turbidity_data'])

for i in lastfivedicts:
    print(i)

#def main():




#if __name__ == '__main__':
 #   main()
