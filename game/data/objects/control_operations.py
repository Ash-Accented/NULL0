from game.modules.base_modules import *
from game.modules.preloads import *
from game.modules.generateimage import GenerateImage
class ControlOperations(pygame.sprite.Sprite):
   def __init__(self, w, h):
      pygame.sprite.Sprite.__init__(self)
      self.w = w
      self.h = h
      self.ind_sh = False
      self.img_lst = ControlOperations.controls(self)

   def controls(ctrl_obj):
      path_desired = "game/images/operations/"
      one_add = GenerateImage.render_equation_copy(ctrl_obj, path_desired, "addition.png")
      two_subtract = GenerateImage.render_equation_copy(ctrl_obj, path_desired, "subtraction.png")
      three_multiply = GenerateImage.render_equation_copy(ctrl_obj, path_desired, "multiplication.png")
      four_divide = GenerateImage.render_equation_copy(ctrl_obj, path_desired, "division.png")
      five_powered = GenerateImage.render_equation_copy(ctrl_obj, path_desired, "powerof.png")
      six_differentiate = GenerateImage.render_equation_copy(ctrl_obj, path_desired, "derivative.png")
      seven_integrate = GenerateImage.render_equation_copy(ctrl_obj, path_desired, "integral.png")
      eight_exponentiate = GenerateImage.render_equation_copy(ctrl_obj, path_desired, "exponentiated.png")
      nine_root = GenerateImage.render_equation_copy(ctrl_obj, path_desired, "root.png")
      ten_evaluate = GenerateImage.render_equation_copy(ctrl_obj, path_desired, "evaluated.png")
      image_list = [one_add, two_subtract, three_multiply, four_divide, five_powered, six_differentiate, seven_integrate, eight_exponentiate, nine_root, ten_evaluate]
      rect = one_add.get_rect()
      i = 1
      for image in image_list:
         image.set_alpha(20)
      return(image_list)

   
   def update_controls(ctrl_obj, error, error_check, check_collision):
      dist_between_imgs_x = 100
      perched_imgs_where_y = 100
      k = 0
      m = 1
      for image in ctrl_obj.img_lst:
         j = str(m)
         text_control = font_cmu_rm.render(j, True, ColorsManual.medium_purple)
         text_control.set_alpha(125)
         text_control_pos = text_control.get_rect(x = (k*dist_between_imgs_x + 50), y = (perched_imgs_where_y - 50))
         image = pygame.transform.smoothscale_by(image, 0.5)
         rect = image.get_rect()
         window.blit(text_control, text_control_pos)
         rect.x = (50 + k*dist_between_imgs_x)
         rect.y = (perched_imgs_where_y)
         if(check_collision):
            image.set_alpha(255)
            ctrl_obj.ind_sh = True
         else:
            image.set_alpha(20)
            ctrl_obj.ind_sh = False
         window.blit(image, rect)
         k += 1
         m += 1
   
