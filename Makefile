ifeq ($(OS),Windows_NT)
    PYTHON := python
else
    PYTHON := python3
endif


c: 
	@$(PYTHON) Main.py c
	@gcc "temp/passgen.c" -o "build/passgen.exe"

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
	@javac -d "build" "temp/Passgen.java"

powershell:
	@$(PYTHON) Main.py powershell

php:
	@$(PYTHON) Main.py php

all: c python bash swift dart java powershell