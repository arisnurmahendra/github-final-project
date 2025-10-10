#!/bin/bash

# Simple Interest Calculator Script

echo "Simple Interest Calculator"
echo "--------------------------"

# Read input from user
read -p "Enter Principal amount: " principal
read -p "Enter Rate of interest: " rate
read -p "Enter Time (in years): " time

# Calculate Simple Interest
interest=$(echo "scale=2; ($principal * $rate * $time) / 100" | bc)

# Output the result
echo "Simple Interest is: $interest"
