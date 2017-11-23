"""/*
** EPITECH PROJECT, 2017
** my.h
** File description:
**
*/"""

import sys
from math import *

class archi():
	point = [float(sys.argv[1]), float(sys.argv[2]), 1]
	plan = [1, 0, 0, 0, 1, 0, 0, 0, 1]
	new_plan = [1, 0, 0, 0, 1, 0, 0, 0, 1]

class balise():
	flag = ["-t", "-h", "-r"]

class operation():
	def multi_matri2(matr):
		x = 0
		y = 0
		var = 0
		somme = 0
		while x < 3:
			y = 0
			while y < 3:
				somme = matr[y * 3 + 0] * archi.plan[0 * 3 + x]
				somme = somme + (matr[y * 3 + 1] * archi.plan[1 * 3 + x])
				somme = somme + (matr[y * 3 + 2] * archi.plan[2 * 3 + x])
				archi.new_plan[y * 3 + x] = somme
				y = y + 1
				x = x + 1
				archi.plan = archi.new_plan
	def rotation(i):
		angle = int(sys.argv[i + 1])
		angle = radians(angle)
		cos_ang = round(cos(angle), 3)
		sin_ang = round(sin(angle), 3)
		angle = [cos_ang, -sin_ang, 0, sin_ang, cos_ang, 0, 0, 0, 1]
		operation.multi_matri2(angle)
		print("Rotation at a", sys.argv[i + 1], "degrees angle")
	def homothety(i):
		homo = [sys.argv[i + 1], sys.argv[i + 2], 1]
		archi.new_plan[0] = archi.plan[0] * int(homo[0])
		archi.new_plan[4] = archi.plan[4] * int(homo[1])
		archi.new_plan[8] = archi.plan[8] * int(homo[2])
		archi.plan = archi.new_plan
		print("Homothety by the ratios", sys.argv[i + 1], "and", sys.argv[i + 2])
	def translation(i):
		sentence = "Translation by the vector ("
		transla = [sys.argv[i + 1], sys.argv[i + 2], 0]
		archi.new_plan[0] = float(archi.plan[0]) + float(transla[0])
		archi.new_plan[4] = float(archi.plan[4]) + float(transla[1])
		archi.new_plan[8] = float(archi.plan[8]) + float(transla[2])
		archi.plan = archi.new_plan
		print(sentence, end = '')
		print (transla[0], end = '')
		print(",", end = '')
		print (transla[1], end = '')
		print (")")
	def display_matrice():
		print(archi.new_plan[0],"	", archi.new_plan[1], "	", archi.new_plan[2])
		print(archi.new_plan[3], "	", archi.new_plan[4], "	", archi.new_plan[5])
		print(archi.new_plan[6], "	", archi.new_plan[7], "	",archi.new_plan[8])
	def	search_operation(i):
		if sys.argv[i] == balise.flag[0]:
			operation.translation(i)
			return (2)
		if sys.argv[i] == balise.flag[1]:
			operation.homothety(i)
			return(2)
		if sys.argv[i] == balise.flag[2]:
			operation.rotation(i)
			return(1)
		return (0)
	def arrondi():
		i = 0
		while i < 9:
			archi.plan[i] = round(archi.plan[i], 2)
			i = i + 1

class rename_point():
	def multi_newpoint(point):
		x = 0
		y = 0
		while y < 3:
			point[y] = float(point[y]) * (archi.plan[x] + archi.plan[x + 1] + archi.plan[x + 2])
			y = y + 1
			x = x + 3
			return (point)
	def new_point():
		i = 0
		point = archi.point
		print ('(', end = '')
		print (point[0], end = '')
		print(",", end = '')
		print(point[1], end = '')
		print(") => (",end = '')
		point = rename_point.multi_newpoint(point)
		while i < 3:
			point[i] = round(point[i], 2)
			i = i + 1
		print (point[0], end = '')
		print (",", end = '')
		print(point[1], end = '')
		print (")")
