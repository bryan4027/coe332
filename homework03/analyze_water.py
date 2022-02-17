import json
import math
import logging
logging.basicConfig(level=logging.DEBUG)
def calculate_turbidity(datavec: list) -> float:
    '''
    This function:
         This function reads in a list of data points recorded real time, takes the last 5 data points and calculates the average Turbidity and returns it

    Args:
         datavec (list): The input is a list of dictionaries with the following values: datetime - a date in the format of a string, sample_volume - a double, calibration_constant - a double, detector_current - a double,  analyzed_by - a string

    Returns:
         this function returns the average turbidity of the last five data points recorded

    '''
    x = -5
    global lastfivedicts
    lastfivedicts = []
    
    for i in range(0,5):
            lastfivedicts.append(datavec[x])
            x = x+1
    avgturb = 0
    for i in range(0,len(lastfivedicts)):
        calibration_const = float(lastfivedicts[i]['calibration_constant'])
        current = float(lastfivedicts[i]['detector_current'])
        avgturb = avgturb + (calibration_const*current)
    avgturb = avgturb/(len(lastfivedicts))
    return avgturb
    

def calculate_minimum_time(avgturb: float) -> float:
    '''
    This function:
         This function reads in the average turbidity of the 5 most recent data points, uses the given equation to calculate the minimum amount of time required, and returns it

    Args:
         avgturb is the average turbidity of the 5 most recent data points. it is always a float.

    Returns:
         this function returns the the amount of time that it takes for the turbidity to get to a safe value. 

    '''
    global hour
    hour = 0
    hour  = math.log((1/avgturb),0.98)
    return (hour)

def printstuff(avgturb: float, time: float) ->None:
    avgturb = 0.86
    print("\n     Avg Turbidity: ",avgturb)
    if (avgturb >= 1):
        logging.warning('Warning: Turbidity is above threshold for safe use ')
        print ("     Minimum time required to return below a safe threshold = ",hour, "\n")
    if (avgturb < 1):
        logging.info ('Turbidity is safe for use. \n' )
    
    
def main():

    with open('turbidity_data.json', 'r') as f:
        datavec = json.load(f)

    turb  = calculate_turbidity(datavec['turbidity_data'])
    time = calculate_minimum_time(turb)
    printstuff(turb, time)


if __name__ == '__main__':
    main()
