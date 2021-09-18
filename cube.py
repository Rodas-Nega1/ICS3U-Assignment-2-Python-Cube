#!/usr/bin/env python3

# Created by: Rodas Nega
# Created on: Sep 2021
# This program calculates the surface and area of a cube
#    with side length inputted from the user


def main():
    # this function calculates the surface area and volume of a cube

    # input
    side_length = int(input("Enter the side length of your cube (cm): "))

    # process
    surface_area = 6 * side_length ** 2
    volume = side_length ** 3

    # output
    print("")
    print("The surface area of the cube is {0} cm².".format(surface_area))
    print("The volume of the cube is {0} cm³.".format(volume))
    print("\nDone.")


if __name__ == "__main__":
    main()
