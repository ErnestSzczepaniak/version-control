prepare:
	pip install pyinstaller

clean:
	rm -rf build dist version.spec

build:
	pyinstaller --onefile main.py

install: build
	cp dist/version /usr/local/bin

uninstall:
rm -rf /usr/local/bin/version

reinstall: build install

.PHONY: prepare clean build install uninstall reinstall