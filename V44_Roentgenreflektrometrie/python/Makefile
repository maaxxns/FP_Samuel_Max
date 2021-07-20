all: build/zscan.pdf build/reflek.pdf build/rockingscan.pdf build/Detectorscan.pdf

build/zscan.pdf: Z_Scan.py | build
	TEXINPUTS=$$(pwd)/../..: MATPLOTLIBRC=../../matplotlibrc python Z_Scan.py

build/reflek.pdf: reflek.py | build
	TEXINPUTS=$$(pwd)/../..: MATPLOTLIBRC=../../matplotlibrc python reflek.py

build/rockingscan.pdf: rockingscan.py | build
	TEXINPUTS=$$(pwd)/../..: MATPLOTLIBRC=../../matplotlibrc python rockingscan.py

build/Detectorscan.pdf: Detectorscan.py | build
	TEXINPUTS=$$(pwd)/../..: MATPLOTLIBRC=../../matplotlibrc python Detectorscan.py


build:
	mkdir -p build

clean:
	rm -rf build

.PHONY: all clean