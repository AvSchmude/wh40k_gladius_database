import os
import re
import sys
import copy
import traceback
from typing import List, Union

import pandas as pd
import numpy as np
import tkinter

from tkinter import filedialog
from bs4 import BeautifulSoup


class XMLReader:
    def __init__(self):
        self.path = ""
        # Unit stats and cost keywords as used in the xml files
        self.unit_stats = ['name', 'armor', 'hitpointsMax',
                           'moraleMax', 'movementMax', 'size',
                           'itemSlots', 'cargoSlots']
        self.unit_costs = ['productionCost', 'foodCost', 'oreCost',
                           'energyCost', 'influenceCost', 'foodUpkeep',
                           'oreUpkeep', 'energyUpkeep', 'influenceUpkeep']
        self.unit_attributes = self.unit_stats + self.unit_costs

    def ask_for_steam_path(self):
        tkinter.Tk().withdraw()  # prevents an empty tkinter window from appearing\n",
        self.path = filedialog.askdirectory()
        # unit_filepath = path + '\\steamapps\\common\\Warhammer 40000 Gladius - Relics of War\\Data\\World\\Units\\ChaosSpaceMarines'
        # icon_filepath = path + '\\steamapps\\common\\Warhammer 40000 Gladius - Relics of War\\Data\\Video\\Textures\\Icons\\Attributes'
        # unit_filepath = 'S:\\SteamLibrary\\steamapps\\common\\Warhammer 40000 Gladius - Relics of War\\Data\\World\\Units\\ChaosSpaceMarines'
        # icon_filepath = 'S:\\SteamLibrary\\steamapps\\common\\Warhammer 40000 Gladius - Relics of War\\Data\\Video\\Textures\\Icons\\Attributes'
        # os.chdir(unit_filepath)
        # os.getcwd()"

    @staticmethod
    def set_path():
        path = 'C:\\Users\\\\Adria\\Documents\\Python_Projekt\\Wh40k - Gladius - Game Files\\Units\\\\ChaosSpaceMarines'
        if os.getcwd() != path:
            os.chdir(path)
        os.getcwd()

    @staticmethod
    def edit_list(data: list):
        """Edit list containing strings.
           Inserts spaces before capitalized letters.
           Then capitalizes the first letter of each word.
           Removes 'Max' from each String.
        """
        data_copy = copy.deepcopy(data)
        for index, elem in enumerate(data_copy):
            data_copy[index] = re.sub(pattern="", repl="", string=elem).title().replace(' Max', '')
        return data_copy

    def create_soups(self):
        # Function creates a list containing the soup of each xml file"
        pot: list[list[Union[BeautifulSoup, str]]] = []
        os.chdir('C:\\Users\\Adria\\Documents\\Python_Projekt\\Wh40k - Gladius - Game Files\\Units\\ChaosSpaceMarines')
        files = os.listdir()
        for file in files:
            if file == 'Headquarters.xml':
                continue
            with open(file, 'r') as f:
                data = f.read()
                soup = BeautifulSoup(data, 'xml')
                pot.append([soup, file])
            os.chdir('C:\\Users\\Adria\\Documents\\Python_Projekt\\Wh40k - Gladius - Game Files\\')
            return pot
        "pot = create_soups() "


if __name__ == '__main__':
    print("Start")

    edit_unit_attrs = edit_list(unit_attributes)
    print(edit_unit_attrs)