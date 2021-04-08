ifeq ($(OS),Windows_NT)
    PYTHON := python
else
    PYTHON := python3
endif


c: 
	@$(PYTHON) Main.py c
	@gcc "temp/passgen.c" -o "Generators/passgen.exe"

python: 
	@$(PYTHON) Main.py python

bash: 
	@$(PYTHON) Main.py bash

swift: 
	@$(PYTHON) Main.py swift

dart:
	@$(PYTHON) Main.py dart

java:
	@$(PYTHON) Main.py java
	@javac -d "Generators" "temp/Passgen.java"


all: c python bash swift dart java