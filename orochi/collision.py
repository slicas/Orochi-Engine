import pyray as pr
from orochi.object import Object,CollisionBody
from orochi.tag import Tag
from math import *
from orochi.math import Ellipse
from orochi.dir import *
import math




def ellipse_rectangle_collision(ellipse_center, ellipse_radius_x, ellipse_radius_y, rect_position, rect_width, rect_height):
    dx = abs(ellipse_center[0] - (rect_position[0] + rect_width / 2))
    dy = abs(ellipse_center[1] - (rect_position[1] + rect_height / 2))
    if dx > ellipse_radius_x + rect_width / 2:
        return False
    if dy > ellipse_radius_y + rect_height / 2:
        return False
    if dx <= rect_width / 2:
        return True
    if dy <= rect_height / 2:
        return True
    corner_dist_sq = (dx - rect_width / 2) ** 2 + (dy - rect_height / 2) ** 2
    return corner_dist_sq <= ellipse_radius_x ** 2

def ellipse_collision(ellipse1_center, ellipse1_radius_x, ellipse1_radius_y, ellipse2_center, ellipse2_radius_x, ellipse2_radius_y):
    dx = ellipse2_center[0] - ellipse1_center[0]
    dy = ellipse2_center[1] - ellipse1_center[1]

    distance = math.sqrt((dx ** 2) / ((ellipse1_radius_x + ellipse2_radius_x) ** 2) + (dy ** 2) / ((ellipse1_radius_y + ellipse2_radius_y) ** 2))

    return distance <= 1



def body_collide_with(body1 : CollisionBody,body2 : CollisionBody):
    b1 = body1.body
    b2 = body2.body
    match(body1.get_type(),body2.get_type()):
        case ("QUAD","QUAD"):
            return pr.check_collision_recs(b1,b2)
        case("ELLIPSE","QUAD"):
            return ellipse_rectangle_collision((b1.center_x,b1.center_y),b1.radius_x,b1.radius_y,(b2.x,b2.y),b2.width,b2.height)
        case("QUAD","ELLIPSE"):
            return ellipse_rectangle_collision((b2.center_x,b2.center_y),b2.radius_x,b2.radius_y,(b1.x,b1.y),b1.width,b1.height)
        case("ELLIPSE","ELLIPSE"):
            return ellipse_collision((b1.center_x,b1.center_y),b1.radius_x,b1.radius_y,(b2.center_x,b2.center_y),b2.radius_x,b2.radius_y)

def body_collide_with_ex(body1 : CollisionBody,body2 : CollisionBody,b1_x_shift = 0,b1_y_shift = 0,b1_width_shift = 0,b1_height_shift = 0,b2_x_shift = 0,b2_y_shift = 0,b2_width_shift = 0,b2_height_shift = 0,b1_xradius_shift = 0,b1_yradius_shift = 0,b2_xradius_shift = 0,b2_yradius_shift = 0,debug = False):
    b1 = pr.Rectangle(body1.x + b1_x_shift - (b1_width_shift*body1.origin),body1.y + b1_y_shift - (b1_height_shift*body1.origin),body1.width + b1_width_shift,body1.height + b1_height_shift) if body1.get_type() == "QUAD" else Ellipse(body1.x + b1_x_shift,body1.y + b1_y_shift,body1.radius_x + b1_xradius_shift,body1.radius_y + b1_yradius_shift)
    b2 = pr.Rectangle(body2.x + b2_x_shift - (b2_width_shift*body2.origin),body2.y + b2_y_shift - (b2_height_shift*body2.origin),body2.width + b2_width_shift,body2.height + b2_height_shift) if body2.get_type() == "QUAD" else Ellipse(body2.x + b2_x_shift,body2.y + b2_y_shift,body2.radius_x + b2_xradius_shift,body2.radius_y + b2_yradius_shift)
    if(debug):
        if(body1.get_type() == "QUAD"):
            pr.draw_rectangle_lines_ex(pr.Rectangle(b1.x - 1,b1.y - 1,b1.width + 2,b1.height + 2),2,(252, 5, 252,255))
        else:
            pr.draw_ellipse_lines(b1.center_x,b1.center_y,b1.radius_x + 1,b1.radius_y+1,(252, 5, 252,255))
        if(body2.get_type() == "QUAD"):
            pr.draw_rectangle_lines_ex(pr.Rectangle(b2.x - 1,b2.y - 1,b2.width + 2,b2.height + 2),2,(252, 5, 252,255))
        else:
            pr.draw_ellipse_lines(b2.center_x,b2.center_y,b2.radius_x + 1,b2.radius_y+1,(252, 5, 252,255))


    match(body1.get_type(),body2.get_type()):
        case ("QUAD","QUAD"):
            return pr.check_collision_recs(b1,b2)
        case("ELLIPSE","QUAD"):
            return ellipse_rectangle_collision((b1.center_x,b1.center_y),b1.radius_x,b1.radius_y,(b2.x,b2.y),b2.width,b2.height)
        case("QUAD","ELLIPSE"):
            return ellipse_rectangle_collision((b2.center_x,b2.center_y),b2.radius_x,b2.radius_y,(b1.x,b1.y),b1.width,b1.height)
        case("ELLIPSE","ELLIPSE"):
            return ellipse_collision((b1.center_x,b1.center_y),b1.radius_x,b1.radius_y,(b2.center_x,b2.center_y),b2.radius_x,b2.radius_y)
        

def object_meeting(object1 : object,object2 : object,debug = False):
    body1 = pr.Rectangle((object1.x)-(object1.width*object1.origin),(object1.y )-(object1.height*object1.origin),object1.width ,object1.height )
    body2 = pr.Rectangle((object2.x)-(object2.width*object2.origin),(object2.y)-(object2.height*object2.origin),object2.width,object2.height)
    if(debug):
        pr.draw_rectangle_lines(int(body1.x - 1),int(body1.y - 1),int(body1.width + 2),int(body1.height + 2),(252, 5, 252,255))
        pr.draw_rectangle_lines(int(body2.x - 1),int(body2.y - 1),int(body2.width + 2),int(body2.height + 2),(252, 5, 252,255))
    return pr.check_collision_recs(body1,body2)


def tag_meeting_detail(tag1 : Tag,tag2 : Tag,debug = False):
    collisions = []
    for object1 in tag1.get_objects():
        body1 = pr.Rectangle(object1.x ,object1.y ,object1.width ,object1.height )
        for object2 in tag2.get_objects():
            body2 = pr.Rectangle(object2.x,object2.y,object2.width,object2.height)
            if(debug):
                pr.draw_rectangle_lines(int(body1.x - 1),int(body1.y - 1),int(body1.width + 2),int(body1.height + 2),(252, 5, 252,255))
                pr.draw_rectangle_lines(int(body2.x - 1),int(body2.y - 1),int(body2.width + 2),int(body2.height + 2),(252, 5, 252,255))
            if pr.check_collision_recs(body1,body2):
                collisions.append({"object1":object1,"object2":object2})
    return collisions

def tag_meeting(tag1 : Tag,tag2 : Tag,debug = False):
    for object1 in tag1.get_objects():
        body1 = pr.Rectangle((object1.x )-(object1.width*object1.origin),(object1.y )-(object1.height*object1.origin),object1.width ,object1.height )
        for object2 in tag2.get_objects():
            body2 = pr.Rectangle((object2.x )-(object2.width*object2.origin),(object2.y)-(object2.height*object2.origin),object2.width,object2.height)
            if(debug):
                pr.draw_rectangle_lines(int(body1.x - 1),int(body1.y - 1),int(body1.width + 2),int(body1.height + 2),(252, 5, 252,255))
                pr.draw_rectangle_lines(int(body2.x - 1),int(body2.y - 1),int(body2.width + 2),int(body2.height + 2),(252, 5, 252,255))
            if pr.check_collision_recs(body1,body2):
                return True
def tag_meeting_near_detail(tag1 : Tag,tag2 : Tag,x,y,debug = False):
    collisions = []
    for object1 in tag1.get_objects():
        body1 = pr.Rectangle((object1.x  + x)-(object1.width*object1.origin),(object1.y  + y)-(object1.height*object1.origin),object1.width ,object1.height )
        for object2 in tag2.get_objects():
           
            body2 = pr.Rectangle((object2.x )-(object2.width*object2.origin),(object2.y)-(object2.height*object2.origin),object2.width,object2.height)
            if(debug):
                pr.draw_rectangle_lines(int(body1.x - 1),int(body1.y - 1),int(body1.width + 2),int(body1.height + 2),(252, 5, 252,255))
                pr.draw_rectangle_lines(int(body2.x - 1),int(body2.y - 1),int(body2.width + 2),int(body2.height + 2),(252, 5, 252,255))
            if pr.check_collision_recs(body1,body2):
                collisions.append({"object1":object1,"object2":object2})
    return collisions
def tag_meeting_near(tag1 : Tag,tag2 : Tag,x,y,debug = False):
    for object1 in tag1.get_objects():
        body1 = pr.Rectangle((object1.x  + x)-(object1.width*object1.origin),(object1.y  + y)-(object1.height*object1.origin),object1.width ,object1.height )
        for object2 in tag2.get_objects():    
            body2 = pr.Rectangle((object2.x )-(object2.width*object2.origin),(object2.y)-(object2.height*object2.origin),object2.width,object2.height)
            if(debug):
                pr.draw_rectangle_lines(int(body1.x - 1),int(body1.y - 1),int(body1.width + 2),int(body1.height + 2),(252, 5, 252,255))
                pr.draw_rectangle_lines(int(body2.x - 1),int(body2.y - 1),int(body2.width + 2),int(body2.height + 2),(252, 5, 252,255))
            if pr.check_collision_recs(body1,body2):
                return True
            
def object_near(object1 : object,object2 : object,x : int,y : int,debug =  False):
    body1 = pr.Rectangle((object1.x  + x)-(object1.width*object1.origin),(object1.y  + y)-(object1.height*object1.origin),object1.width ,object1.height )
    body2 = pr.Rectangle((object2.x )-(object2.width*object2.origin),(object2.y)-(object2.height*object2.origin),object2.width,object2.height)
    if(debug):
        pr.draw_rectangle_lines(int(body1.x - 1),int(body1.y - 1),int(body1.width + 2),int(body1.height + 2),(252, 5, 252,255))
        pr.draw_rectangle_lines(int(body2.x - 1),int(body2.y - 1),int(body2.width + 2),int(body2.height + 2),(252, 5, 252,255))
    return pr.check_collision_recs(body1,body2)
