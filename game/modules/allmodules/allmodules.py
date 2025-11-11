
import pygame
'''Purpose: Used as the primary (and only) game engine for "NULL0", pygame-ce (community edition) is used as the documentation is regularly updated'''
import socket
import threading

#MATH RELATED LIBRARIES
from sympy import * #Purpose: Render equations as text/images within game 
'''Purpose: Render equations respective to player w/ latex & images within the game.'''
from sympy.abc import x #Purpose: Prevent issues with undefined variables, add as needed 
'''Purpose: Prevent undefined variable errors, adds x as required.'''
from sympy.testing.pytest import ignore_warnings
'''Purpose: To avoid crashes/errors when division by zero errors are thrown.'''
import numpy as np #Purpose: Do rote mathematical calculations to store into arrays speedily, x and y mapped 
'''Purpose: Perform rote mathematical calculations, storing into numpy arrays preventing the requirement for loops, improving the efficiency of retrieving the dedicated function. Used to store 2D arrays that can perform operations.'''
from PIL import Image #Purpose: Generate a compressed image made by sympy, increases game performance and efficiency
'''Purpose: Generate a compressed sympy image, allowing for unique sized equations with custom DPI settings, increases game performance and efficiency'''
import os.path #Compatibility for paths between linux and windows, as / \ mismatches can occur
'''Purpose: Allow compatibility for paths between linux and windows by correcting / \ mismatches'''
import math 
'''Purpose: Exception handling of NaN, +inf & -inf as solutions for sympy equations'''
import numexpr
'''Purpose: Fast numerical expression evaluator for NumPy, codeprinter used for numerical evaluation'''


from common.player_brief import PlayerBrief
'''See common/player_brief'''

from common.network_requests import NetworkObjectTypes, GetGames
'''See common/network_requests'''

from common.client_connection import ClientConnection
'''See common/client_connection.py'''

from game.modules.clamp import Clamp
'''See game/modules/clamp.py'''

#GAME_DEPENDENCIES
from game.data.background.background import bounds_x, bounds_y, grid_spacing, GridBackground
'''Purpose: Generating a background with rendering boundaries of bounds_x by bounds_y, and with grid_lines that are "grid_spacing" amount apart, includes class GridBackground housing two methods'''

from game.data.display.display import screen, display_info, display_flags, width, height
'''Purpose: Generating a screen surface representative of the resolution of monitor [width, height]. Display_info and display_flags record the properties of the display monitor as well as the surface properties, respectively.'''

from game.data.display.frames import clock, framerate
'''Purpose: Generate a clock with pygame and maintaining a universal framerate for the game to render at'''

from game.data.player.player_render import player, player_size, player_border, player_scope_size, player_velocity_base, player_pos_init_x, player_pos_init_y, RenderPlayer
'''Purpose: Generate a player, with corresponding proprties attributed to its rendered appearance, movement, and position'''

from game.data.player.player_movement import PlayerMovement
'''Purpose: Tracking movement of player after detection of key presses through pygame'''

from game.data.objects.equation import EquationObject
'''Purpose: Generating an equation that moves alongside the player, representative of its function in latex'''

from game.data.player.player_func import PlayerFunc
'''Purpose: Initialization of the player function.'''

from game.data.operations.operationself import OperationsSelf
'''Purpose: Operations that are accessible for the player to perform upon its own function'''

from game.modules.generateimage import GenerateImage
'''Purpose: Generate an image of the player's designated equation, with its subsequent storage as a temporary file'''

from game.modules.reset_surface import ResetSurface
'''Purpose: Re-drawing of surface for clean slate, necessary for repetitive blitting of surfaces'''

from game.data.exceptions.errors import CheckFunctions
'''Purpose: Negate the errors thrown for functions that possess NaN, +inf, with math imported for NaN/inf detection'''

from game.data.preload.sound_effects import SoundEffects
'''Purpose: Maintain dedicated python file for sound effects, used or unused'''

from game.data.preload.fonts import font_cmu_rm, font_cmu_bld
'''Purpose: Maintain dedicated python file for fonts, used or unused, Computer Modern Serif Roman font'''

from game.data.animations.intro_animation import IntroAnimation
'''Purpose: Dedicated intro animation serving as a segue for the rest of the game'''

from game.data.gamestates.intro_skip import IntroSkip
'''Purpose: Skippable section at beginning to skip the intro cutscene'''

from game.data.preload.colors import ColorsManual
'''Purpose: Maintain dedicated python files for colors, used or unused, helps for reusing colors'''


from game.data.objects.enemy import Enemy
'''Purpose: Generate Enemy objects and set their absolute positions [effect of staying still as player moves across screen]'''


from game.data.objects.minimap import MiniMap
'''Purpose: Generate a graphic minimap, not complete, for now represents coordinates of the player & enemy rect objects as well as their attribute values [dx/dy]'''

from game.data.objects.hitboxes import Hitbox
'''Purpose: Generate a hitbox for the respective entity based upon the size of their radius, meant to deal with collisions, seperate from the player/enemy rects themselves'''

from game.data.controls.control_operations import ControlOperations
'''Purpose: Display the images of the various controls for the player to utilize, serving for now as a helpful indicator of the various abilities at the player's disposal '''

from game.data.function.generate_graph_plots import GeneratePlots
'''Purpose: Generate the plot points for the function assigned to the player at a given instance, after conversion of SymPy expression to numerical evaluation of NumPy through Lambdify'''

from game.data.function.draw_function import DrawFunction
'''Purpose: Draw the resulting plot points generated by "GeneratePlots", by rendering grouped lines sequentially'''
