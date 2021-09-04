"""
File: my_drawing.py
Name: Husan Tung, Lin
----------------------
The function draws a face by using GObject(GOval, GRect, GLabel, GPolygon, GArc) and Gwindow.
"""

from campy.graphics.gobjects import GOval, GRect, GLabel, GPolygon, GArc
from campy.graphics.gwindow import GWindow

window = GWindow(800, 400, title='Cute Emoji')


def main():
    """
    I pick three cute emojis(sunglasses, mask and zipper mouth face) from iOS system and try to draw them.
    """
    emoji1()
    emoji2()
    emoji3()
    labels()


def emoji1():
    """
    Sunglasses
    component: face + mouse + sunglasses + reflection
    """
    # face
    face = GOval(200, 200)
    face.filled = True
    face.color = 'gold'
    face.fill_color = 'gold'
    window.add(face, x=50, y=40)
    # mouse
    mouse_bottom = GOval(90, 90)
    mouse_bottom.filled = True
    window.add(mouse_bottom, x=105, y=105)
    mouse_upper = GOval(92, 92)
    mouse_upper.filled = True
    mouse_upper.color = 'gold'
    mouse_upper.fill_color = 'gold'
    window.add(mouse_upper, x=104, y=100)
    # sunglasses (left, right, central)
    left_upper_glass = GOval(90, 10)
    left_upper_glass.filled = True
    window.add(left_upper_glass, x=57, y=100)
    left_glass = GPolygon()
    left_glass.add_vertex((57, 105))
    left_glass.add_vertex((148, 105))
    left_glass.add_vertex((142, 150))
    left_glass.add_vertex((63, 150))
    left_glass.filled = True
    window.add(left_glass)
    left_glass_bottom = GOval(78, 10)
    left_glass_bottom.filled = True
    window.add(left_glass_bottom, x=63, y=145)

    right_upper_glass = GOval(90, 10)
    right_upper_glass.filled = True
    window.add(right_upper_glass, x=153, y=100)
    right_glass = GPolygon()
    right_glass.add_vertex((153, 105))
    right_glass.add_vertex((242, 105))
    right_glass.add_vertex((238, 150))
    right_glass.add_vertex((159, 150))
    right_glass.filled = True
    window.add(right_glass)
    right_glass_bottom = GOval(78, 10)
    right_glass_bottom.filled = True
    window.add(right_glass_bottom, x=159, y=145)

    central_sun_glass = GRect(20, 7)
    central_sun_glass.filled = True
    window.add(central_sun_glass, x=142, y=104)
    # reflection (left, right)
    reflection_l = GOval(80, 5)
    reflection_l.filled = True
    reflection_l.fill_color = 'gray'
    reflection_l.color = 'gray'
    window.add(reflection_l, 62, 107)
    reflection_l = GOval(80, 5)
    reflection_l.filled = True
    window.add(reflection_l, 62, 109.5)

    reflection_r = GOval(80, 5)
    reflection_r.filled = True
    reflection_r.fill_color = 'gray'
    reflection_r.color = 'gray'
    window.add(reflection_r, 156, 107)
    reflection_r = GOval(80, 5)
    reflection_r.filled = True
    window.add(reflection_r, 156, 109.5)
    return face, mouse_upper, mouse_bottom, left_glass, left_glass_bottom, left_upper_glass, \
           right_glass, right_glass_bottom, right_upper_glass, central_sun_glass, reflection_l, reflection_r


def emoji2():
    """
    Mask
    component: face + eyebrows + eyes + cheek + mask
    """
    # face
    face = GOval(200, 200)
    face.filled = True
    face.color = 'gold'
    face.fill_color = 'gold'
    window.add(face, x=300, y=40)
    # eyebrows (left, right)
    eyebrow_l = GArc(60, 60, 40, 130)
    eyebrow_l.filled = True
    window.add(eyebrow_l, x=335, y=97)
    eyebrow_l_bottom = GArc(60, 60, 40, 130)
    eyebrow_l_bottom.filled = True
    eyebrow_l_bottom.color = 'gold'
    eyebrow_l_bottom.fill_color = 'gold'
    window.add(eyebrow_l_bottom, x=335, y=101)

    eyebrow_r = GArc(70, 60, 20, 110)
    eyebrow_r.filled = True
    window.add(eyebrow_r, x=415, y=97)
    eyebrow_r_bottom = GArc(70, 60, 20, 110)
    eyebrow_r_bottom.filled = True
    eyebrow_r_bottom.color = 'gold'
    eyebrow_r_bottom.fill_color = 'gold'
    window.add(eyebrow_r_bottom, x=416, y=101)
    # eyes (left, right)
    eye_l = GArc(50, 50, 40, 130)
    eye_l.filled = True
    window.add(eye_l, x=350, y=127)
    eye_l_bottom = GArc(50, 50, 40, 130)
    eye_l_bottom.filled = True
    eye_l_bottom.color = 'gold'
    eye_l_bottom.fill_color = 'gold'
    window.add(eye_l_bottom, x=350, y=131)

    eye_r = GArc(56, 48, 20, 110)
    eye_r.filled = True
    window.add(eye_r, x=410, y=127)
    eye_r_bottom = GArc(56, 48, 20, 110)
    eye_r_bottom.filled = True
    eye_r_bottom.color = 'gold'
    eye_r_bottom.fill_color = 'gold'
    window.add(eye_r_bottom, x=410, y=131)
    # cheek (left and right)
    cheek_l = GOval(50, 30)
    cheek_l.filled = True
    cheek_l.color = 'peachpuff'
    cheek_l.fill_color = 'peachpuff'
    window.add(cheek_l, x=310, y=130)

    cheek_r = GOval(50, 30)
    cheek_r.filled = True
    cheek_r.color = 'peachpuff'
    cheek_r.fill_color = 'peachpuff'
    window.add(cheek_r, x=440, y=130)
    # mask (mask + line1234)
    mask = GRect(100, 60)
    mask.filled = True
    mask.fill_color = 'snow'
    mask.color = 'snow'
    window.add(mask, 352, 142)

    mask_line1 = GPolygon()
    mask_line1.add_vertex((309, 188))
    mask_line1.add_vertex((400, 188))
    mask_line1.add_vertex((400, 193))
    mask_line1.add_vertex((313, 193))
    mask_line1.filled = True
    mask_line1.fill_color = 'snow'
    mask_line1.color = 'snow'
    window.add(mask_line1)

    mask_line2 = GPolygon()
    mask_line2.add_vertex((450, 188))
    mask_line2.add_vertex((490, 188))
    mask_line2.add_vertex((490, 193))
    mask_line2.add_vertex((447, 193))
    mask_line2.filled = True
    mask_line2.fill_color = 'snow'
    mask_line2.color = 'snow'
    window.add(mask_line2)

    mask_line3 = GPolygon()
    mask_line3.add_vertex((355, 155))
    mask_line3.add_vertex((300, 127))
    mask_line3.add_vertex((300, 122))
    mask_line3.add_vertex((355, 150))
    mask_line3.filled = True
    mask_line3.fill_color = 'snow'
    mask_line3.color = 'snow'
    window.add(mask_line3)

    mask_line4 = GPolygon()
    mask_line4.add_vertex((450, 155))
    mask_line4.add_vertex((500, 127))
    mask_line4.add_vertex((500, 122))
    mask_line4.add_vertex((450, 150))
    mask_line4.filled = True
    mask_line4.fill_color = 'snow'
    mask_line4.color = 'snow'
    window.add(mask_line4)
    return face, eye_l, eye_r, eyebrow_l, eyebrow_r, cheek_l, cheek_r, \
           mask, mask_line1, mask_line2, mask_line3, mask_line4


def emoji3():
    """
    Zipper mouth face
    component: face + eyes + mouth + zipper
    """
    # face
    face = GOval(200, 200)
    face.filled = True
    face.color = 'gold'
    face.fill_color = 'gold'
    window.add(face, x=550, y=40)
    # eyes(left, right)
    left_eye = GOval(15, 24)
    left_eye.filled = True
    left_eye.color = 'saddlebrown'
    left_eye.fill_color = 'saddlebrown'
    window.add(left_eye, x=610, y=110)

    right_eye = GOval(15, 24)
    right_eye.filled = True
    right_eye.color = 'saddlebrown'
    right_eye.fill_color = 'saddlebrown'
    window.add(right_eye, x=675, y=110)
    # mouth
    line = GRect(100, 5)
    line.filled = True
    line.fill_color = 'saddlebrown'
    line.color = 'saddlebrown'
    window.add(line, x=600, y=170)
    # zipper(zipper, zipper123456789, zipper_hole12)
    zipper1 = GRect(10, 15)
    zipper1.filled = True
    zipper1.color = 'darkgray'
    zipper1.fill_color = 'gray'
    window.add(zipper1, x=610, y=170)

    zipper2 = GRect(10, 15)
    zipper2.filled = True
    zipper2.color = 'darkgray'
    zipper2.fill_color = 'gray'
    window.add(zipper2, x=620, y=160)

    zipper3 = GRect(10, 15)
    zipper3.filled = True
    zipper3.color = 'darkgray'
    zipper3.fill_color = 'gray'
    window.add(zipper3, x=630, y=170)

    zipper4 = GRect(10, 15)
    zipper4.filled = True
    zipper4.color = 'darkgray'
    zipper4.fill_color = 'gray'
    window.add(zipper4, x=640, y=160)

    zipper5 = GRect(10, 15)
    zipper5.filled = True
    zipper5.color = 'darkgray'
    zipper5.fill_color = 'gray'
    window.add(zipper5, x=650, y=170)

    zipper6 = GRect(10, 15)
    zipper6.filled = True
    zipper6.color = 'darkgray'
    zipper6.fill_color = 'gray'
    window.add(zipper6, x=660, y=160)

    zipper7 = GRect(10, 15)
    zipper7.filled = True
    zipper7.color = 'darkgray'
    zipper7.fill_color = 'gray'
    window.add(zipper7, x=670, y=170)

    zipper8 = GRect(10, 15)
    zipper8.filled = True
    zipper8.color = 'darkgray'
    zipper8.fill_color = 'gray'
    window.add(zipper8, x=680, y=160)

    zipper = GPolygon()
    zipper.add_vertex((686, 177.5))
    zipper.add_vertex((706, 168))
    zipper.add_vertex((726, 205))
    zipper.add_vertex((702, 217))
    zipper.filled = True
    zipper.fill_color = 'gray'
    zipper.color = 'darkgray'
    window.add(zipper)

    zipper_hole1 = GArc(22, 25, 30, 180)
    zipper_hole1.filled = True
    zipper_hole1.fill_color = 'gold'
    zipper_hole1.color = 'darkgray'
    window.add(zipper_hole1, 692, 175)

    zipper_hole2 = GArc(25, 25, 210, 180)
    zipper_hole2.filled = True
    zipper_hole2.fill_color = 'gold'
    zipper_hole2.color = 'darkgray'
    window.add(zipper_hole2, 696, 190)

    zipper9 = GPolygon()
    zipper9.add_vertex((691, 173))
    zipper9.add_vertex((696, 169))
    zipper9.add_vertex((701, 175))
    zipper9.add_vertex((696, 179))
    zipper9.filled = True
    zipper9.fill_color = 'gray'
    zipper9.color = 'darkgray'
    window.add(zipper9)

    return face, left_eye, right_eye, line, zipper1, zipper2, zipper3, zipper4\
        , zipper5, zipper6, zipper7, zipper8, zipper9, zipper, zipper_hole1, zipper_hole2


def labels():
    """
    add some words
    """
    sunglasses = GLabel('SUNGLASSES')
    sunglasses.font = '-20'
    window.add(sunglasses, x=68, y=300)

    mask = GLabel('MASK')
    mask.font = '-20'
    window.add(mask, x=365, y=300)

    zipper_mouth_face = GLabel('ZIPPER')
    zipper_mouth_face.font = '-20'
    window.add(zipper_mouth_face, x=610, y=300)
    zipper_mouth_face2 = GLabel('MOUTH FACE')
    zipper_mouth_face2.font = '-20'
    window.add(zipper_mouth_face2, x=570, y=330)

    emoji = GLabel('~EMOJI~')
    emoji.font = '-30'
    window.add(emoji, x=320, y=380)
    return sunglasses, mask, zipper_mouth_face, zipper_mouth_face2, emoji



if __name__ == '__main__':
    main()
