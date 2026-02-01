echo "Principal amount enter cheyyandi:"
read principal

echo "Rate of Interest enter cheyyandi:"
read rate

echo "Time period (years) enter cheyyandi:"
read time

simple_interest=$((principal * rate * time / 100))

echo "Simple Interest = $simple_interest"
