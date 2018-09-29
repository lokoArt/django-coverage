import math


def __estimate_consumption_for_airplane(airplane: dict) -> dict:
    fuel_consumption_ratio = 0.8
    passenger_fuel_consumption = 0.002
    airplane_tank_ratio = 200

    fuel_tank = airplane['id'] * airplane_tank_ratio
    fuel_consumption = math.log(airplane['id'], 10) * fuel_consumption_ratio + \
                       passenger_fuel_consumption * airplane['passengers_number']

    maximum_duration = fuel_tank / fuel_consumption
    return {'id': airplane['id'], 'fuel_consumption': fuel_consumption, 'maximum_duration': maximum_duration}


def estimate_consumption_for_airplanes(airplanes: list) -> list:
    return list(map(__estimate_consumption_for_airplane, airplanes))
