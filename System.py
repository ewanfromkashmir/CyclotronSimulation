import math
import numpy as np
import statistics
import random
import copy
import pickle
import scipy.constants
from Particle import Particle, ChargedParticle, bunch
from ElectromagneticField import EMField, GeneralEMField

''' Defining parameters such as time, timestep and the applied magnetic field strength.'''

time = 0
delta = 0.0001
AppliedB = 0.00001

''' Creating empty data lists to which data can be added later in the code.'''

Data = []

''' Defining an electric field constant as a variable, based on the requirement for circular motion in a cyclotron.'''

ElectricFieldConstant = ((scipy.constants.elementary_charge)*(AppliedB)*time)/(scipy.constants.m_p)

''' Defining the applied electromagnetic field between the dees as an instance of the EMField class.'''

AppliedFieldGap = EMField(np.array([0,0.1*math.sin(ElectricFieldConstant*time),0]), np.array([0,0,AppliedB]))

''' Defining the applied electromagnetic field outside the dees as an instance of the EMField class.'''

AppliedFieldDees = EMField(np.array([0,0,0]), np.array([0,0,AppliedB]))

''' Double loop to apply the acceleration due to Lorentz's force to the protons.'''

for i in range(3000):

    ''' Loop to return the acceleration calculated with Lorentz's law and set the acceleration of a proton equal to this.
        If the y-coordinate of the proton is between the dees, the field AppliedFieldGap is used.
        If the y-coorindate of the proton is in the dees, the field AppliedFieldDees is used.'''

    for proton in bunch:
        if proton.position[1] >= 0.000005 or proton.position[1] <= -0.000005:
            proton.acceleration = np.array([0,0,0], dtype = float)
            tempacc = AppliedFieldDees.getAcceleration(proton)
            proton.acceleration += tempacc
        else:
            proton.acceleration = np.array([0,0,0], dtype = float)
            tempacc = AppliedFieldGap.getAcceleration(proton)
            proton.acceleration += tempacc

    ''' Loop to update the position and velocity of a proton using Euler/Euler-Cromer and the acceleration due to Lorentz's force.'''

    for proton in bunch:
        proton.update(delta)

    ''' Updating the system time.'''

    time += delta

    ''' Loop to copy the list of protons 'bunch' to a new list data, along with a timestamp, for every 100 iterations of the initial loop.'''

    if i % 2 == 0:
        item = [time, copy.deepcopy(bunch)]
        Data.append(item)

np.save("Data.npy", Data, allow_pickle = True)



