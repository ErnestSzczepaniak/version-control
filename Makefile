SOURCES := $(shell find . -name '*.py')

configure:
	pip install pyinstaller

clean:
	rm -rf build dist version.spec

build: SOURCES
	python3 -m PyInstaller main.py --onefile --name version

install:
	cp dist/version /usr/local/bin

uninstall:
	rm -rf /usr/local/bin/version

.PHONY: SOURCES