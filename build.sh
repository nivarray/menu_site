#!/bin/bash
sudo apt-get update
sudo apt-get install -y \
	libgirepository1.0-dev \
	gobject-introspection \
	pkg-config \
	meson \
	build-essential \
	python3-dev \
	libglib2.0-dev \
	python3-gi \
	python3-gi-cairo \
	libcairo2-dev \
	libpango1.0-dev \
	libffi-dev \
	zlib1g-dev \
&& pip install -r requirements.txt
