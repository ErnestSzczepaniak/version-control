SOURCES := $(shell find . -name '*.py')

configure:
	apt install python3-pip
	pip install pyinstaller

build: SOURCES
	python3 -m PyInstaller main.py --onefile --name version-control

install:
	cp dist/version-control /usr/local/bin
	cp version-control-completion /etc/bash_completion.d
	ln -s /usr/local/bin/version-control /usr/local/bin/vc

uninstall:
	rm -rf /usr/local/bin/version

.PHONY: SOURCES