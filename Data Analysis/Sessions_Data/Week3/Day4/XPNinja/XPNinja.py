#XP Ninja - Week 3 Day 4

# The base class Temperature is an abstract class, defining the interface for all temperature types.
# It ensures all subclasses will implement a common set of methods.
from abc import ABC, abstractmethod

class Temperature(ABC):
    """
    A base class for temperature representations.
    
    This abstract class defines the fundamental interface for temperature objects,
    including a value attribute and methods for converting to other temperature
    scales (Celsius, Fahrenheit, and Kelvin).
    """
    
    def __init__(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Temperature value must be a number.")
        self._value = value
    
    @property
    def value(self):
        return self._value
    
    @abstractmethod
    def to_celsius(self):
        pass
    
    @abstractmethod
    def to_fahrenheit(self):
        pass
    
    @abstractmethod
    def to_kelvin(self):
        pass

# --- Concrete Subclasses ---
# These subclasses adhere to the interface defined by the Temperature base class.

class Celsius(Temperature):
    """Represents a temperature in Celsius."""
    
    def to_celsius(self):
        """Converts the temperature to Celsius (returns self)."""
        return self
    
    def to_fahrenheit(self):
        """Converts the temperature to Fahrenheit."""
        return Fahrenheit((self.value * 9/5) + 32)
    
    def to_kelvin(self):
        """Converts the temperature to Kelvin."""
        return Kelvin(self.value + 273.15)
    
    def __repr__(self):
        return f"{self.value}°C"

class Fahrenheit(Temperature):
    """Represents a temperature in Fahrenheit."""

    def to_celsius(self):
        """Converts the temperature to Celsius."""
        return Celsius((self.value - 32) * 5/9)
    
    def to_fahrenheit(self):
        """Converts the temperature to Fahrenheit (returns self)."""
        return self
    
    def to_kelvin(self):
        """Converts the temperature to Kelvin."""
        return Kelvin((self.value - 32) * 5/9 + 273.15)
        
    def __repr__(self):
        return f"{self.value}°F"

class Kelvin(Temperature):
    """Represents a temperature in Kelvin."""
    
    def to_celsius(self):
        """Converts the temperature to Celsius."""
        return Celsius(self.value - 273.15)

    def to_fahrenheit(self):
        """Converts the temperature to Fahrenheit."""
        return Fahrenheit((self.value - 273.15) * 9/5 + 32)
    
    def to_kelvin(self):
        """Converts the temperature to Kelvin (returns self)."""
        return self
        
    def __repr__(self):
        return f"{self.value}K"
        
# --- Example Usage ---
if __name__ == "__main__":
    celsius_temp = Celsius(25)
    print(f"Original temperature: {celsius_temp}")
    
    fahrenheit_from_celsius = celsius_temp.to_fahrenheit()
    print(f"Converted to Fahrenheit: {fahrenheit_from_celsius}")
    
    kelvin_from_celsius = celsius_temp.to_kelvin()
    print(f"Converted to Kelvin: {kelvin_from_celsius}")
    
    print("-" * 20)
    
    fahrenheit_temp = Fahrenheit(77)
    print(f"Original temperature: {fahrenheit_temp}")
    
    celsius_from_fahrenheit = fahrenheit_temp.to_celsius()
    print(f"Converted to Celsius: {celsius_from_fahrenheit}")
    
    kelvin_from_fahrenheit = fahrenheit_temp.to_kelvin()
    print(f"Converted to Kelvin: {kelvin_from_fahrenheit}")
    
    print("-" * 20)
    
    kelvin_temp = Kelvin(298.15)
    print(f"Original temperature: {kelvin_temp}")
    
    celsius_from_kelvin = kelvin_temp.to_celsius()
    print(f"Converted to Celsius: {celsius_from_kelvin}")
    
    fahrenheit_from_kelvin = kelvin_temp.to_fahrenheit()
    print(f"Converted to Fahrenheit: {fahrenheit_from_kelvin}")

    #Exercise 2 - Quantum Particles

    import random

class QuantumParticle:
    """
    Represents a quantum particle with position, momentum, and spin.
    
    Measurements of position or momentum disturb the particle, causing its state
    to change. The particle can also be entangled with another, where a spin 
    measurement on one instantly affects the other.
    """
    
    def __init__(self, position=None, momentum=None, spin=None):
        """
        Initializes the quantum particle. Attributes are randomly generated
        if not provided.
        """
        self.position = position if position is not None else random.randint(1, 10000)
        self.momentum = momentum if momentum is not None else random.random()
        self.spin = spin if spin is not None else random.choice([0.5, -0.5])
        self.entangled_partner = None

    def _disturb(self):
        """
        A private method to simulate quantum disturbance.
        Randomly changes position and momentum and prints a message.
        """
        self.position = random.randint(1, 10000)
        self.momentum = random.random()
        print('Quantum Interferences!!')

    def position_measurement(self):
        """
        Measures the particle's position.
        Causes a disturbance and returns the current position.
        """
        self._disturb()
        return self.position

    def momentum_measurement(self):
        """
        Measures the particle's momentum.
        Causes a disturbance and returns the current momentum.
        """
        self._disturb()
        return self.momentum

    def spin_measurement(self):
        """
        Measures the particle's spin.
        If entangled, sets the partner's spin to the opposite value.
        """
        measured_spin = random.choice([0.5, -0.5])
        self.spin = measured_spin
        
        if self.entangled_partner:
            self.entangled_partner.spin = -measured_spin
            print('Spooky Action at a Distance !!')
            
        return self.spin
    
    def entangle(self, other_particle):
        """
        Entangles this particle with another quantum particle.
        Raises a TypeError if the other object is not a QuantumParticle.
        """
        if not isinstance(other_particle, QuantumParticle):
            raise TypeError("Can only entangle with another QuantumParticle.")
        
        self.entangled_partner = other_particle
        other_particle.entangled_partner = self
        print("Particles are now entangled.")

    def __repr__(self):
        """
        Provides a meaningful string representation of the particle's state.
        """
        return (f"QuantumParticle(position={self.position}, "
                f"momentum={self.momentum:.4f}, spin={self.spin}, "
                f"entangled={bool(self.entangled_partner)})")


# --- Example Usage ---
if __name__ == "__main__":
    print("--- Creating particles ---")
    p1 = QuantumParticle()
    p2 = QuantumParticle()
    
    print(f"Particle 1: {p1}")
    print(f"Particle 2: {p2}")
    
    print("\n--- Measuring Particle 1 (Position & Momentum) ---")
    print(f"Initial position of p1: {p1.position}")
    p1.position_measurement()
    print(f"New position of p1 after measurement: {p1.position}")

    print(f"\nInitial momentum of p1: {p1.momentum}")
    p1.momentum_measurement()
    print(f"New momentum of p1 after measurement: {p1.momentum}")

    print("\n--- Entangling particles ---")
    p1.entangle(p2)
    
    print(f"\nInitial spins before measurement:")
    print(f"Particle 1 spin: {p1.spin}")
    print(f"Particle 2 spin: {p2.spin}")
    
    print("\n--- Measuring spin of Particle 1 ---")
    p1.spin_measurement()
    
    print(f"Spin of p1 after measurement: {p1.spin}")
    print(f"Spin of p2 (the entangled partner): {p2.spin}")

    print("\n--- Attempting to entangle with a non-particle ---")
    try:
        p3 = "not a particle"
        p1.entangle(p3)
    except TypeError as e:
        print(f"Error caught: {e}")

        #end