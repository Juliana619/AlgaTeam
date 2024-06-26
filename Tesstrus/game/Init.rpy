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
image Val Objection = "Characters/Val Objection.png" #Objection!

#ПОДРУГА ВАЛЕРЫ
image Valp Normal = "Characters/Valp Normal.png"  #Обыч
image Valp Zam = "Characters/Valp Zam.png" #Зам

#РАСКОМЕНТИРОВАТЬ КОГДА БУДУТ КАРТИНКИ
#Рикс
image Rix = "Characters/Rix Normal.png"

#Панда
image Panda Normal = "Characters/Panda Normal.png"  #Обыч
image Panda Cry = "Characters/Panda Cry.png" #Плач

#Рыбка
image Fish Normal = "Characters/Fish Normal.png"  #Обыч
image Fish Sad = "Characters/Fish Sad.png" #Плач

#Остин
image Ostin Normal = "Characters/Ostin Normal.png" #Норм
image Ostin Evil = "Characters/Ostin Evil.png" #Злой

#Мужик с ФС
image Man Sad = "Characters/Man Sad.png" #Грусть
image Man Cry = "Characters/Man Cry.png" #Плач

#ЕНОТ
image Rac Happy = "Characters/Rac Happy.png" #Радостный
image Rac Worr = "Characters/Rac Worr.png" #Тревожный


#КОРОЛЬ
image King Freez = "Characters/King Freez.png" #Замор
image King Happy = "Characters/King Happy.png" #Счаст
image King Surp = "Characters/King Surp.png" #Удив

#КОРОЛЬ РМ
image KRM Sad = "Characters/KRM Sad.png"
image KRM Evil = "Characters/KRM Evil.png"
image KRM Happy = "Characters/KRM Happy.png"

#ДВОРЕЦКИЙ
image DRM Normal = "Characters/DRM Normal.png"

#удалиьть
image Joy Normal = "Characters/Joy Normal.png"
image Joy Sad = "Characters/Joy Sad.png"
image Markiz Normal = "Characters/Markiz Normal.png"

#==========================================================================

# Определение персонажей игры.

define val = Character('Валерия', color="#f8d77b", image='Val')
define valp = Character('Зоя', color="#48d198", image='Valp')
define rixnone = Character('Голос', color="#ffffff", image=None)
define rix = Character('Дракон', color="#0e6415", image='Rix')
define panda = Character('Красная панда', color="#0e6415", image='Panda')
define fish = Character('Рыбка', color="#6116c4", image='Fish')
define ostin = Character('Садовник', color="#ee2e2e", image='Ostin')
define man = Character('Мужчина', color="#6384cc", image='Man')
define rac = Character('Енот', color="#666970", image='Rac')
define king = Character('Король', color="#f8e53a", image='King')
define drm = Character('Дворецкий', color="#921818", image='DRM')
define krm = Character('Король Эрэм', color="#7b0c8a", image='KRM')

define ulik = Character('Ульяна', color="#de8ee9")
define mari = Character('Мария', color="#f8a4c7")

define incognito = Character('?', color="#ffffff")
#удалиьть
define m = Character('Маркиз', color="#665f37", image='Markiz')
define mn = Character('?', color="#665f37")
define j = Character('Джой', color="#f8d77b", image='Joy')
define jn = Character('?', color="#f8d77b")
define gg = Character('Я', color="#c07bf8")
define g = Character('Я', color="#c07bf8")

#==========================================================================

# Картинки фонов
image bg_bedroom = im.Scale("Backgrounds/bg_bedroom.png", 1920, 1080)
image bg_street = im.Scale("Backgrounds/bg_street.png", 1920, 1080)
image bg_fishdom = im.Scale("Backgrounds/bg_fishdom.png", 1920, 1080)
image bg_gardenscapes = im.Scale("Backgrounds/bg_gardenscapes.png", 1920, 1080)
image bg_palace = im.Scale("Backgrounds/bg_palace.png", 1920, 1080)
image bg_wildscapes = im.Scale("Backgrounds/bg_wildscapes.png", 1920, 1080)
image bg_goldhunter = im.Scale("Backgrounds/bg_goldhunter.png", 1920, 1080)
image bg_royaloutside = im.Scale("Backgrounds/bg_royaloutside.png", 1920, 1080)
image bg_familyscapes = im.Scale("Backgrounds/bg_familyscapes.png", 1920, 1080)
image bg_gardenscapes_house = im.Scale("Backgrounds/bg_gardenscapes_house.png", 1920, 1080)

# Картинки концовок
image end_lostopportunity = im.Scale("Ends/end_lostopportunity.png", 1920, 1080)
image end_doggi = im.Scale("Ends/end_doggi.png", 1920, 1080)
image end_dream = im.Scale("Ends/end_dream.png", 1920, 1080)
image end_heroes = im.Scale("Ends/end_heroes.png", 1920, 1080)
image end_paradise = im.Scale("Ends/end_paradise.png", 1920, 1080)
image end_part = im.Scale("Ends/end_part.png", 1920, 1080)
image end_slave = im.Scale("Ends/end_slave.png", 1920, 1080)
image end_stay = im.Scale("Ends/end_stay.png", 1920, 1080)

#==========================================================================
define fs = Character(None, kind=nvl) #Для вывода текста на весь экран

#==========================================================================
# Переменные
define wildchip = False
define fishchip = False
define familychip = False
define gardenchip = False
define goldhunterchip = False
define chipcount = 0


define audio.heroes = "audio/Hackathon Heroes.mp3"
define audio.Family = "audio/Family.mp3"
define audio.Ends = "audio/Ends.mp3"
define audio.Fight = "audio/Fight.mp3"
define audio.Fishdom = "audio/Fishdom.mp3"
define audio.Garden = "audio/Garden.mp3"
define audio.Goldh = "audio/Goldh.mp3"
define audio.RoyalMatch = "audio/RoyalMatch.mp3"
define audio.Start = "audio/Start.mp3"
define audio.Wildscapes = "audio/Wildscapes.mp3"



# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

#==========================================================================
#Слайдшоу меню
image menu_slideshow:
    im.Scale("Backgrounds/bg_bedroom.png", 1920, 1080) with dissolve
    pause 2.0
    #im.Scale("images/Ends/end_happy.png", 1920, 1080) with dissolve
    #pause 3.0
    #im.Scale("images/Ends/end_alone.png", 1920, 1080) with dissolve
    #pause 3.0
    #im.Scale("images/Ends/end_domosed.png", 1920, 1080) with dissolve
    #pause 3.0
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