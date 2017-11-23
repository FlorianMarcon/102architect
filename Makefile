##
## EPITECH PROJECT, 2017
## Makefile
## File description:
##
##

cc		=	

RM		=	rm -f

EX		=	

SRC		=	

OBJ		=	$(SRC:.$(EX)=.o)

NAME		=	

CFLAGS		=	-W -Wall -Wextra -Werror -I./include

all:		
	rm -f *.o

clean:
	$(RM) $(OBJ)
	$(RM) *~
	$(RM) *#

fclean: clean
	$(RM) $(NAME)

re:	fclean all
