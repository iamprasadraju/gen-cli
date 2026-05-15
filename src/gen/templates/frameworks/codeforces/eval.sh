#!/bin/bash

clang++ main.cpp
cat in.txt | ./a.out | diff - out.txt
