#DOCUMENTATION CAN BE FOUND @ ./allmodules/allmodules.py


import socket
import threading

#MATH RELATED LIBRARIES
from sympy import * 
from sympy.abc import x 
from sympy.testing.pytest import ignore_warnings
import numpy as np 
from PIL import Image 
import os.path 
import math 
from scipy.integrate import quad
import numexpr

from common.player_brief import PlayerBrief
from common.network_requests import NetworkObjectTypes, GetGames
from common.client_connection import ClientConnection
from game.modules.clamp import Clamp 

from game.data.background.background import bounds_x, bounds_y, grid_spacing, GridBackground
from game.data.display.display import screen, display_info, display_flags, width, height
from game.data.display.frames import clock, framerate
from game.data.player.player_render import player, player_size, player_border, player_scope_size, player_velocity_base, player_pos_init_x, player_pos_init_y, RenderPlayer
from game.data.player.player_movement import PlayerMovement
from game.data.objects.equation import EquationObject
from game.data.player.player_func import PlayerFunc
from game.data.operations.operationself import OperationsSelf
from game.modules.generateimage import GenerateImage
from game.modules.reset_surface import ResetSurface
from game.data.exceptions.errors import CheckFunctions
from game.data.preload.sound_effects import SoundEffects
from game.data.preload.fonts import font_cmu_rm, font_cmu_bld
from game.data.animations.intro_animation import IntroAnimation
from game.data.gamestates.intro_skip import IntroSkip
from game.data.preload.colors import ColorsManual
from game.data.objects.enemy import Enemy
from game.data.objects.minimap import MiniMap
from game.data.objects.hitboxes import Hitbox
from game.data.controls.control_operations import ControlOperations
from game.data.function.generate_graph_plots import GeneratePlots
from game.data.function.draw_function import DrawFunction

