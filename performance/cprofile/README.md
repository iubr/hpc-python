## Using cProfile

In this exercise we analyze the performance of heat equation solver with cProfile.

The file [heat_main.py](heat_main.py) contains the (very inefficient)
implementation of the two dimensional heat equation. Use `cProfile` for
investigating where the time is spent in the program. Note that the execution 
time can be between 40 - 60 s depending on your hardware. (You can see also 
results of the simulation in the *heat_nnn.png* output files). 

Using cProfile, personal Notes:
1. Run the profiel and save results in "profile_results.dat"
$ python3 -m cProfile -o profile_results.dat heat_main.py 

2. Analyze results:
$ python3 -m pstats profile_results.dat
	Commands: 
		help
			stats
		stats 
		strip
		sort [keys]
			keys = time, calls, ...
