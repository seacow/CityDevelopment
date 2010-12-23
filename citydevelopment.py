import pygame, sys
from pygame.locals import *
import buttonbar


# Make a building manager. --> Not in this prototype though
# Its purpose is to hold all information on building.
# A city will tell the manager when it builds or researches something,
#  and then the manager will tell the city what buildings are unlocked.

# Make a tech manager. --> Not in this prototype though
# Its purpose is to hold all information on technologies.
# A city will tell the manager when it builds or researches something,
#  and then the manager will tell the city what techs are unlocked.

# Or should we take some of the creation power from the city and give 
#  it to the managers?
# For example, a manager will tell the city when it gets a tech/building.
# Though there will only be 1 tech manager and tons of cities..... 



class Building:
    def __init__ (self, name, city):
        self.name = name
        self.city = city
        self.technologies = []

    def create_building (self):
        self.city.add_building (self)

    def get_technologies (self):
        return self.technologies

    def get_name (self):
        return self.name

class Technology:
    def __init__ (self, name, city):
        self.name = name
        self.city = city

    def gain_technology (self):
        self.city.add_technology (self)

    def get_name (self):
        return self.name

class Granary (Building):
    def __init__ (self, city):
        Building.__init__ (self, 'Granary', city)
        self.technologies.append (Technology ('Plow', city))

class LumberMill (Building):
    def __init__ (self, city):
        Building.__init__ (self, 'Lumber Mill', city)
        self.technologies.append (Technology ('Axe', city))
class Smelter (Building):
    def __init__ (self, city):
        Building.__init__ (self, 'Smelter', city)
        self.technologies.append (Technology ('Shovel', city))

class City:
    def __init__ (self, name):
        self.name = name
        self.buildings = []
        self.technologies = []
        # resources

    def add_building (self, building):
        self.buildings.append(building)
    def add_technology (self, technology):
        self.technologies.append(technology)

    def get_name (self):
        return self.name

if __name__ == '__main__':
    pygame.init()
    size = 320, 240
    screen = pygame.display.set_mode(size)

    city = City ('Seacowton')

    granary = Granary (city)
    lumber_mill = LumberMill (city)
    smelter = Smelter (city)
    #building_list = []
    #building_list.append(Building('Farm'))
    #building_list.append(Building('Lumber Camp'))
    #building_list.append(Building('Mine'))
    #building_list.append(Building('Market'))
    #building_list.append(Building('House'))
    #building_list.append(Building('Granary'))
    #building_list.append(Building('Lumber Mill'))
    #building_list.append(Building('Smelter'))
    #building_list.append(Building('Blacksmith'))
    #building_list.append(Building('Harbor'))


    bar = buttonbar.Bar(screen)
    city_contents = buttonbar.Button (bar, 'Print city')
    granary_button = buttonbar.Button (bar, 'Granary', granary.create_building)
    lumber_mill_button = buttonbar.Button (bar, 'Lumber Mill', lumber_mill.create_building)
    smelter_button = buttonbar.Button (bar, 'Smelter', smelter.create_building)
    #granary_button = buttonbar.Button (bar, 'Granary')
    #lumber_mill_button = buttonbar.Button (bar, 'Lumber Mill')
    #smelter_button = buttonbar.Button (bar, 'Smelter')
    #farm_button = buttonbar.Button (bar, 'Farm')
    #lumbercamp_button = buttonbar.Button (bar, 'Lumber Camp')
    #mine_button = buttonbar.Button (bar, 'Mine')
    #market_button = buttonbar.Button (bar, 'Market')
    #house_button = buttonbar.Button (bar, 'House')
    #blacksmith_button = buttonbar.Button (bar, 'Blacksmith')
    #harbor_button = buttonbar.Button (bar, 'Harbor')

    tech_buttons = []
    for building in granary, lumber_mill, smelter:
        for tech in building.get_technologies():
            tech_buttons.append (buttonbar.Button (bar, tech.get_name(), tech.gain_technology))


    while True:
        screen.fill((0,0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type in bar.EVENTS:
                clicked = bar.update(event)
                for button in clicked:
                    if button == city_contents:
                        print 'Buildings in %s' %city.get_name()
                        for building in city.buildings:
                            print building.get_name()
                        print ''
                        print 'Technologies in %s' %city.get_name()
                        for tech in city.technologies:
                            print tech.get_name()
                        print ''
                        print ''
                    else:
                        button.hide()
        bar.draw(screen)

        pygame.display.flip()
        pygame.time.wait(50)
