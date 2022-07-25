READ ME BEFORE USE:


The Particle program contains the Particle class and its subclass ChargedParticle.
In this program one may choose how many protons to generate. 
Running this program then generates a bunch of protons, containing the specified amount, with random positions and velocities.

The ElectromagneticField program contains the GeneralEMField class and its subclass EMField. This needn't be run.

The System program contains the main loop which models the motion of protons.
Initital time 'time' can be specified although this is best left at 0.
Timestep 'delta' can be specified, around 10 microseconds or below works best.
This program must be ran to produce the data which is then saved to a file 'Data.npy' in the same directory as the program.

The Plots program then imports the data from the file 'Data.npy' and produces:
-a plot of the motion of the protons

The Test program contains the unit tests for the system's various functions. This can be run.


NOTE:

Unfortunately, the system at present is incomplete, owing to a failure to properly calibrate the initial positions, velocities and the applied magnetic field strength.

With more time, it would have been possible to correct this. However, given the limited extension provided it has not been possible to fix the system and as such it is incomplete.