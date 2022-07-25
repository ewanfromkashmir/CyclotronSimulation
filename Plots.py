import numpy as np 
import math
import copy
import random
import statistics
from matplotlib import pyplot as plt
from Particle import Particle, ChargedParticle
from ElectromagneticField import GeneralEMField, EMField


''' Importing data obtained from System program, in the form of a list.'''

DataIn = np.load("C:\\Users\\ewanh\\Phys389\\phys389-2021-project-ewanhughes26\\Data.npy", allow_pickle = True)


''' Creating empty lists to store data later on.'''

time = []
xpositions = []
ypositions = []
xvelocity = []
yvelocity = []
kineticenergies = []
totalxmomenta = []
totalymomenta = []
totallinearmomenta = []
varxpos = []
varypos = []
sdxpos = []
sdypos = []
iqrxpos = []
iqrypos = []


''' Loop to add spaces for data in the above lists.'''

for i in range(len(DataIn[0][1])):
    xpositions.append([])
    ypositions.append([])
    xvelocity.append([])
    yvelocity.append([])


''' Loop to calculate x and y positions of all the protons as a function of time.'''

for i in range(len(DataIn)):
    for j in range(len(DataIn[0][1])):
        xpositions[j].append(DataIn[i][1][j].position[0])
        ypositions[j].append(DataIn[i][1][j].position[1])


''' Loop to calculate x and y velocities of all the protons as a function of time.'''

for i in range(len(DataIn)):
    for j in range(len(DataIn[0][1])):
        xvelocity[j].append(DataIn[i][1][j].velocity[0])
        yvelocity[j].append(DataIn[i][1][j].velocity[1])


''' Loop to calculate the total linear momentum and total kinetic energy of the system as a function of time.'''

for i in range(len(DataIn)):
    tempmomentum = np.array([0,0,0], dtype = float)
    tempke = 0.
    for proton in DataIn[i][1]:
        tempmomentum += proton.Momentum()
        tempke += proton.KineticEnergy()
    time.append(DataIn[i][0])
    totallinearmomenta.append(np.linalg.norm(tempmomentum))
    kineticenergies.append(tempke)


''' Functions to calculate mean, standard deviation, variance and interquartile range from a list.'''

def Mean(list):
    return statistics.mean(list)

def StandardDeviation(list):
    return statistics.stdev(list)

def Variance(list):
    return statistics.variance(list)

def InterquartileRange(list):
    return np.percentile(list, 75) - np.percentile(list, 25)


''' Creating an empty list.'''

templist = []

''' Loop to populate the empty list with data of the standard deviation of the x-positions of protons against time.'''

for item in DataIn:
    xpostemp = []
    for particle in item[1]:
        temppos = particle.position[0]
        xpostemp.append(temppos)
    templist.append([item[0], StandardDeviation(xpostemp)])

''' Loop to plot the standard deviation of the x-positions of protons against time.'''
        
a = []
b = []

for i in range(len(templist)):
    a.append(templist[i][0])
    b.append(templist[i][1])
plt.plot(a, b, color = 'red')
plt.xlabel("Time (s)")
plt.ylabel("Standard Deviation in $x$-Position (m)")
plt.show()


''' Emptying the list.'''    

templist = []

''' Loop to calculate the standard deviation of the y-positions of protons against time.'''

for item in DataIn:
    ypostemp = []
    for particle in item[1]:
        temppos = particle.position[1]
        ypostemp.append(temppos)
    templist.append([item[0], StandardDeviation(ypostemp)])

''' Loop to plot the standard deviation of the y-positions of protons against time.'''
        
a = []
b = []

for i in range(len(templist)):
    a.append(templist[i][0])
    b.append(templist[i][1])
plt.plot(a, b, color = 'red')
plt.xlabel("Time (s)")
plt.ylabel("Standard Deviation in $y$-Position (m)")
plt.show()


''' Emptying the list.'''

templist = []

''' Loop to calculate the variance of the x-positions of the protons as a function of time.'''

for item in DataIn:
    xpostemp = []
    for particle in item[1]:
        temppos = particle.position[0]
        xpostemp.append(temppos)
    templist.append([item[0], Variance(xpostemp)])

''' Loop to plot the variance of the x-positions of the protons as a function of time.'''
        
a = []
b = []

for i in range(len(templist)):
    a.append(templist[i][0])
    b.append(templist[i][1])
plt.plot(a, b, color = 'blue')
plt.xlabel("Time (s)")
plt.ylabel("Variance in $x$-Position (m$^2$)")
plt.show()

''' Empyting the list.'''    

templist = []

''' Loop to calculate the variance of the y-positions of the protons as a function of time.'''

for item in DataIn:
    ypostemp = []
    for particle in item[1]:
        temppos = particle.position[1]
        ypostemp.append(temppos)
    templist.append([item[0], Variance(ypostemp)])

''' Loop to plot the variance of the y-positions of the protons as a function of time.'''
        
a = []
b = []

for i in range(len(templist)):
    a.append(templist[i][0])
    b.append(templist[i][1])
plt.plot(a, b, color = 'blue')
plt.xlabel("Time (s)")
plt.ylabel("Variance in $y$-Position (m$^2$)")
plt.show()


''' Emptying the list.'''

templist = []

''' Loop to calculate the interquartile range of the x-positions of the protons as a function of time.'''

for item in DataIn:
    xpostemp = []
    for particle in item[1]:
        temppos = particle.position[0]
        xpostemp.append(temppos)
    templist.append([item[0], InterquartileRange(xpostemp)])

''' Loop to plot the interquartile range of the x-positions of the protons as a function of time.'''
        
a = []
b = []

for i in range(len(templist)):
    a.append(templist[i][0])
    b.append(templist[i][1])
plt.plot(a, b, color = 'green')
plt.xlabel("Time (s)")
plt.ylabel("Interquartile Range in $x$-Position (m)")
plt.show()

''' Emptying the list.'''    

templist = []

''' Loop to calculate the interquartile range of the y-positions of the protons as a function of time.'''

for item in DataIn:
    ypostemp = []
    for particle in item[1]:
        temppos = particle.position[1]
        ypostemp.append(temppos)
    templist.append([item[0], InterquartileRange(ypostemp)])

''' Loop to plot the interquartile range of the y-positions of the protons as a function of time.'''
        
a = []
b = []

for i in range(len(templist)):
    a.append(templist[i][0])
    b.append(templist[i][1])
plt.plot(a, b, color = 'green')
plt.xlabel("Time (s)")
plt.ylabel("Interquartile Range in $y$-Position (m)")
plt.show()


''' Plotting a two-dimensional diagram of the x, y positions of all protons.'''

for j in range(len(DataIn[0][1])):                                                                         
    plt.plot(xpositions[j], ypositions[j])
plt.xlabel("$x$ position of proton $\mathrm{(m)}$")
plt.ylabel("$y$ position of proton $\mathrm{(m)}$")
plt.legend
plt.show()