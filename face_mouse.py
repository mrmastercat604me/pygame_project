import pygame,math

def face_mouse(image,image_rect,correction_angle,surface):
    mx, my = pygame.mouse.get_pos()
    dx,dy =  mx - image_rect.centerx, my - image_rect.centery
    angle =  math.degrees(math.atan2(-dy, dx)) - correction_angle
    rot_image = pygame.transform.rotate(image,angle)
    rot_image_rect = rot_image.get_rect(center = image_rect.center)
    surface.blit(rot_image,rot_image_rect.topleft)
