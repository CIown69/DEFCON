#Project DEFCON

from DEFCON_Arsenal import B83, B61_MOD13, W87, W88, W76_MOD1
from DEFCON_Targets import russian_military_targets, Russian_Cities, Chinese_Cities, chinese_military_targets
from DEFCON_WarPlans import MilitaryStrikePackage, CityStrikePackage, russian_military_strike_package, russian_city_strike_package, chinese_city_strike_package, chinese_military_strike_package
import time
import sys

B83_Gravity_Bomb = B83(name="B83 Hydrogen Bomb", yield_kt=1200, delivery_system="B-52 Stratofortress")
B61_MOD13_Gravity_Bomb = B61_MOD13(name="B61 Mod 13 Hydrogen Bomb", yield_kt=360, delivery_system="F-35 Lightning II")
W87_Warhead = W87(name="W87 Warhead", yield_kt=300, delivery_system="Minuteman III MIRV ICBM", range_km=9600)
W88_Warhead = W88(name="W88 Warhead", yield_kt=475, delivery_system="Trident II MIRV SLBM", range_km=7400)
W76_MOD1_Warhead = W76_MOD1(name="W76 Mod 1 Warhead", yield_kt=90, delivery_system="Trident II MIRV SLBM", range_km=7400)

def user_data():
    new_username = input("Name: ")
    return new_username

def checklist():
    username = user_data()
    print("")
    print("Welcome '",(username),"' NORAD has ICBM launch detection. Confidence is HIGH. ")
    print("NORAD Tracking 1,200 inbound targets")
    time.sleep(1)
    print("Proceed in counter attack?")
    response = input("")
    if response == 'yes':
        return
    elif response == 'no':
        print("Understood, NORAD is Standing Down.")
        time.sleep(1)
        print("The warning from NORAD was unwarrented, a computer glitch was the cause of the alarm.")
        time.sleep(1)
        print("World War 3 was averted") 
        sys.exit()
    else:
        print("Invalid response, Please try again")
        return checklist()
    
def targetlist():
    response = input("")
    if response == 'yes':
        from DEFCON_ICBMDATA import fig
        return
    elif response == 'no':
        print("Stand Down Missile Defense?") 
        response == input("")
        if response == 'yes':
            sys.exit()
        elif response == 'no':
            print("*Returning to target list*")
            time.sleep(2)
            print("Input: Yes or No")
            return targetlist()
        else:
            print("Invalid Input")
            print("*Returning to target list*")
            time.sleep(2)
            return targetlist()
    else:
        print("Invalid response, Please try again")
        return targetlist()
    
def defenseplan():
    print("Russian Full Scale Retalitory Strike - option 1")
    print("Chinese Full Scale Retalitory Strike - option 2")
    time.sleep(1)
    response = input("Enter 1 or 2:")
    if response == '1':
        print("Counter Value Plan or Counter Force Plan?")
        print("1 (Counter Value) or 2 (Counter Force)")
        print("Or Enter help, for more information.")
        response = input("")
        if response == '1':
            russian_city_strike_package.execute()
        elif response == '2':
            russian_military_strike_package.execute()
        elif response == 'help':
            print("Counter Force Plan:")
            print("This Nuclear Stategy aims for military targets only, and aims to lower civilian causalties.")
            time.sleep(2)
            print("Counter Value Plan:") 
            print("This Strategy refers to the MAD doctorine, in which civillian populations are targeted.")
            print("Aiming for the highest death toll and capitulation of the society.")
            return defenseplan()
        else:
            print("Invalid Strike Option")
            return defenseplan()
    elif response == '2':
        print("Counter Value Plan or Counter Force Plan?")
        print("1 (Counter Value) or 2 (Counter Force)")
        print("Or Enter HELP, for more information.")
        response = input("")
        if response == '1':
            chinese_city_strike_package.execute()
        elif response == '2':
            chinese_military_strike_package.execute()
        elif response == 'HELP':
            print("Counter Force Plan:")
            print("This Nuclear Stategy aims for military targets only, and aims to lower civilian causalties.")
            time.sleep(2)
            print("Counter Value Plan:") 
            print("This Strategy refers to the MAD doctorine, in which civillian populations are targeted.")
            print("Aiming for the highest death toll and capitulation of the society.")
            return defenseplan()
        else:
            print("Invalid Strike Option")
            return defenseplan()
    else:
        print("Invalid input, returning to options.")
        time.sleep(1)
        return defenseplan()
    
def simresults():
    response = input("Yes or No: ")
    if response == 'yes':
        print("Estimations predict a current total of over 360 million dead.")
        time.sleep(1)
        print("Predicitons indicate a further 5 Billion to die from indirect causes; Starvation, elements, loss-of-shelter, etc.")
        time.sleep(1)
        print("The collapse of human civilization is imminent.")
        time.sleep(1)
    
def main():
    print("WARNING NUCLEAR ATTACK IMMINENT")
    time.sleep(1)
    print("DEFCON 1 has been raised, please complete the checklist and move to launch control.")
    time.sleep(1)
    print("*DO NOT USE CAPITALIZATION*")
    print("")

    print("Designated Survivor")
    print("------------------------------------------------------------------")
    print("Enter Your Information:")
    checklist()

    print("Current Arsenal List: 3,708 Warheads")
    print(B83_Gravity_Bomb.name,"|" "Yield:", B83_Gravity_Bomb.yield_kt,"Kilotons","|" "Delivery:", B83_Gravity_Bomb.delivery_system)
    time.sleep(1)
    print(B61_MOD13_Gravity_Bomb.name,"|" "Yield:", B61_MOD13_Gravity_Bomb.yield_kt,"Kilotons","|" "Delivery:", B61_MOD13_Gravity_Bomb.delivery_system)
    time.sleep(1)
    print(W87_Warhead.name,"|" "Yield:", W87_Warhead.yield_kt,"Kilotons","|" "Delivery:", W87_Warhead.delivery_system)
    time.sleep(1)
    print(W88_Warhead.name,"|" "Yield:", W88_Warhead.yield_kt,"Kilotons","|" "Delivery:", W88_Warhead.delivery_system)
    time.sleep(1)
    print(W76_MOD1_Warhead.name,"|" "Yield:", W76_MOD1_Warhead.yield_kt,"Kilotons","|" "Delivery:", W76_MOD1_Warhead.delivery_system)

    print("Access Projected Target List?")
    targetlist()
    print("*Targets Locked*")
    print("Select Defense Plan:")
    defenseplan()
    time.sleep(5)
    print("US TARGETS DESTROYED IN COUNTER ATTACK")
    print("ALL COMBAT UNITS LOST")
    time.sleep(2)
    print("")
    print("You have completed your duty, in an honorable fashion.")
    time.sleep(2)
    print("Would You like to see your results?")
    simresults()

    print("Do you want to see your hometown?")
    print("Yes or No")
    response = input("")
    if response == 'yes':
        from DEFCON_Detonation import get_city_coordinates, fig
        print("THE WAR IS OVER")
    elif response == 'no':
        print("You're right, it might be easier to not know.")
        print("THE WAR IS OVER")
    else:
        print("I'll take that as a 'no'; It might be easier to live in ignorance.")
        print("THE WAR IS OVER")

if __name__ == "__main__":
    main()