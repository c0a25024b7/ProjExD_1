import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bgflip_img = bg_img
    bgflip_img = pg.transform.flip(bgflip_img,True,False)
    fly_img = pg.image.load("fig/3.png")#練習３
    fly_img = pg.transform.flip(fly_img ,True ,False)#練習３
    fly_rct = fly_img.get_rect() # 練習１０ー１
    fly_rct.center =300 ,200 #練習１０－２
    tmr = 0
    y = -1
    z = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        x = tmr%3200
        screen.blit(bg_img, [-x, 0])
        screen.blit(bgflip_img, [-x+1600, 0])
        screen.blit(bg_img, [-x+3200, 0])
        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_UP]:
            z = -1
        if key_lst[pg.K_DOWN]:
            z = 1
        if key_lst[pg.K_LEFT]:
            y = -2
        if key_lst[pg.K_RIGHT]:
            y = 1
        fly_rct.move_ip((y, z))
        screen.blit(fly_img,fly_rct)
        pg.display.update()
        tmr += 1        
        y = -1
        z = 0
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()