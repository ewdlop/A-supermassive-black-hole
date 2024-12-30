import math

def calculate_schwarzschild_radius(mass):
    """
    Calculate the Schwarzschild radius of a black hole.
    
    Parameters:
    mass (float): Mass of the black hole in kilograms.
    
    Returns:
    float: Schwarzschild radius in meters.
    """
    G = 6.67430e-11  # gravitational constant in m^3 kg^-1 s^-2
    c = 299792458  # speed of light in m/s
    return 2 * G * mass / c**2

def calculate_event_horizon(mass):
    """
    Calculate the event horizon of a black hole.
    
    Parameters:
    mass (float): Mass of the black hole in kilograms.
    
    Returns:
    float: Event horizon in meters.
    """
    return calculate_schwarzschild_radius(mass)

def calculate_hawking_radiation(mass):
    """
    Calculate the Hawking radiation of a black hole.
    
    Parameters:
    mass (float): Mass of the black hole in kilograms.
    
    Returns:
    float: Hawking radiation in watts.
    """
    h_bar = 1.054571817e-34  # reduced Planck constant in m^2 kg / s
    G = 6.67430e-11  # gravitational constant in m^3 kg^-1 s^-2
    c = 299792458  # speed of light in m/s
    k_B = 1.380649e-23  # Boltzmann constant in J/K
    return (h_bar * c**6) / (15360 * math.pi * G**2 * mass**2 * k_B)
