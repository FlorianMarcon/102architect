"""/*
** EPITECH PROJECT, 2017
** my.h
** File description:
**
*/"""

import sys
import need
from math import *
from need import *

def	base():
	size = len(sys.argv)
	i = 0
	while i < size:
		i = i + operation.search_operation(i)
		i = i + 1

def main():
	base()
	operation.arrondi()
	operation.display_matrice()
	rename_point.new_point()
	return (0)

main()
