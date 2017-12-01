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
	plan_base = [1, 0, 0, 0, 1, 0, 0, 0, 1]
	new_plan = [1, 0, 0, 0, 1, 0, 0, 0, 1]


class balise():
	flag = ["-t", "-h", "-r", "-s"]

class operation():
	def egalite():
		archi.plan[0] = archi.new_plan[0]
		archi.plan[1] = archi.new_plan[1]
		archi.plan[2] = archi.new_plan[2]
		archi.plan[3] = archi.new_plan[3]
		archi.plan[4] = archi.new_plan[4]
		archi.plan[5] = archi.new_plan[5]
		archi.plan[6] = archi.new_plan[6]
		archi.plan[7] = archi.new_plan[7]
		archi.plan[8] = archi.new_plan[8]
	def multi_matri(matr):
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
		operation.egalite()
	def symetrie(i):
		angle = float(sys.argv[i + 1])
		angle = radians(angle)
		tab = [1, 0, 0, 0, 1, 0, 0, 0, 1]
		tab[0] =  pow(cos(angle), 2) - pow(sin(angle), 2)
		tab[1] = 2 * cos(angle) * sin(angle)
		tab[3] = 2 * cos(angle) * sin(angle)
		tab[4] = pow(sin(angle), 2) - pow(cos(angle), 2)
		operation.multi_matri(tab)
		print ("Symmetry about an axis inclined with an angle of ", end = '')
		print(sys.argv[i + 1], "degrees")
	def rotation(i):
		angle = int(sys.argv[i + 1])
		angle = radians(angle)
		cos_ang = cos(angle)
		sin_ang = sin(angle)
		angle = [cos_ang, -sin_ang, 0, sin_ang, cos_ang, 0, 0, 0, 1]
		operation.multi_matri(angle)
		print("Rotation at a", sys.argv[i + 1], "degree angle")
	def homothety(i):
		var = 0
		homo = [0, 0, 0, 0, 0, 0, 0, 0, 1]
		homo[0] = float(sys.argv[i + 1])
		homo[4] = float(sys.argv[i + 2])
		operation.multi_matri(homo)
		operation.egalite()
		print("Homothety by the ratios", sys.argv[i + 1], "and", sys.argv[i + 2])
	def translation(i):
		sentence = "Translation by the vector ("
		transla = [1, 0, 0, 0, 1, 0, 0, 0, 1]
		transla[2] = float(sys.argv[i + 1])
		transla[5] = float(sys.argv[i + 2])
		operation.multi_matri(transla)
		operation.egalite()
		print(sentence, end = '')
		print (sys.argv[i + 1], end = '')
		print(", ", end = '')
		print (sys.argv[i + 2], end = '')
		print (")")
	def	search_operation(i):
		if sys.argv[i] == balise.flag[0]:
			operation.translation(i)
			return (2)
		if sys.argv[i] == balise.flag[1]:
			operation.homothety(i)
			return (2)
		if sys.argv[i] == balise.flag[2]:
			operation.rotation(i)
			return (1)
		if sys.argv[i] == balise.flag[3]:
			operation.symetrie(i)
			return (1)
		return (0)
	def arrondi():
		i = 0
		while i < 9:
			archi.new_plan[i] = round(archi.plan[i], 2)
			i = i + 1

class rename_point():
	def multi_newpoint(point):
		new_point = [0, 0, 0]
		x = 0
		y = 0
		while y < 3:
			somme = archi.plan[y * 3 + 0] * point[0]
			somme = somme + archi.plan[y * 3 + 1] * point[1]
			somme = somme + archi.plan[y * 3 + 2] * point[2]
			new_point[y] = float(round(somme, 2))
			y = y + 1
		return (new_point)
	def new_point():
		i = 0
		point = archi.point
		print ('(', end = '')
		print (sys.argv[1], end = '')
		print(",", end = '')
		print(sys.argv[2], end = '')
		print(") => (",end = '')
		point = rename_point.multi_newpoint(point)
		while i < 3:
			point[i] = round(point[i], 2)
			i = i + 1
		print ("%.2f" % point[0], end = '')
		print (",", end = '')
		print("%.2f" % point[1], end = '')
		print (")")

class displaying():
	def display_matrice():
		print("%.2f" % archi.new_plan[0],"	", end = '')
		print("%.2f" % archi.new_plan[1], "	", end = '')
		print("%.2f" % archi.new_plan[2])
		print("%.2f" % archi.new_plan[3], "	", end = '')
		print("%.2f" % archi.new_plan[4], "	", end = '')
		print("%.2f" % archi.new_plan[5])
		print("%.2f" % archi.new_plan[6], "	", end = '')
		print("%.2f" % archi.new_plan[7], "	", end = '')
		print("%.2f" % archi.new_plan[8])
	def display():
		i = 0
		while i < 9:
			if archi.new_plan[i] == 0:
				archi.new_plan[i] = 0
			i = i + 1
		displaying.display_matrice()
