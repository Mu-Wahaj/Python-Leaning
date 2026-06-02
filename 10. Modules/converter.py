def lbs_to_kg(weight):
    return weight * 0.45    
def kg_to_lbs(weight):
    return weight / 0.45
def rupees_to_dollars(money):
    return money * 280
def dollars_to_rupees(money):
    return money / 280

def celsius_to_fahrenheit(temp):
    return (temp * 9/5) + 32
def fahrenheit_to_celsius(temp):
    return (temp - 32) * 5/9
def km_to_miles(distance):
    return distance * 0.62
def miles_to_km(distance):
    return distance / 0.62
def cm_to_inches(length):
    return length * 0.39
def inches_to_cm(length):
    return length / 0.39
def feet_to_meters(length):
    return length * 0.30
def meters_to_feet(length):
    return length / 0.30
def liters_to_gallons(volume):
    return volume * 0.26
def gallons_to_liters(volume):
    return volume / 0.26   


#exeercise to find the maximum value in a list using a function from the converter module

def find_max(list):
    max = list[0]
    for i in list:
        if i > max:
            max = i
    return max