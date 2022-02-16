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
        print("     Warning: Turbidity is above threshold for safe use ")
        avgturb = 1.1992
        calculate_minimum_time()
    if (avgturb < 1):
        print ("     Turbidity is safe for use. \n" )

def calculate_minimum_time():
    hour = 0
    hour  = math.log((1/avgturb),0.98)
    print ("     Minimum time required to return below a safe threshold = ",hour, "\n")

def main():

    with open('turbidity_data.json', 'r') as f:
        datavec = json.load(f)

    calculate_turbidity(datavec['turbidity_data'])


if __name__ == '__main__':
    main()
