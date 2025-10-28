#Project DEFCON
#dictionaries of weapon yields
import numpy as np

class US_NuclearWeapon:
    """Base class for nuclear weapons."""
    def __init__(self, name, yield_kt, delivery_system):
        if yield_kt <= 0:
            raise ValueError("Yield must be positive")
        self.name = name
        self.yield_kt = yield_kt
        self.delivery_system = delivery_system
    
    def damage(self):
        """Method to calculate the damage of the weapon. Must be overridden in subclasses."""
        raise NotImplementedError("This method should be overridden in subclasses")

    def calculate_casualties(self, city_population):
        """Simplified casualty calculation assuming 80% casualty rate."""
        return city_population * 0.8
    
    def calculate_target_casualties(self, target_population):
        """Simplified casualty calculation for military targets assuming 50% casualty rate."""
        return target_population * 1.0

class B83(US_NuclearWeapon):
    """Class for the B83 thermonuclear bomb."""
    def __init__(self, name, yield_kt, delivery_system):
        super().__init__(name, yield_kt, delivery_system)
    
    def damage(self):
        """Damage calculation for the B83 bomb."""
        return self.yield_kt * 10
    
    def calculate_casualties(self, city_population):
        """Casualty calculation for the B83 bomb."""
        return city_population * 0.80
    
    def calculate_target_casualties(self, target_population):
        """Simplified casualty calculation for military targets assuming 100% casualty rate."""
        return target_population * 1.0

class B61_MOD13(US_NuclearWeapon):
    """Class for the B61 Mod 13 thermonuclear bomb."""
    def __init__(self, name, yield_kt, delivery_system):
        super().__init__(name, yield_kt, delivery_system)
    
    def damage(self):
        """Damage calculation for the B61 Mod 13 bomb."""
        return self.yield_kt * 10
    
    def calculate_casualties(self, city_population):
        """Casualty calculation for the B61 Mod 13 bomb."""
        return city_population * 0.55
    
    def calculate_target_casualties(self, target_population):
        """Simplified casualty calculation for military targets assuming 100% casualty rate."""
        return target_population * 1.0

class W87(US_NuclearWeapon):
    """Class for the W87 tactical nuclear weapon."""
    def __init__(self, name, yield_kt, delivery_system, range_km):
        super().__init__(name, yield_kt, delivery_system)
        self.range_km = range_km  # Effective range of the tactical weapon
    
    def damage(self):
        """Damage calculation for the W87 weapon."""
        return self.yield_kt * 10
    
    def calculate_casualties(self, city_population):
        """Casualty calculation for the W87 weapon."""
        return city_population * 0.55
    
    def calculate_target_casualties(self, target_population):
        """Simplified casualty calculation for military targets assuming 100% casualty rate."""
        return target_population * 1.0

class W88(US_NuclearWeapon):
    """Class for the W88 tactical nuclear weapon."""
    def __init__(self, name, yield_kt, delivery_system, range_km):
        super().__init__(name, yield_kt, delivery_system)
        self.range_km = range_km  # Effective range of the tactical weapon
    
    def damage(self):
        """Damage calculation for the W88 weapon."""
        return self.yield_kt * 10
    
    def calculate_casualties(self, city_population):
        """Casualty calculation for the W88 weapon."""
        return int(city_population * 0.65)
    
    def calculate_target_casualties(self, target_population):
        """Simplified casualty calculation for military targets assuming 100% casualty rate."""
        return int(target_population * 1.0)

class W76_MOD1(US_NuclearWeapon):
    """Class for the W76 Mod 1 tactical nuclear weapon."""
    def __init__(self, name, yield_kt, delivery_system, range_km):
        super().__init__(name, yield_kt, delivery_system)
        self.range_km = range_km  # Effective range of the tactical weapon
    
    def damage(self):
        """Damage calculation for the W76 Mod 1 weapon."""
        return self.yield_kt * 10
    
    def calculate_casualties(self, city_population):
        """Casualty calculation for the W76 Mod 1 weapon."""
        return city_population * 0.1
    
    def calculate_target_casualties(self, target_population):
        """Simplified casualty calculation for military targets assuming 90% casualty rate."""
        return target_population * 0.9

# Example instances
if __name__ == "__main__":
    # Create instances of each weapon type
    B83_Gravity_Bomb = B83(name="B83", yield_kt=1200, delivery_system="B-52 Stratofortress")
    B61_MOD13_Gravity_Bomb = B61_MOD13(name="B61 Mod 13", yield_kt=360, delivery_system="F-35 Lightning II")
    W87_Warhead = W87(name="W87", yield_kt=300, delivery_system="ICBM", range_km=9600)
    W88_Warhead = W88(name="W88", yield_kt=475, delivery_system="SLBM", range_km=7400)
    W76_MOD1_Warhead = W76_MOD1(name="W76 Mod 1", yield_kt=90, delivery_system="SLBM", range_km=7400)

    city_population = 100000
    target_population = 8000

    # Calculate and print casualties for each weapon
    print(f"{B83_Gravity_Bomb.name} damage: {B83_Gravity_Bomb.damage()} estimated military casualties: {B83_Gravity_Bomb.calculate_target_casualties(target_population)} estimated casualties: {B83_Gravity_Bomb.calculate_casualties(city_population)}")
    print(f"{B61_MOD13_Gravity_Bomb.name} damage: {B61_MOD13_Gravity_Bomb.damage()} estimated military casualties: {B61_MOD13_Gravity_Bomb.calculate_target_casualties(target_population)} estimated casualties: {B61_MOD13_Gravity_Bomb.calculate_casualties(city_population)}")
    print(f"{W87_Warhead.name} damage: {W87_Warhead.damage()} estimated military casualties: {W87_Warhead.calculate_target_casualties(target_population)} estimated casualties: {W87_Warhead.calculate_casualties(city_population)}")
    print(f"{W88_Warhead.name} damage: {W88_Warhead.damage()} estimated military casualties: {W88_Warhead.calculate_target_casualties(target_population)} estimated casualties: {W88_Warhead.calculate_casualties(city_population)}")
    print(f"{W76_MOD1_Warhead.name} damage: {W76_MOD1_Warhead.damage()} estimated military casualties: {W76_MOD1_Warhead.calculate_target_casualties(target_population)} estimated casualties: {W76_MOD1_Warhead.calculate_casualties(city_population)}")