#!/bin/bash
# Script to calculate simple interest

# Formula: (P * T * R) / 100
# P = Principal, T = Time, R = Rate

echo "Enter Principal:"
read P
echo "Enter Time (in years):"
read T
echo "Enter Rate of Interest:"
read R

SI=$((P * T * R / 100))

echo "Simple Interest = $SI"

