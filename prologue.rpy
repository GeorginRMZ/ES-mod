label mod_start:
    th "Лена лучший персонаж"
    mi "Факты"
    un "Спасибо"
    sm "Негры"

    scene bg ext_bus

    "Негры утырки"

    scene bg ext_camp_entrance_day
    show sl normal pioneer far at center with dissolve

    "... в пионерской форме."
    th "Логика меня не подвела."
    th "Впрочем, пионерская форма в XXI веке…"
    th "Впрочем, девочки {i}здесь{/i}..."
    "Я застыл на месте не в силах сделать ни шагу."
    "Очень хотелось убежать.{w} Подальше отсюда, подальше от этого автобуса, ворот, статуй, подальше от этой чёртовой птицы с её сиестой."
    "Просто бежать, бежать свободно, словно ветер, бежать всё быстрее, маша рукой пролетающим мимо планетам, подмигивая галактикам."
    "Бежать, став лучом пульсара, превратившись в реликтовое излучение, бежать навстречу неизвестности."
    "Бежать куда угодно, но {b}подальше{/b} отсюда!"
    slp "Негры пидоры?"

    window hide
    menu:
        "Да" if True:
            window show

            "Не ну ведь по факту же"
            slp "Меня Славя зовут, а тебя?"
            me "А меня гигачад зовут."
            sl "Ну проходи gigachad."

            hide sl with dissolve
            window hide
            scene bg ext_clubs_day
            with dissolve
            play ambience ambience_camp_center_day fadein 5
            window show

            me "Based woman."

        "Black lives matter" if True:
            window show
            show sl angry pioneer far at center with dissolve

            slp "Ну и пошел ты нахуй."

            hide sl with dissolve
            window hide
            scene bg ext_bus
            window show

            "Базированная gigachad woman захлопнула дверь в лагерь и я сел плакать у автобуса. Ведь black lives matter"
            me "Я балбес."


