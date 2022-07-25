import numpy as np 
import math
import copy
import scipy.constants
from Particle import ChargedParticle
from abc import ABC, abstractmethod


''' Class to implement Lorentz's Law using an abstract method, returning an acceleration.
    This is borrowed from the class in the course notes.'''

class GeneralEMField(ABC):

    ''' Function to initialise class, defining electric and magnetic fields as numpy arrays.'''

    @abstractmethod
    def __init__(self, ElectricField = np.array([0,0,0], dtype=float), MagneticField = np.array([0,0,0], dtype=float)):
        self.electric = np.array(ElectricField,dtype=float)
        self.magnetic = np.array(MagneticField, dtype=float)
        super(GeneralEMField, self).__init__()


    def __repr__(self):
        return 'EMField: E = {0}, B = {1}'.format(self.electric,self.magnetic)

    ''' Function to return an acceleration calculated with Lorentz's Law.'''

    def getAcceleration(self, particle, Time=0.0):                                          
        lorentz = np.array(self.electric, dtype=float)                                      
        lorentz+=np.cross(particle.velocity, self.magnetic)                                 
        lorentz *= (particle.charge/particle.mass)                                          
        return lorentz                                                                      


''' Class to allow concrete implementation of the abstract GeneralEMField class.
    This is borrowed from the class in the course notes.'''

class EMField(GeneralEMField):
    
    def __init__(self, ElectricField = np.array([0,0,0], dtype=float), 
                       MagneticField = np.array([0,0,0], dtype=float) ):
        super().__init__(ElectricField,MagneticField)




