import pytest
import statistics
import copy
import random
import numpy as np
import math
from Particle import Particle, ChargedParticle
from ElectromagneticField import GeneralEMField, EMField


''' Functions to calculate mean, standard deviation, variance and interquartile range from a list.
    These are duplicated here as to avoid importing the entirety of the Plots program.'''

def Mean(list):
    return statistics.mean(list)

def StandardDeviation(list):
    return statistics.stdev(list)

def Variance(list):
    return statistics.variance(list)

def InterquartileRange(list):
    return np.percentile(list, 75) - np.percentile(list, 25)


''' Defining variables a to d as random integers between 1 and 10.'''

a = 1.0*random.randrange(1,10)
b = 1.0*random.randrange(1,10)
c = 1.0*random.randrange(1,10)
d = 1.0*random.randrange(1,10)
e = 1.0*random.randrange(1,10)
f = 1.0*random.randrange(1,10)


''' Creating two testparticles as iterations of the ChargedParticle class.
    One uses the random integers above for its position and velocity components, while the other uses the same integers each time.'''

testparticle = ChargedParticle(np.array([a,b,c]), np.array([d,e,f]), np.array([0,0,0]), Mass=1, Charge=1)
testparticlereal = ChargedParticle(np.array([2, -2, 1]), np.array([0, 5, -3]), Mass=2, Charge=-1)


''' Creating a list of the above randomly-generated integers, and a list of specific integers between 1 and 10.'''

testlist = [a, b, c, d, e, f]
testlistreal = [7, 6, 2, 9, 10, 8, 1, 1, 3, 8]


''' Creating test functions for the various functions included in the system.'''

def test_KineticEnergy1():
    assert testparticle.KineticEnergy == 0.5*(d*d + e*e + f*f)

def test_KineticEnergy2():
    assert testparticlereal.KineticEnergy > 5.83094 and testparticlereal.KineticEnergy < 5.83096

def test_Momentum1():
    assert testparticle.Momentum == np.array([d, e, f])

def test_Momentum2():
    assert testparticlereal.Momentum == np.array([0, 10, -6], dtype = float)
    
def test_Mean():
    assert Mean(testlistreal) > 5.499 and Mean(testlistreal) < 5.501
    
def test_StandardDeviation():
    assert StandardDeviation(testlistreal) > 3.26342 and StandardDeviation(testlistreal) < 3.26344 

def test_Variance():
    assert Variance(testlistreal) > 10.649 and Variance(testlistreal) < 10.651

def test_InterquartileRange():
    assert InterquartileRange(testlistreal) > 6.49 and InterquartileRange(testlistreal) < 6.51
    

    
    
    
