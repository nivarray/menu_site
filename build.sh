#!/bin/bash
apt-get update
apt-get install -y libgirepository1.0-dev gobject-introspection
pip install -r requirements.txt
