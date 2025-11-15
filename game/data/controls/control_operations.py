from game.modules.base_modules import *
from game.modules.preloads import *
from game.modules.generateimage import GenerateImage
class ControlOperations:
   def controls(equation_object):
      path_desired = "game/images/operations/"
      one_add = GenerateImage.render_equation_copy(equation_object, path_desired, "addition.png")
      two_subtract = GenerateImage.render_equation_copy(equation_object, path_desired, "subtraction.png")
      three_multiply = GenerateImage.render_equation_copy(equation_object, path_desired, "multiplication.png")
      four_divide = GenerateImage.render_equation_copy(equation_object, path_desired, "division.png")
      five_powered = GenerateImage.render_equation_copy(equation_object, path_desired, "powerof.png")
      six_differentiate = GenerateImage.render_equation_copy(equation_object, path_desired, "derivative.png")
      seven_integrate = GenerateImage.render_equation_copy(equation_object, path_desired, "integral.png")
      eight_exponentiate = GenerateImage.render_equation_copy(equation_object, path_desired, "exponentiated.png")
      nine_root = GenerateImage.render_equation_copy(equation_object, path_desired, "root.png")
      ten_evaluate = GenerateImage.render_equation_copy(equation_object, path_desired, "evaluated.png")
      image_list = [one_add, two_subtract, three_multiply, four_divide, five_powered, six_differentiate, seven_integrate, eight_exponentiate, nine_root, ten_evaluate]
      rect = one_add.get_rect()
      i = 1
      text_image_list = []
      text_image_pos_list = []
      for image in image_list:
         image.set_alpha(20)
         j = str(i)
         i += 1
         text_image = font_cmu_bld.render(j, True, (255, 255, 255))
         text_image_pos = text_image.get_rect(x = (rect.x), y = rect.y + i*200)
         text_image_list.append(text_image)
         text_image_pos_list.append(text_image_pos)
      return(image_list, text_image_list, text_image_pos_list)
   
   def update_controls(image_list, text_image_list, text_image_pos_list, error, error_check, check_collision):
      dist_between_imgs_x = 100
      perched_imgs_where_y = 100
      k = 0
      m = 1
      text_control = font_cmu_rm.render("", True, (255, 0, 0))
      text_control_pos = text_control.get_rect(x = (width//2 - 300), y = (height - 200))
      
      for image in image_list:
         j = str(m)
         text_control = font_cmu_rm.render(j, True, ColorsManual.medium_purple)
         text_control.set_alpha(125)
         text_control_pos = text_control.get_rect(x = (k*dist_between_imgs_x + 50), y = (perched_imgs_where_y - 50))
         image = pygame.transform.smoothscale_by(image, 0.5)
         rect = image.get_rect()
         window.blit(text_control, text_control_pos)
         rect.x = (50 + k*dist_between_imgs_x)
         rect.y = (perched_imgs_where_y)
         text_image = text_image_list[k]
         text_image_pos = text_image_pos_list[k] 
         if(check_collision):
            image.set_alpha(255)
            error_check = False
         else:
            image.set_alpha(20) 
         window.blit(image, rect)
         k += 1
         m += 1

