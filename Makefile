SOURCES := $(shell find . -name '*.py')

configure:
	pip install pyinstaller

clean:
	rm -rf build dist version.spec

build: SOURCES
	pyinstaller main.spec

install:
	cp dist/version /usr/local/bin

uninstall:
	rm -rf /usr/local/bin/version

.PHONY: SOURCES