import sys
if len(sys.argv) == 2:
    script_name = sys.argv[0]
    salary = float(sys.argv[1])
    print("User provided salary:")
else:
    script_name = sys.argv[0]
    salary = 50000.0  # default salary
    print("No input given - using default salary:")
