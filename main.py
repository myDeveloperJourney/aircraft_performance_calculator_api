from fastapi import FastAPI, Query
from typing import Optional, List

app = FastAPI()

@app.get("/")
def home():
    return {"Message": "Welcome to the Aircraft Performance Calculator!"}

# Pre-defined variable values
fuel_capacity = 1000  # gallons
fuel_consumption_rate = 50  # gallons per hour
true_air_speed = 150  # knots
payload = 5000  # pounds
fuel_weight = 6000  # pounds
moment_list = [10000, 2500]  # pound-feet
total_weight = 1500  # pounds
cl = 1.5  # lift coefficient
rho = 1.225  # air density in kg/m^3
v = 100  # velocity in m/s
s = 20  # wing area in m^2
cd = 0.02  # drag coefficient
mass = 5000  # mass in kg
g = 9.81  # acceleration due to gravity in m/s^2
thrust = 6000  # thrust in N
drag = 5000  # drag in N
velocity = 50  # initial velocity in m/s
acceleration = 2  # acceleration in m/s^2
time = 10  # time in seconds

def calculate_range(fuel_capacity, fuel_consumption_rate, true_air_speed):
    range_in_hours = fuel_capacity / fuel_consumption_rate
    range_in_miles = range_in_hours * true_air_speed
    return range_in_miles

def calculate_endurance(fuel_capacity, fuel_consumption_rate):
    endurance_in_hours = fuel_capacity / fuel_consumption_rate
    return endurance_in_hours

def calculate_total_weight(payload, fuel_weight):
    return payload + fuel_weight

def calculate_cg_position(moment_list, total_weight):
    total_moment = sum(moment_list)
    return total_moment / total_weight

def calculate_moment(weight, arm):
    return weight * arm

def calculate_lift(cl, rho, v, s):
    return 0.5 * cl * rho * v**2 * s

def calculate_drag(cd, rho, v, s):
    return 0.5 * cd * rho * v**2 * s

def calculate_weight(mass, g):
    return mass * g

def calculate_acceleration(thrust, drag, weight, mass):
    return (thrust - drag - weight) / mass

def calculate_velocity(velocity, acceleration, time):
    return velocity + acceleration * time

def calculate_distance(velocity, time):
    return velocity * time

def pretty_print(range_, endurance, total_weight, cg_position, lift, drag, weight, acceleration, velocity, distance):
    return {
        "title": "Performance Calculations",
        "Range": "{} miles".format(range_),
        "Endurance": "{} hours".format(endurance),
        "Total Weight": "{} pounds".format(total_weight),
        "Center of Gravity Position": "{} feet".format(cg_position),
        "Lift": "{} Newtons".format(lift),
        "Drag": "{} Newtons".format(drag),
        "Weight": "{} Newtons".format(weight),
        "Acceleration": "{} m/s^2".format(acceleration),
        "Velocity": "{} m/s".format(velocity),
        "Distance": "{} meters".format(distance),
    }

@app.get("/calculate")
def calculate(
    fuel_capacity: Optional[float] = 1000, 
    fuel_consumption_rate: Optional[float] = 50, 
    true_air_speed: Optional[float] = 150, 
    payload: Optional[float] = 5000, 
    fuel_weight: Optional[float] = 6000, 
    moment_list: Optional[List[float]] = Query([10000, 2500]), 
    total_weight: Optional[float] = 1500, 
    cl: Optional[float] = 1.5, 
    rho: Optional[float] = 1.225, 
    v: Optional[float] = 100, 
    s: Optional[float] = 20, 
    cd: Optional[float] = 0.02, 
    mass: Optional[float] = 5000, 
    g: Optional[float] = 9.81, 
    thrust: Optional[float] = 6000, 
    drag: Optional[float] = 5000, 
    velocity: Optional[float] = 50, 
    acceleration: Optional[float] = 2, 
    time: Optional[float] = 10):
    
    updated_velocity = calculate_velocity(velocity, acceleration, time)
    
    return pretty_print(
        calculate_range(fuel_capacity, fuel_consumption_rate, true_air_speed), 
        calculate_endurance(fuel_capacity, fuel_consumption_rate), 
        calculate_total_weight(payload, fuel_weight), 
        calculate_cg_position(moment_list, total_weight), 
        calculate_lift(cl, rho, v, s), 
        calculate_drag(cd, rho, v, s), 
        calculate_weight(mass, g), 
        calculate_acceleration(thrust, drag, calculate_weight(mass, g), mass), 
        updated_velocity,
        calculate_distance(updated_velocity, time)
    )
