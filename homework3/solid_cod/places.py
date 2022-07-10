from abc import ABC, abstractmethod


class Place(ABC):

    @abstractmethod
    def get_local_antagonist(self):
        ...

class Kostroma(Place):
#    name = 'Kostroma'
    coordinates = [11.11, 22.22]
    def get_local_antagonist(self):
        print('Orcs hid in the forest')


class Tokyo(Place):
    name = 'Tokyo'

    def get_local_antagonist(self):
        print('Godzilla stands near a skyscraper')
