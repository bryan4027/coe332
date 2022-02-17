import json
import math

def calculate_turbidity(datavec: list) -> float:
    x = -5
    global lastfivedicts
    lastfivedicts = []
    for i in range(0,5):
        lastfivedicts.append(datavec[x])
        x = x+1
    avgturb = 0
    for i in range(0,5):
        calibration_const = float(lastfivedicts[i]['calibration_constant'])
        current = float(lastfivedicts[i]['detector_current'])
        avgturb = avgturb + (calibration_const*current)
    avgturb = avgturb/(len(lastfivedicts))
    return avgturb
    

def calculate_minimum_time(avgturb: float) -> float:
    global hour
    hour = 0
    hour  = math.log((1/avgturb),0.98)
    return hour

def printstuff(avgturb: float, time: float) ->None:
    print("\n     Avg Turbidity: ",avgturb)
    if (avgturb >= 1):
        print("     Warning: Turbidity is above threshold for safe use ")
        print ("     Minimum time required to return below a safe threshold = ",hour, "\n")
    if (avgturb < 1):
        print ("     Turbidity is safe for use. \n" )
    
    
def main():

    with open('turbidity_data.json', 'r') as f:
        datavec = json.load(f)

    turb  = calculate_turbidity(datavec['turbidity_data'])
    time = calculate_minimum_time(turb)
    printstuff(turb, time)


if __name__ == '__main__':
    main()
