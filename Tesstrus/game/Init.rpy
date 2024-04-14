#==========================================================================
# Картинки персонажей
#ВАЛЕРА
image Val Normal = "Characters/Val Normal.png" #Обыч
image Val Thoughtful = "Characters/Val Thoughtful.png" #Задум
image Val Hz = "Characters/Val Hz.png" #ХЗ
image Val Fight = "Characters/Val Fight.png" #Бой
image Val Strict = "Characters/Val Strict.png" #СТРОГ
image Val Pain = "Characters/Val Pain.png" #БОЛ
image Val Shy = "Characters/Val Shy.png" #СМУЩ
image Val Happy = "Characters/Val Happy.png" #ДОВ
image Val Honor = "Characters/Val Honor.png" #ЧЕСТЬ
image Val Rapture = "Characters/Val Rapture.png" #ВСОХ
image Val Fear = "Characters/Val Fear.png" #ИСПУГ
image Val Stick = "Characters/Val Stick.png" #ПАЛК
image Val Objection = "Characters/Joy Objection.png" #Objection!

#удалиьть
image Joy Normal = "Characters/Joy Normal.png"
image Joy Sad = "Characters/Joy Sad.png"
image Markiz Normal = "Characters/Markiz Normal.png"

#==========================================================================

# Определение персонажей игры.

define val = Character('Валерия', color="#f8d77b", image='Val')

#удалиьть
define m = Character('Маркиз', color="#665f37", image='Markiz')
define mn = Character('?', color="#665f37")
define j = Character('Джой', color="#f8d77b", image='Joy')
define jn = Character('?', color="#f8d77b")
define gg = Character('Я', color="#c07bf8")
define g = Character('Я', color="#c07bf8")

#==========================================================================

# Картинки фонов

#удалиьть
image bg_bedroom = im.Scale("Backgrounds/bg_bedroom.png", 1920, 1080)
image bg_street = im.Scale("Backgrounds/bg_street.png", 1920, 1080)
image end_alone = im.Scale("Ends/end_alone.png", 1920, 1080)
image end_burger = im.Scale("Ends/end_burger.png", 1920, 1080)
image end_dead = im.Scale("Ends/end_dead.png", 1920, 1080)
image end_domosed = im.Scale("Ends/end_domosed.png", 1920, 1080)
image end_happy = im.Scale("Ends/end_happy.png", 1920, 1080)


#==========================================================================
define fs = Character(None, kind=nvl) #Для вывода текста на весь экран

#==========================================================================
# Переменные
define BoolBurger = False #Взять ли бургер

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

#==========================================================================
#Слайдшоу меню
image menu_slideshow:
    im.Scale("Backgrounds/bg_bedroom.png", 1920, 1080) with dissolve
    pause 2.0
    im.Scale("images/Ends/end_happy.png", 1920, 1080) with dissolve
    pause 3.0
    im.Scale("images/Ends/end_alone.png", 1920, 1080) with dissolve
    pause 3.0
    im.Scale("images/Ends/end_domosed.png", 1920, 1080) with dissolve
    pause 3.0
    repeat
#==========================================================================
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