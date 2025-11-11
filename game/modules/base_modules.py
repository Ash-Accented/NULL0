import socket
import threading
import pygame


#MATH RELATED LIBRARIES
from sympy import * #Purpose: Render equations as text/images within game 
from sympy.abc import x #Purpose: Prevent issues with undefined variables, add as needed 
from sympy.testing.pytest import ignore_warnings
import numpy as np #Purpose: Do rote mathematical calculations to store into arrays speedily, x and y mapped 
from PIL import Image #Purpose: Generate a compressed image made by sympy, increases game performance and efficiency
import os.path #Compatibility for paths between linux and windows, as / \ mismatches can occur
import math #EXCEPTION HANDLING
from scipy.integrate import quad
import numexpr
#numpy.linspace[start, stop, number_of_points] [change from numpy.arange --> numpy.linspace]
#Iterating through an array [depend on numpy's ability to iterate through the numbers themselves; augmented memory]

from common.player_brief import PlayerBrief
from common.network_requests import NetworkObjectTypes, GetGames
from common.client_connection import ClientConnection
from game.modules.clamp import Clamp 
