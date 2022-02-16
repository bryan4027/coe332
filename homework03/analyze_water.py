import json
import math

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
    print("\n     Avg Turbidity: ",avgturb)
    
    if (avgturb >= 1):
        print("     Warning: Turbidity is above threshold for safe use \n")
    if (avgturb < 1):
        print ("     Turbidity is safe for use. \n")

#def caclulate_minimum_time():


with open('turbidity_data.json', 'r') as f:
    datavec = json.load(f)

calculate_turbidity(datavec['turbidity_data'])




#def main():




#if __name__ == '__main__':
 #   main()
