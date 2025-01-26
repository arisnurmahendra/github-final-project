#!/bin/bash

# Input for principal amount, interest rate, and time
echo "Enter the principal amount (P): "
read P
echo "Enter the annual interest rate (r) as a fraction (e.g., 0.05 for 5%): "
read r
echo "Enter the time in years (t): "
read t

# Calculate simple interest
interest=$(echo "$P * $r * $t" | bc)

# Display the result
echo "The simple interest is: $interest"
