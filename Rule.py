
def game_beginning():
    return '**Начало игры**\n\n' \
           'В начале игры у каждого игрока есть 20 жизней.\n\n' \
            'Чтобы одержать победу, вы должны сократить количество жизней оппонента до нуля.' \
           ' Можно также победить оппонента, если он должен взять карту,' \
           ' а его колода пуста, или если заклинание или способность объявляет вас победителем.\n\n' \
            'Определите, кто из игроков будет делать первый ход.' \
           ' Если вы только что закончили предыдущую партию с этим же оппонентом,' \
           ' то проигравший решает, кто ходит первым.' \
           ' В противном случае, бросьте кубик или подкиньте монету,' \
           ' чтобы выбрать игрока, который примет это решение.\n\n' \
            'Каждый игрок тасует свою колоду и набирает руку из семи карт, чтобы начать игру.' \
           ' Если вам не понравилась ваша начальная рука, можно запросить пересдачу. ' \
           'Втасуйте карты обратно в колоду и наберите новую руку, уже из шести карт. ' \
           'Так можно поступать до тех пор, пока вас не устроят взятые карты, ' \
           'но при каждой пересдаче в новой руке должно быть на одну карту меньше.'

def starting_phase():
    return '**НАЧАЛЬНАЯ ФАЗА**\n\n' \
            '\t1.Шаг разворота\n' \
            '\t\tРазверните все ваши повернутые перманенты.' \
            ' Если это первый ход в данной партии, то \t\tперманентов у вас пока нет,' \
            ' поэтому просто пропустите этот шаг. ' \
            'Во время этого шага нельзя \t\tразыгрывать заклинания и активировать способности.\n\n' \
            '\t2.Шаг поддержки\n' \
            '\t\tЭтот этап хода часто упоминается в тексте карт. ' \
            'Если что-то должно произойти всего лишь один \t\tраз в ходу, в самом начале,' \
            ' то способность срабатывает «в начале вашего шага поддержки».' \
            ' Игроки \t\tмогут разыгрывать мгновенные заклинания и активировать способности.\n\n' \
            '\t3.Шаг взятия карты\n' \
            '\t\tВозьмите одну карту из вашей библиотеки.' \
            ' (Игрок, который ходит первым, пропускает шаг взятия \t\tкарты во время своего первого хода,' \
            ' поскольку у него и так есть преимущество.)' \
            ' Теперь игроки могут \t\tразыгрывать мгновенные заклинания и активировать способности.'
