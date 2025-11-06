
from game.modules.modules import *
pygame.init()
pygame.mixer.init()
pygame.display.set_caption("spinNull0")
from game.modules.clamp import Clamp 
from game.data.background.background import bounds_x, bounds_y, grid_spacing, GridBackground
from game.data.display.display import screen, display_info, display_flags
from game.data.player.player_render import player,  player_size, RenderPlayer
from game.data.player.player_movement import PlayerMovement
from game.data.objects.textbox import TextBox
from game.data.objects.equation import EquationObject
from game.data.player.player_func import PlayerFunc
from game.data.objects.point import PointObject
from game.data.operations.operationself import OperationsSelf
from game.modules.generateimage import GenerateImage
from game.modules.reset_surface import ResetSurface
from game.data.exceptions.errors import CheckFunctions
from game.data.preload.sound_effects import sound_effect_function_draw, sound_effect_intro_animation, sound_effect_null_robot, sound_effect_electric, sound_effect_powerup, sound_effect_blast, sound_effect_interaction
from game.data.preload.fonts import font_cmu_rm, font_cmu_bld
from game.data.animations.intro_animation import IntroAnimation
from game.data.gamestates.intro_skip import IntroSkip
from game.data.preload.colors import ColorsManual

