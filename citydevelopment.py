import pygame, sys
from pygame.locals import *
import buttonbar



class Building:
    def __init__ (self, name):
        self.name = name
    def get_name (self):
        return self.name


#class Granary (Building):
    #def __init__ (self):
        #Building.__init__ (self, 'Granary')
        ##unique techs
#class LumberMill (Building):
    #def __init__ (self):
        #Building.__init__ (self, 'Lumber Mill')
#class Smelter (Building):
    #def __init__ (self):
        #Building.__init__ (self, 'Smelter')

class City:
    def __init__ (self, name):
        self.name = name
        self.buildings = []
        self.available_buildings = []
        # resources
        # available technologies
    def add_building (self, building):
        self.buildings.append(building)
    def get_name (self):
        return self.name

if __name__ == '__main__':
    pygame.init()
    size = 320, 240
    screen = pygame.display.set_mode(size)

    #building_list = []
    #building_list.append(Building('Granary'))
    #building_list.append(Building('Lumber Mill'))
    #building_list.append(Building('Smelter'))
    granary = Building('Granary')
    lumber = Building('Lumber Mill')
    smelter = Building('Smelter')

    bar = buttonbar.Bar(screen)
    city_contents = buttonbar.Button (bar, 'Print city')
    granary_button = buttonbar.Button (bar, 'Granary')
    lumber_button = buttonbar.Button (bar, 'Lumber Mill')
    smelter_button = buttonbar.Button (bar, 'Smelter')


    city = City ('Seacowton')

    while True:
        screen.fill((0,0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type in bar.EVENTS:
                clicked = bar.update(event)
                if granary_button in clicked:
                    city.add_building (granary)
                    granary_button.hide()
                if lumber_button in clicked:
                    city.add_building (lumber)
                    lumber_button.hide()
                if smelter_button in clicked:
                    city.add_building (smelter)
                    smelter_button.hide()
                if city_contents in clicked:
                    print 'Buildings in %s' %city.get_name()
                    for building in city.buildings:
                        print building.get_name()
                    print ''
        bar.draw(screen)

        pygame.display.flip()
        pygame.time.wait(50)
