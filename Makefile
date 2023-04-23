ifeq ($(OS),Windows_NT)
    PYTHON := python
    EXECUTABLE := passgen.exe
else
    PYTHON := python3
    EXECUTABLE := passgen
endif


c: 
	@$(PYTHON) Main.py c
	@gcc "temp/passgen.c" -lssl -lcrypto -o "build/passgen"

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

ruby:
	@$(PYTHON) Main.py ruby

tcl:
	@$(PYTHON) Main.py tcl

all: c python bash swift dart java powershell php ruby tcl