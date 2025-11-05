import socket
import threading
import pygame


#MATH RELATED LIBRARIES
from sympy import * #Purpose: Render equations as text/images within game 
from sympy.abc import x #Purpose: Prevent issues with undefined variables, add as needed 
import numpy as np #Purpose: Do rote mathematical calculations to store into arrays speedily, x and y mapped 
from PIL import Image #Purpose: Generate a compressed image made by sympy, increases game performance and efficiency
import os.path #Compatibility for paths between linux and windows, as / \ mismatches can occur
import math #EXCEPTION HANDLING


from common.player_brief import PlayerBrief
from common.network_requests import NetworkObjectTypes, GetGames
from common.client_connection import ClientConnection
