SOURCES := $(shell find . -name '*.py')
SHELL := /bin/bash

configure:
	apt install python3-pip
	pip install pyinstaller

build: SOURCES
	rm -rf build dist version.spec
	python3 -m PyInstaller main.py --onefile --name version

install:
	cp dist/version /usr/local/bin
	cp version-completion /etc/bash_completion.d/

uninstall:
	rm -rf /usr/local/bin/version

.PHONY: SOURCES

