## Measuring the time it takes to tun a python code

You can measure small code snippets with timeit
E.g. from command line:
$python3 -m timeit -s "from math import sin" "sin(0.2)"
$python3 -m timeit -n 3 -s "from math import sin" "sin(0.2)"

Or directly inserted in python scripts:
https://docs.python.org/3/library/timeit.html
