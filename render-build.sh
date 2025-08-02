#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

# Add ffmpeg install command for Debian-based systems
apt-get update && apt-get install -y ffmpeg
