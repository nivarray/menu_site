#!/bin/bash
apt-get update
apt-get install -y \
	libgirepository1.0-dev \
	gobject-introspection \
	pkg-config \
	meson \
	build-essential \
	python3-dev
pip install -r requirements.txt
