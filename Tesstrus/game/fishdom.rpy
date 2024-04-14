label FishdomStart:
    scene bg_street
    with hpunch
    show Val Pain at leftm with easeinleft
    show Rix at rightm with easeinright
    "Моргнув, Лера очутилась… под водой?"
    val Normal "Драк! Опять ты так резко! Ну зачем???"
    val Thoughtful "Я что, умею дышать под водой? Драк, а ты?"
    rix "Я всего лишь бесплотный дух, забыла?"
    val Thoughtful "Да блин. Тогда получается, что и **мое** тело здесь как будто ненастоящее. Хммм…"
    val Thoughtful "Как будто бы это какая-то симуляция…"
    rix "Не бери в голову. Нам сейчас важно найти артефакт, в котором заключена мощь этого мира!"
    rix "Ты же понимаешь, что каждая секунда промедления может стоить жизни обитателям других миров?"
    val Normal "Да, так что давай не будем тратить время на споры и рассуждения."
    rix "Ага, согласен. Погнали осмотримся?"
    val Thoughtful "{i}И все-таки… Что со мной происходит? А что, если я умерла, а это все - что-то типа чистилища? 7 кругов ада и один уже пройден?{/i}"
    rix "Я не понял, ты идешь или как?"
    val Normal "Да-да, извини."
    "Местность здесь была не такая опустошенная, как в прошлом мире. Вокруг было много цветных и ярких декораций, статуй, растений. Но, тут и там, можно было заметить уже начавшийся процесс запустения."
    "Была одна странная вещь в этом мире. Дальше 15 метров декорации выглядели будто картонные, а дальнейший обзор закрывала темная пелена. Куда бы ты не посмотрел - всюду твой обзор был ограничен."
    incognito "ААААААААААААААААААААААААААААААААААААААААААА! ПОМОГИТЕ!!!!!"
    show Val Fear at leftm with easeinleft
    "Чей-то крик прервал размышления Леры. Девушка обернулась в сторону звука и увидела, как огромная лягушка гналась за маленькой изящной рыбкой."
    rix "Мы должны что-то сделать!"

    menu:
        "Проигнорировать рыбку" :
            jump IgnoreFish
        "Помочь рыбке" :
            jump HelpFish
    return

label IgnoreFish:
    val Hz "Похоже, что это естественный круговорот в природе. Не думаю, что нам стоит вмешиваться в такое. А то мы и сами сможем стать участниками пищевой цепочки."
    rix "Пффффф. А я и не думал, что ты такая трусиха."
    val Hz "Это просто рациональное мышление, отвали."
    "Побродив по местности Лера так ничего и не нашла. Кроме довольной сытой лягушки, отдыхающей неподалеку от остатков рыбьих плавников."
    rix "Я думаю, что в этом мире мы ничего не найдем, пора двигаться дальше"
    jump GardenStart
    return

label HelpFish:
    "Осмотревшись вокруг, Лера увидела торчащие из песка пластиковые игральные карты."
    val Thoughtful "Это должно сработать. Должно ведь, да?"
    "Лера схватила карты и начала пулять(метать?) их в лягушку. Вопреки всем законам физики карты полетели строго по заданной траектории и вонзились в тело земноводного."
    "Лягушка оставила рыбку и поскакала прочь. При этом, скорость зеленой была еще быстрее, чем в момент погони за рыбкой."
    show Fish Normal at right with easeinright
    fish Normal "Юная русалка, я не знаю где твой хвост, но спасибо за то, что помогла мне!"
    val Shy "Ааа… ээээ? Даааа…. Не за что!"
    rix "Пфффхахахах, ты что, засмущалась от того, что тебя русалкой обозвали? Не забывай зачем мы здесь! Распроси ее об артефакте!"
    val "Рыбка… Красотка! Слушай, а у вас тут есть что-то типа артефакта? Местной реликвии? Какой-то штуки, которая имеет силу?"
    fish Normal "А, ты еще не поняла? Ты же сама воспользовалась ей, чтобы меня спасти."
    rix "Точно, эти карты явно обладают какой-то силой."
    val Happy " Теперь поняла! А ты не против, если я прихвачу карты с собой?"
    fish Normal "Ну хорошо. Ты выглядишь доброй. Ты спасла меня. Можешь взять с собой одну карту."
    val Thoughtful "Всего одну?"
    fish Normal "Не пойми меня неправильно! Тут недавно был один чужеземец. Все рыскал, искал что-то. Видимо то же самое, что и ты. К счастью, он ничего не нашел."
    fish Sad "Но наш мир после этого… Он стал немного другим. Начал меняться. В плохую сторону."
    fish Sad "Если ты сможешь нам как-то помочь, остановить это, то бери эту карту!"
    "Попав в руки Леры, карта превратилась в фишку!"
    #ПЕРЕБИВКА "ВЫ ПОЛУЧИЛИ ПРЕДМЕТ"
    $ chipcount = chipcount + 1
    $ fishchip = True
    val Honor "Ничего не обещаю рыбка, но я постараюсь!"
    rix "Кажется, нам пора"
    val Thoughtful "Но почему карта превратилась в фиш…"
    jump GardenStart
    return