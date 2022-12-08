The Particle program contains the Particle class and its subclass ChargedParticle.
In this program one may choose how many protons to generate. 
This program must be ran to generate a bunch of protons, containing the specified amount, with random positions and velocities.

The ElectromagneticField program contains the GeneralEMField class and its subclass EMField. 

The System program contains the main loop which models the motion of protons.
Initital time 'time' can be specified, this works best at 0.
Timestep 'delta' can be specified, around 10 microseconds or below works best.
This program must be ran to produce the data which is then saved to a file 'Data.npy' in the same directory as the program.

The Plots program then imports the data from the file 'Data.npy' and produces a plot of the motion of protons.
This program must be ran to view the results.

TL/DR: run Particle, run System, run Plots.
