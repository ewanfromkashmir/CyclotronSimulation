import numpy as np
import math
import copy
import scipy.constants
import random


class Particle:

    ''' Class to model a particle and its motion, using numpy arrays.'''

    ''' Importing constants from scipy.'''

    gravconstant = scipy.constants.G                         
    elementcharge = scipy.constants.elementary_charge       
    protonmass = scipy.constants.m_p

    ''' Choosing a method, either 'Euler' or 'EulerCromer'.'''

    Method = 'EulerCromer'     

    ''' Function to initialise Particle class.'''                

    def __init__(self, Position=np.array([0,0,0], dtype=float), Velocity=np.array([0,0,0], dtype=float), Acceleration=np.array([0,-10,0], dtype=float), Name='Ball', Mass=1.0):
        self.Name = Name
        self.position = np.array(Position,dtype=float)
        self.velocity = np.array(Velocity,dtype=float)
        self.acceleration = np.array(Acceleration,dtype=float)
        self.mass = Mass

    def __repr__(self):
        return 'Particle: {0}, Mass: {1:12.3e}, Position: {2}, Velocity: {3}, Acceleration: {4}'.format(self.Name,self.mass,self.position, self.velocity,self.acceleration)

    ''' Function to calculate kinetic energy of a Particle.'''
    
    def KineticEnergy(self):
        return 0.5*self.mass*np.vdot(self.velocity,self.velocity)

    ''' Function to calculate linear momentum of a Particle.'''
  
    def Momentum(self):
        return self.mass*np.array(self.velocity,dtype=float)

    ''' Function applying either the Euler or Euler-Cromer method to model the motion of a Particle.'''

    def update(self, deltaT):
        if self.Method == 'EulerCromer':
            self.velocity += deltaT*self.acceleration                                   
            self.position += deltaT*self.velocity
        elif self.Method == 'Euler':    
            self.position += deltaT*self.velocity
            self.velocity += deltaT*self.acceleration
        else: 
            raise ValueError('Please choose either the Euler or Euler-Cromer method in the input above')


class ChargedParticle(Particle):

    ''' Class to model a Charged Particle, extending the Particle class through inheritance and adding charge as a parameter.
        The ChargedParticle class applies a random x and y position, and a random x and y velocity to each charged particle.
        The class also applies the mass and charge of a proton to each charged particle.'''

    ''' Importing constants from scipy.'''

    elementcharge = scipy.constants.elementary_charge       
    massproton = scipy.constants.m_p

    ''' Function to initialise ChargedParticle class. Sets random positions and velocities and adds the charge and mass of a proton.'''

    def __init__(self, Position=np.array( [0.001*random.randrange(0,100), 0.001*random.randrange(0,100),0],dtype =float), Velocity=np.array( [0.001*random.randrange(0,100), 0.001*random.randrange(0,100),0],dtype =float), Acceleration=np.array( [0, -10,0],dtype =float), Name='Proton', Mass=massproton, Charge=elementcharge):
        super().__init__(Position=Position, Velocity=Velocity, Acceleration=Acceleration, Name=Name, Mass=Mass)
        self.charge = Charge

    def __repr__(self):
        return 'Charged Particle: {0}, Mass: {1:12.3e}, Charge: {2:12.3e}, Position: {3}, Velocity: {4}, Acceleration: {5}'.format(self.Name,self.mass,self.charge,self.position, self.velocity,self.acceleration) 


def createprotonbunch(number):

    ''' Function to create a bunch of protons with random x, y positions and velocities. This makes use of the Random module.'''

    ''' Creating an empty list to contain protons.'''

    protonbunch = []

    ''' Importing constants from scipy.'''
    
    elementcharge = scipy.constants.elementary_charge       
    massproton = scipy.constants.m_p

    ''' Loop to add protons with random x, y positions and velocities to the above list.'''

    for i in range(number):
        protonbunch.append(ChargedParticle(Position=np.array( [0.00001*random.randrange(-100,100), 0.00001*random.randrange(-100,100),0],dtype =float), Velocity=np.array( [0.0001*random.randrange(-100,100), 0.0001*random.randrange(-100,100),0],dtype =float), Acceleration=np.array( [0, -10,0],dtype =float), Name='Proton', Mass=massproton, Charge=elementcharge))
    return protonbunch


''' Creating a list consisting of (_) protons, then assigning this list to a variable 'bunch'.'''

bunch = createprotonbunch(20)
