##NOT IN USE I REPEAT NOT IN USE, JUST TO DOCUMENT ALL MODULES/REOCCURING OBJECTS IN USE
import socket
import threading
import pygame
from common.player_brief import PlayerBrief
from common.network_requests import NetworkObjectTypes, GetGames
from common.client_connection import ClientConnection

class Clamp:
   def clamp(val, min, max):
      """
      Given a numeric value, and minimum and maximum values, will restrict the value to within the range of min to max and return. Min should be less than max or nothing will happen
      """

      if val < min: val = min
      elif val > max: val = max
      return val
   pass


