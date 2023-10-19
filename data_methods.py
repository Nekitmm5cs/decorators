from decorators import collect_data


@collect_data("dealership.txt")
def data_methods(brand, model, year, engine, hp, color):
    car_info = f"Brand: {brand} \nModel: {model} \nYear: {year} \nEngine: {engine} \nHorsepower: {hp} \nColor: {color}"
    return car_info

