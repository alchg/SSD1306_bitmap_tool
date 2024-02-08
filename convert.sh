#!/bin/bash

if ! command -v ffmpeg &> /dev/null; then
    echo "Error: ffmpeg command not found. Please install ffmpeg."
    exit 1
fi

if ! command -v convert &> /dev/null; then
    echo "Error: convert command not found. Please install ImageMagick."
    exit 1
fi

if ! command -v python &> /dev/null; then
    echo "Error: python command not found. Please install Python."
    exit 1
fi

if [ $# -ne 1 ]; then
    echo "Error: Exactly one file name should be specified."
    exit 1
fi

if [ -e "$1" ]; then
    echo "Specified file name: $1"
else
    echo "Error: The specified file does not exist."
    exit 1
fi

rm work.mp4
ffmpeg -i "$1" -s 128x64 work.mp4

mkdir jpg
rm ./jpg/*

ffmpeg -i work.mp4 -vf "fps=20" ./jpg/%06d.jpg

mkdir bmp
rm ./bmp/*

cd ./jpg/
ls |xargs -I {} convert {} -threshold 50% ../bmp/{}.bmp
cd ../

rm ./txt/*
ls ./bmp/*|xargs -I {} python 2txt.py {}

rm ./rvh/*
ls ./txt/*|xargs -I {} python 2rvh.py {}

rm ./output/*
ls ./rvh/*|xargs -I {} python 2dat.py {}

rm output.dat
cd ./output/
ls | sort | xargs cat > ../output.dat
cd ../

ls -l ./output.dat

echo Finish!!
