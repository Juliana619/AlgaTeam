image Joy Normal = "Characters/Joy Normal.png"
image Joy Sad = "Characters/Joy Sad.png"
image Markiz Normal = "Characters/Markiz Normal.png"

image bg_bedroom = im.Scale("Backgrounds/bg_bedroom.png", 1920, 1080)
image bg_street = im.Scale("Backgrounds/bg_street.png", 1920, 1080)
image end_alone = im.Scale("Ends/end_alone.png", 1920, 1080)
image end_burger = im.Scale("Ends/end_burger.png", 1920, 1080)
image end_dead = im.Scale("Ends/end_dead.png", 1920, 1080)
image end_domosed = im.Scale("Ends/end_domosed.png", 1920, 1080)
image end_happy = im.Scale("Ends/end_happy.png", 1920, 1080)
# Определение персонажей игры.
define m = Character('Маркиз', color="#665f37", image='Markiz')
define mn = Character('?', color="#665f37")
define j = Character('Джой', color="#f8d77b", image='Joy')
define jn = Character('?', color="#f8d77b")
define gg = Character('Я', color="#c07bf8")
define g = Character('Я', color="#c07bf8")
# $ mtest = Character('test', window_left_padding=270, show_side_image=Image("Characters/Markiz Normal.png", xalign=0.0, yalign=1.0), color="#00cc66", what_color="#00ffcc", who_drop_shadow=[ (2, 1) ,(3, 2), (4, 3), (5, 4), (6, 5) ], who_drop_shadow_color="#006666" ). 
define fs = Character(None, kind=nvl) #Для вывода текста на весь экран

# Переменные
define BoolBurger = False #Взять ли бургер

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

#Слайдшоу меню
image menu_slideshow:
    im.Scale("Backgrounds/bg_bedroom.png", 1920, 1080)
    pause 3.0
    "images/Ends/end_happy.png"
    pause 3.0
    "images/Ends/end_alone.png"
    pause 3.0
    "images/Ends/end_alone.png"
    pause 3.0
    "images/Ends/end_domosed.png"
    pause 3.0
    repeat

#ЭКРАН ЗАГРУЗКИ?
label splashscreen:
    # отображаем чёрный экран
    scene black with dissolve
    # мелодия, которую мы хотим проиграть перед лого. Помните, что лучше выставить громкость по умолчанию пониже, чтобы для игрока этот звук не оказался слишком громким 
    # play sound splashscreen fadein 0.5
    #пауза перед отображением лого 
    pause 0.5 
    #отображение лого с позиционированием по экрану
    show image "UI/Logo.png" with dissolve:
        xalign 0.5 ypos 100
    pause 4
    hide image "UI/Logo.png" with dissolve
    #останавливаем звук, чтобы при пропуске, например, он не продолжал играть в главном меню
    #stop sound fadeout 2.0 
    pause 1
    return #чтобы закончить label splashscreen