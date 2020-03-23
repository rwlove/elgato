#!/bin/python

import leglight
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--on", action="store_true", help="Turn the light on")
parser.add_argument("--off", action="store_true", help="Turn the light off")
args = parser.parse_args()

myLight = leglight.LegLight('192.168.5.25', 9123)

if args.on:
    myLight.brightness(5)
    myLight.on()
elif args.off:
    myLight.off()

#myLight.on()
#myLight.brightness(14)
#myLight.color(3500)

