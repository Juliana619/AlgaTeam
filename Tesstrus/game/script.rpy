﻿# Вы можете расположить сценарий своей игры в этом файле.


# Поменять только на одну реплику j @ Normal "хаппи хаппи хаппи" 

# Игра начинается здесь:
label start:
    #Разные положения для персонажей:
    transform centerm:
        xalign 0.5
        yalign -0.5
    transform rightm:
        xalign 0.9
        yalign -0.5
    transform leftm:
        xalign 0.1
        yalign -0.5
    transform centerz:
        xalign 0.5
        yalign 0.9
    transform centerf:
        xalign 0.5
        yalign 0.4
    #Погнали
    scene bg_street with Dissolve(.5)
    stop music fadeout 1
    play music Start
    "После нескольких дней бесконечных дождей солнечный и теплый день казался настоящей наградой."
    "Идеально, чтобы лениться или вздыхать на нежелание заниматься важными задачами."
    "Если, конечно, нет других проблем…"
    show Valp Zam at rightm with easeinright
    valp Zam "Лер, ты меня совсем не слушаешь. Что происходит?"
    show Val Pain at leftm with easeinleft
    val "Нет-нет, всё в порядке. Извини, просто выпала немного."
    valp Zam "Ладно, по-другому спрошу. Что у тебя случилось? Ты последнее время какая-то потерянная."
    val Thoughtful "Не знаю как это объяснить...Но в какой-то момент я начала слышать голос на фоне. И это не метафора, буквально незнакомый голос постоянно в моей голове."
    val Normal "Уже даже не помню как давно это продолжается. Кажется, будто он всегда был со мной."
    valp Normal "Так... И что он хочет от тебя?"
    val Hz "Эээ, да я не знаю, как-то никогда к нему не прислушивалась."
    valp Zam "То есть, ты просто терпишь этот шум в голове? Может, стоит ему попробовать ответить?"
    val Thoughtful "Не думала об этом… И ты удивительно легко приняла эту информацию, но ладно, стоит попробовать."

    #смена локации на дом или тип того
    scene bg_bedroom
    with Dissolve(.5)
    show Val Thoughtful at centerm with easeinleft
    val Thoughtful "{i}Окей, голос в голове, что мне с тобой делать… {/i}"
    menu:
        "Поговорить" :
            jump TalkWithDragon
        "Проигнорировать" :
            jump IgonreDragon #КОНЦОВКА
    return

label TalkWithDragon:
    val Normal "{i}А как?.. Ну то есть… Ты меня слышишь? Привет?{/i}"
    "{i}Эй… Эй! Ты это мне?{/i}"
    val Normal "{i}Нуу, наверное? Очень надеюсь, что больше голосов у меня в голове нет и тебя одного достаточно.{/i}"
    rixnone "Грубо. Но это неважно."
    rixnone "Наконец-то, ты меня слушаешь! Мне очень нужна твоя помощь! Что-то страшное происходит у меня дома и только ты можешь помочь мне спасти наше королевство миров…"
    val Normal "Стой-стой-стой! Какая помощь, какое королевство вообще кто ты…"
    rixnone "Это совершенно не важно! Ведь я даже показаться тебе не могу, только быть проводником в своем мире. Дома я великий дракон, но ты можешь представить меня как угодно, это не имеет значения. Мне очень нужна твоя помощь!"
    "Лера отдала всё на откуп своему воображению. Кажется, представить себе дракона не было такой уж сложной задачей." 
    "Но ассоциировать собеседника с каким-то образом было комфортнее, чем общаться с чем-то совершенно бестелесным."
    show Val Normal at leftm with easeinleft
    show Rix at rightm with easeinright
    val Normal "Хорошо… Дракон, значит… И чем я могу помочь?"
    rix "Дело в том, что мой дом это не одно место или планета в привычном понимании. Он держится на гармонии нескольких миров, которые хоть и существуют параллельно, но своей силой они поддерживают и дополняют друг друга!"
    val Thoughtful "И с одним из миров что-то случилось?"
    rix "Не с одним! Это разрушение началось давно, оно постепенно продвигается по всем мирам. Я не могу сказать, что именно происходит, но это чувство, что мой дом слабеет, становится всё сильнее."
    val Normal "Но чем я могу помочь?"
    rix "Как ты могла уже догадаться, мне сложно поддерживать своё непосредственное присутствие в реальности, но я могу стать твоим проводником!"
    rix "Твоими глазами я увижу что происходит и смогу подсказать действия, как помочь мирам и спасти положение."
    val Strict "И ты просто кинешь меня в гущу событий? Удобно, конечно, сам-то ты останешься в безопасности."
    rix "Я не могу пообещать тебе, что всё пройдет легко и безопасно. Могу лишь сказать, что я не знаю источник этого уничтожения, пока что мы отправимся туда, откуда я давно чувствую боль упадка."
    rix "Но у тебя всегда будет выбор отказаться! Я верну тебя домой сразу и больше никогда не побеспокою. И я сделаю всё, чтобы ты не пострадала. Прошу тебя, Лера, только ты можешь помочь мне."
    menu:
        "Cогласиться" :
            jump AgreeWithDragon
        "Отказаться" :
            jump IgonreDragon
    return

label AgreeWithDragon:
    val Normal "Хорошо, я согласна помочь. Но при условии, что ты будешь говорить мне правду. Твоя реальность мне совершенно незнакома, хочется хоть кому-то в ней доверять."
    rix "Конечно! Понимаю, что для тебя это риск, но спасибо огромное, что готова отправиться со мной!"
    val Thoughtful "Подожди, а как это срабо…"
    "Неожиданно Леру окутало ощущение, похожее на свободное падение - земля ушла из под ног, её тело как будто стало легче, дыхание перехватило." 
    "Очертания комнаты поблекли, реальность вокруг неё начала смазываться, и Лера рефлекторно зажмурилась."
    jump Wildstart
    return

