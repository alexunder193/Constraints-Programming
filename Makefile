SOURCE = constraints.c
OUT    = constraints
CC     = gcc
FLAGS  = -o


all:
	$(CC)  $(SOURCE)  $(FLAGS) $(OUT)

