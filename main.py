from data_methods import data_methods
from display_methods import display_dealership

def main():
    car_info = data_methods("BMW", "M5 F90", 2022, 4.4, 625, "Black")
    display_dealership(car_info)

if __name__ == "__main__":
    main()
