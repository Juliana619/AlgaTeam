label GoldGoStart:
    scene bg_street
    with hpunch
    show Val Pain at leftm with easeinleft
    show Rix at rightm with easeinright
    val Pain "Боже… это было сложно… Я так устала."
    rix "Ты молодец. Справилась."
    val Pain "Спасибо за то, что так скоро переместил меня из того мира. На этот раз - спасибо!"
    rix "Лер, выше нос! Я думаю, что это конечная."
    val Fear "Неужели мы тут умрем?"
    rix "Нет! Конечно нет! Я не это имел в виду, Лер."
    val Happy "Да шучу я, расслабься!"
    rix "А….."
    rix "В общем. Я понял про какого деда в фиолетовых одеяниях говорил тот мужчина."
    rix "Кажется, что этим дедом был…" 
    rix "…король этого мира!"
    val Thoughtful "Неужели?"
    val Fight "Тогда зададим ему трепку!"
    jump GoldStart
    return

label GoldRunStart:
    scene bg_street
    with hpunch
    show Val Pain at leftm with easeinleft
    show Rix at rightm with easeinright
    val Pain "Ужасный мужчина. Ужасный мир. Это.. все… было ужасно… Я хочу домой…"
    val Pain "Почему тут так холодно?"
    rix "Я переместил нас в место похолоднее. Я надеялся, что это поможет тебе успокоиться."
    val Honor "Спасибо… Мне уже лучше."
    jump GoldStart
    return

label GoldStart:
    val Thoughtful "А слушай, Драк! Этот мир не похож на остальные… Что-то тут не так."
    rix "Дурость какая, все миры не похожи один на другой. Суть у них, может, и одна, но внешне они уникальны!"
    val "Нет, я не об этом. Он ощущается иначе. Здесь время будто бы замерло. Не похоже будто тут что-то вообще было, а еще он как будто… Не доделан?"
    "И правда многие вещи в мире выглядели брошенными на полпути, будто кто-то начал работу, но не успел её закончить и оставил так, с надеждой когда-нибудь доделать."
    "Но при этом повсюду были видны горы золота. Монеты переливались, привлекая к себе всё внимание и затмевая окружающую их пустоту."
    rix "Не может быть хорошим тот, кто так зациклен на золоте…"
    val Normal "Ну да, ты-то настолько материальное отрицаешь, что и тела у тебя нет"
    rix "…Очень смешно. Давай-ка не забывать, что здесь нас может поджидать разгадка, я чувствую, что мы уже близки к разгадке. А, значит, и к источнику опасности."
    "Неожиданно со стороны послышался грохот, а затем звук чего-то быстро приближающегося."
    val Fight "А вот кажется и опасность!"
    "Лера оглянулась по сторонам в поисках предмета для обороны, но не успела ничего схватить, как перед ней выскочил енот."
    show Rac Worr at centerz with easeinleft
    rac Worr "Стой! Не уходи!"
    val Fight "Это ты стой! Не вздумай нападать!"
    rac Worr "Что? Какое нападение! Мне помощь нужна!"
    val Fight "Так я тебе и поверила! Ваш мир, кажется, не в беде. Наоборот, воруете у других во своё благо!"
    rac Worr "Что? Что за бред?! Еще как в беде! Моего короля заморозили!"
    "Лера немного растерянно посмотрела на енота, но продолжила держать от него дистанцию."
    rix "Слушай, ну кажется, он правду говорит…"
    val Normal "Объясни, что у вас тут произошло? И про короля расскажи подробнее…"
    rac Worr "Я всё объясню! Просто поверь мне, нам нужно скорее идти, а то время на исходе! Я расскажу всё по дороге!"
    "Лера задумчиво оглядела мир еще раз, посмотрела на енота. Кажется, им нужно было не сюда, в этом мире они просто тратили время."
    "Но енот уже не казался таким опасным и, кажется, ему действительно нужна была помощь. Но есть ли у девушки на это время?"

    menu:
        "Помочь еноту" :
            jump Helpracoon
        "Не помогать еноту" :
            jump Ignoreracoon
    return

label Ignoreracoon:
    val Normal "Мне кажется, мы здесь ничего не найдем и нужно дальше двигаться."
    rix "Возможно, ты права… Но уйти всегда успеем, может, всё-таки поможем ему?"
    val "Дракош, ты же сам меня поторапливал. Давай двигаться дальше, мы зря тратим время"
    rac Worr "Эй! С кем ты разговариваешь? Почему ты меня не слушаешь?"
    rix "Может, всё-таки…"
    val "Нет, нужно уходить. Или у тебя миры закончились?"
    rix "На самом деле… Весь этот антураж и золото напомнили мне об одном мире и его правителе, но, приготовься, не самое приятное место."
    jump RMStart
    return

label Helpracoon:
    "Лера вздохнула и кивнула еноту, соглашаясь ему помочь. Он тут же повел девушку вглубь мира на ходу объясняя всё произошедшее."
    rac Worr "Вообще-то, золото мы ниоткуда не воруем, нам хватало ресурсов своего мира. Но затем пришел этот злобный король и всё остановилось."
    rac "Просто время замерло, как будто поток сил покинул нас и ушел в другие миры. А мы остались… Ну такими."
    val Thoughtful "Подожди. Еще один король?"
    rac Worr "Да! Я не знаю, кто он. Но помогите мне разморозить нашего короля, он его точно узнал, я всё видел!"
    "Енот привел Леру к странной конструкции, внизу которой замер король. Он был в огромном ледяном блоке. Сверху у конструкции была несложная система трубок, которая вела к трем сосудам: с золотом, холодной водой и кипятком."
    show King Freez at rightm with easeinright
    rac Worr "Это какая-то очень странная загадка! Ничего не пойму! Что бы я не нажимал, всё затем отматывается к началу!"
    "Показательно енот начал нажимать на рычаги перед конструкцией - он сыпал на ледяной блок монетами, выливал ледяную воду, сливал кипяток мимо короля, смешивал ледяную воду с горячей, делая последнюю еле теплой."
    "Ничего не помогало королю, и после каждой попытки конструкция отматывалась к исходному положению."
    "Лера смотрела на каждый новый заход енота и чувствовала, как начинает закипать."
    val Fight "Ты что, сдурел?!"
    rac Worr "А что я не так сделал? Я пытаюсь королю помочь!"
    val "Да это же банальный паззл. Отойди в сторону, всё проще простого."
    "В три клика Лера слила ненужную ледяную воду, засыпала короля монетами и сверху облила кипятком. Ледяной блок поддался, и вскоре живой и целый король выбрался из конструкции."
    rac Happy "Мой Король! Вы в порядке! Вы свободны!"
    king Happy "Сколько времени прошло! Я уж думал и не выберусь из этой западни! Спасибо, мой друг, что привел помощь."
    val Strict "Вы могли бы быть свободны раньше, если бы кое-кто был повнимательнее."
    rix "Ну, Лер, ты чего злая такая, ну перенервничал енот."
    king Happy "Огромное спасибо, моя спасительница! Как же хорошо, что вы оказались в нашем мире. Хоть он и не в лучшем состоянии сейчас."
    val Shy "Что ж, да не за что… Кажется, и правда все беды в другие миры не из вашего идут."
    king Surp "Что? Конечно нет, ваш Король в другом замке! Это всё злой Король Эрэм. Мне, конечно, говорили, что мы похожи. Но это только на первый взгляд! Я, знаете ли, и моложе, и в другие миры за мощью выдуманной не лезу!"
    rix "Так вот кто это был всё это время! Лер, я знаю этот мир, мы можем отправляться!"
    val Honor "Спасибо вам большое за информацию! Пора положить конец этой тирании!"
    king Happy "Подождите! Возьмите это и удачи! Пусть она поможет вам в вашей борьбе!"
    "Лера взяла у Короля фишку и кивнула на прощание прежде чем Дракон уже начал перемещение в следующий и, наконец, конечный мир."
    #ПЕРЕБИВКА "ВЫ ПОЛУЧИЛИ ФИШКУ"
    $ chipcount = chipcount + 1
    $ goldhunterchip = True
    jump RMStart
    return
