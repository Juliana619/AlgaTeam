label GardenStart:
    scene bg_street
    with hpunch
    show Val Pain at leftm with easeinleft
    show Rix at rightm with easeinright

    val Fight "ДРАКОШ. НУ НАФИГА ТАК РЕЗКО?"
    "Лера чуть не упала от такой внезапной смены мира." 
    rix "Лерчик! Ты только посмотри вокруг! Как тут красиво!"
    "Привыкнув к солнечному свету Лера наконец смогла разжмурить глаза и рассмотреть новый мир."
    show Val Rapture at leftm with easeinleft
    "В этот раз Валерию закинуло в чудесный цветущий сад. Казалось, что каждый цветочек, каждая травинка здесь были окружены вниманием и заботой. Вся эта атмосфера была просто волшебной."
    "Фонтаны, лавочки, белоснежные статуи, и шикарный особняк, выкрашенный в желтую краску! От всего этого великолепия просто захватывало дух."
    val Rapture "Этот мир прекрасен…"
    menu:
        "Вспомнить зачем мы здесь" :
            jump Remind
        "Наслаждаться каждой секундой своего существования." :
            jump Joy
    return
label Joy:
    scene bg_street
    "Лера понюхала сначала один цветок. Следом другой. Потом она побежала к соседней клумбе. Затем она решила покачаться на качелях. Потом поиграть с корабликами в фонтане…"
    "В скором времени она познакомилась с хозяевами этого места - садовником и его псом."
    "Садовник был так добр к ней, что разрешил остаться в саду столько, сколько она пожелает."
    "Дни сменялись днями. Лера классно проводила время со своими новыми приятелями: она играли в шахматы с садовником, бегала по саду с псом."
    "Садовник познакомил девушку и с другими обитателями этого мира. Все они были очень дружные."
    "Назойливый голос Дракоши в голове какое-то время все еще пытался достучаться до девушки и напомнить зачем она пришла в этот сад."
    "Но вскоре он затих."
    "Лера думала, что ее жизнь всегда будет наполнена только счастьем и радостью."
    "Однако это длилось недолго… В какой-то момент мир райского сада начал гнить и умирать так же, как и другие миры."
    "Валерия пыталась позвать дракона. Она осознала свою ошибку. Но дракон больше не появился. Возможно, что он исчез навсегда…"
    "ПОЛУЧЕНА КОНЦВОКА: РАЙСКИЙ САД"
    return

label Remind:
    "Пение птиц и свежий воздух дарили чувство спокойствия. Но, в то же время, что-то в душе  Леры, беспокоило ее. Она стояла неподвижно, вглядываясь в даль сада, и, вдруг, услышала голос дракончика." 
    rix "ЛЕЕЕЕРААААА!"
    "Голос был где-то далеко, но постепенно приближался и возвращал Леру в реальность."
    rix "ЛЕРА! Ответь! Только не снова, не игнорируй меня!"
    val Pain "Драк! Этот сад, он одурманил меня! Я почти перестала слышать твой голос."
    val Honor "Но сейчас я вспомнила зачем мы здесь. Нам нужно спешить!"
    rix "Фуууух, хвала богам, ты очнулась. Еще бы чуть-чуть и… и я бы потерял тебя. И я бы потерял себя."
    val Thoughtful "Что? Себя?"
    rix "Себя? Нет, тебе послышалось. Тебя! Т Е Б Я."
    val Fight "Да поняла я, поняла. Еще десяток раз повтори, ага, будто я умственно отсталая!"
    val Fight "Предлагаю осмотреть особняк!"
    "Валерия подошла к особняку и постучала в дверь. Ответа не было. Тогда она постучала еще раз. И еще. Дверь никто не открывал."
    "Девушка начала дергать ручку двери, но та, естественно, не поддавалась."
    val Fight "Уууух дурацкая дверь!!!"
    "Лера со всей дури пнула по двери и тут же пожалела об этом. Боль в ноге заставила Леру открыть рот для крика, но тут сзади раздался мужской голос."
    incognito "Во-первых, тут есть звонок!"
    show Val Fear at leftm with easeinleft
    show Ostin Evil at rightm with easeinright
    "Обернувшись, девушка увидела зло настроенного усатого лысого садовника и рычащую собаку. На злость садовника указывали красное лицо и вилы, направленные в ее сторону."
    ostin Evil "А во-вторых, с какой стати ты пытаешься вломиться в этот особняк??"
    val Shy "Ох простите. Это ваш дом? Мы тут просто… Мы не местные, да! Хотели попросить помощи."
    ostin Evil "Ах вы бандитская шайка, значит ты тут не одна! Я вызываю полицию! Где твои пособники?"
    val Fear "Я… Не надо полицию!"
    val Fear "Я здесь одна, я ошиблась, вы меня очень напугали своими вилами."
    ostin Evil "ХВАТИТ МЕНЯ ДУРИТЬ!"
    "Садовник начал угрожающе приближаться."
    rix "ДА СКАЖИ ТЫ ЕМУ ПРАВДУ, ЧТО ТЫ МЕЛЕШЬ, ДЕВКА?"
    val Fear "Мистер Садовник, пожалуйста, послушайте, я вам сейчас все объясню, не надо меня на вилы!"
    ostin Evil "Я слушаю, рассказывай."
    val "Я не местная, это правда. Я из другого мира."
    "Валерия рассказала всю свою историю. О том, как она путешествует по мирам, ведомая голосом дракона, и собирает разные предметы, обладающие силой. Рассказала и о том, что все это нужно для того, чтобы спасти остальные миры."
    val Fear "Только пожалуйста, не протыкайте меня своими вилами! Прошу!"
    ostin Normal "Ахахаха. Да я бы никогда не стал убивать людей. Насаживать их на вилы. Ты ведь и сама меня напугала! Поэтому я и схватил первое, что попалось под руку."
    val Shy "Простите за недоразумение. Мои чувства чуть-чуть вышли из под контроля."
    val Rapture "Этот сад, он замечательный. Он будто обостряет все чувства и эмоции."
    val Honor "Но дело в том, что мне нужна ваша помощь! Ваш сад и ваши друзья в опасности."
    ostin Normal "В опасности? С чего ты взяла? Здесь нет ни намека на опасноть!"
    val "Мой друг, дракон, не мог отправить меня в ваш мир просто так. "
    ostin Normal "А этот дракон, он сейчас здесь? С нами?"
    val Thoughtful "Ну, на самом деле физически его здесь нет. Но я могу слышать его голос. К сожалению, по какой-то причине, дракона не могут слышать другие существа."
    ostin Normal "Хм, это звучит невероятно, но почему-то я тебе верю. Как я могу помочь?"
    val Honor "Спасибо! С прошлого мира я получила фишку и карту. Возможно, что в вашем мире есть что-то подобное? Какие-то вещи, которые обладают необыкновенными свойствами."
    ostin Normal "О, да, у нас тоже есть фишки! Только они немного другие."
    ostin Normal "Вот, возьми. Могу дать тебе, но только одну!"

    #ПЕРЕБИВКА "ВЫ ПОЛУЧИЛИ ПРЕДМЕТ"
    $ gardenchip = True

    val Happy "Спасибо большое!"
    val Thoughtful "Если не секрет, можете рассказать для чего вам эти фишки? И почему они вам так дороги?"
    ostin Normal "Фишки помогают мне восстанавливать сад. И даже потеря одной штуки может повлечь за собой необратимые последствия."
    ostin Normal "Представь, что фишки - это части магического кода. Если одна пропадет, код может неправильно сработать!"
    val Thoughtful "Хм. Если честно, то ничего не понятно, но очень интересно."
    rix "Лерчик, молодец! А теперь нам пора. Даю тебе время попрощаться с этим мужчиной. Отправляемся через Десять… Девять…"
    val Fear "О, мне пора!"
    ostin Normal "Эх, даже на чай не осталась!"
    val Happy "Большое спасибо за помощь! Я постараюсь вернуть вам фишку. Если получится!"
    rix "Два… Один…"
    jump FamilyStart
    return  