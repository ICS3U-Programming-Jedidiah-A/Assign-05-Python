# !/usr/bin/env python3
# Created By: Jedidiah
# Date: Jan 26, 2021
# This program ask the user for the
# radius of a sphere and display its volume.
import math


def calc_volume(radius):
    volume = (4/3)*math.pi*radius**3
    print("If radius is {} the volume is {}"
          .format(radius, volume))


def main():
    user_radius = input("Enter the radius: ")

    try:
        radius_from_user = float(user_radius)
        if radius_from_user <= 0:
            print("Number must be positive.")
        else:
            calc_volume(radius_from_user)

    except Exception:
        print("Invalid input")


if __name__ == "__main__":
    main()
