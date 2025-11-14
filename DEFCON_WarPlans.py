import time
from DEFCON_Arsenal import B83, B61_MOD13, W87, W88, W76_MOD1
from DEFCON_Targets import Chinese_Cities, Russian_Cities, russian_military_targets, chinese_military_targets

class StrikePackage:
    """Base class to represent a strike package."""
    def __init__(self, name, targets):
        self.name = name
        self.targets = targets  # List of target dictionaries
    
    def execute(self):
        """Execute the strike package."""
        print(f"Executing strike package: {self.name}")
        for target in self.targets:
            self.strike_target(target)
    
    def select_weapon(self, target_type):
        """Select a weapon based on the target importance."""
        if target_type == "Large":
            return B83(name="B83", yield_kt=1200, delivery_system="B-52 Stratofortress")
        elif target_type == "Medium":
            return W88(name="W88", yield_kt=475, delivery_system="SLBM", range_km=7400)
        elif target_type == "Small":
            return W87(name="W87", yield_kt=300, delivery_system="ICBM", range_km=9600)
        elif target_type == "Tactical":
            return W76_MOD1(name="W76 Mod 1", yield_kt=90, delivery_system="SLBM", range_km=7400)
        else:
            return B61_MOD13(name="B61 Mod 13", yield_kt=360, delivery_system="F-35 Lightning II")


class CityStrikePackage(StrikePackage):
    """Class to represent a city strike package."""
    def strike_target(self, target):
        """Select and strike the target."""
        name, attributes = target
        target_type, population = attributes

        print(f"Striking Target city: {name}, a {target_type} city with a population of {population}")

        weapon = self.select_weapon(target_type)
        casualties = weapon.calculate_casualties(population)
        print(f"Selected weapon: {weapon.name}, Estimated casualties: {casualties}")
        time.sleep(1)
        print("")

class MilitaryStrikePackage(StrikePackage):
    """Class to represent a military target strike package."""
    def strike_target(self, target):
        """Select and strike the target."""
        name, attributes = target
        target_type, target_population = attributes

        print(f"Striking military target: {name}, a {target_type} target, with a military population of {target_population}")

        weapon = self.select_weapon(target_type)
        casualties = weapon.calculate_target_casualties(target_population)
        print(f"Selected weapon: {weapon.name}, Estimated casualties: {casualties}")
        time.sleep(2)
        print("")

# Define your strike packages
russian_military_strike_package = MilitaryStrikePackage("NATO-Russian Counter Force Plan", russian_military_targets.items())
chinese_military_strike_package = MilitaryStrikePackage("Chinese Counter Force Plan", chinese_military_targets.items())
russian_city_strike_package = CityStrikePackage("NATO-Russian Counter Value Plan", Russian_Cities.items())
chinese_city_strike_package = CityStrikePackage("Chinese Counter Value Plan", Chinese_Cities.items())

# Execute the strike packages
def main():
    print("NATO-Russian Escalation")
    print("Far East Strategy")
    response = input("Choose Scenario: ").lower()

    if response == ("NATO-Russian Escalation").lower():
        response2 = input("Counter Force Plan or Counter Value Plan:  ").lower()
        if response2 == ("Counter Force").lower():
            russian_military_strike_package.execute()
        elif response2 == ("Counter Force Plan").lower():
            russian_military_strike_package.execute()
        
        elif response2 == ("Counter Value").lower():
            russian_city_strike_package.execute()
        elif response2 == ("Counter Value Plan").lower():
            russian_city_strike_package.execute()

        else:
            print("Invalid Input")

    elif response == ("Far East Strategy").lower():
        response2 = input("Counter Force Plan or Counter Value Plan:  ").lower()
        if response2 == ("Counter Force").lower():
            chinese_military_strike_package.execute()
        elif response2 == ("Counter Force Plan").lower():
            chinese_military_strike_package.execute()
        
        elif response2 == ("Counter Value").lower():
            chinese_city_strike_package.execute()
        elif response2 == ("Counter Value Plan").lower():
            chinese_city_strike_package.execute()

        else:
            print("Invalid Input")   

    else:
        print("Invalid Input") 

if __name__ == "__main__":
    main()