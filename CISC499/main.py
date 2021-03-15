from formatt import *
from builder import build as dr


def main(filename):
	s,t = format_svg(filename)
	dr(s,t)
   
def mainSides(length, width, height, thickness):
	s,t = input_2_sides(length, width, height, thickness)
	dr(s,t)
