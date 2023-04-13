
import sqlite3
try:
    conn = sqlite3.connect("zxcasuka (1).db ")
    cursor = conn.cursor()
    cursor.execute('''DELETE FROM recrd''')
    cursor.execute("""INSERT INTO recrd VALUES (0101, "Гендо Икраи", "Директор и главное представительное лицо Nerv. Очень закрытый человек, имеющий большие планы")""")
    cursor.execute("""INSERT INTO recrd VALUES (0102, "Мисато Кацураги", "Майор, руководитель отделения тактических операций Nerv в реальных боевых действиях. Порой ведёт себя по-детски, но её спланированные решения не раз приводили Nerv к победе против ангелов.") """)
    cursor.execute("""INSERT INTO recrd VALUES (0103,"Макото Хьюга","Хьюга — работник оперативного отдела Nerv и является главным помощником капитана — Мисато Кацураги.") """)
    cursor.execute("""INSERT INTO recrd VALUES (0104,"Рицуко Акаги","Главный научный сотрудник Nerv и руководитель техническим отделением штаб-квартиры, которое отвечает за исследования и разработку Евангелионов, а также их техническое обслуживание и ремонт.") """)
    cursor.execute("""INSERT INTO recrd VALUES (0105,"Майя Ибуки","Одна из трёх главных компьютерных техников в штаб-квартире Nerv, наряду с Макото Хьюгой и Сигэру Аобой(Покинул Nerv). Работает непосредственно под руководством доктора Рицуко Акаги.") """)
    cursor.execute("""INSERT INTO recrd VALUES (0201,"ЕВА00","Первый оперативный Евангелион, пилотируемый Рей Айанами. Будучи прототипом, Ева-00 первоначально не предназначалась для боёв, но позднее она была усовершенствована и использована против Ангелов.") """)
    cursor.execute("""INSERT INTO recrd VALUES (0202,"ЕВА01","Флагманская меха, созданная Gehirn. Пилотируется сыном Гендо Икари, Синдзи Икари. В отличие от других Ев, тело Евы-01 было создано непосредственно из тела Лилит, а посему меха носит название «потомство» Лилит или её «клон».") """)
    cursor.execute("""INSERT INTO recrd VALUES (0203,"ЕВА02", 'Третий завершённый Евангелион и первая производственная модель. Конструкция Евы-02 якобы исправляет ошибки, допущенные при строительстве прототипа Евы-00 и тестового типа Евы-01, что делает её первым Евангелионом, построенным специально для борьбы с Ангелами.') """)
    cursor.execute("""INSERT INTO recrd VALUES (0204,"ЕВА03НЕДЕЙСТВИТЕЛЬНО", "Построенный первым филиалом Nerv в Соединённых Штатах, — вторая боевая модель Евангелиона. Перевезена в Мацусиро на первое испытание. Пилотируется 4 дитя - Тодзи Судзухара. Уничтожен Евой-01 на псевдопилоте.") """)
    cursor.execute("""INSERT INTO recrd VALUES (0301,"NERV", 'Nerv (ネルフ, Неруфу, с нем. «нерв») — военизированное специальное учреждение, номинально находящимся под контролем Организации Объединённых Наций. Официальная цель Nerv состоит в том, чтобы возглавить защиту человечества против Ангелов и остановить их от инициирования Третьего удара после разрушений, вызванных Адамом во время Второго удара в 2000 году, с помощью Евангелионов, которые были построены этой организацией. Nerv возглавляет командующий Гэндо Икари.') """)
    cursor.execute("""INSERT INTO recrd VALUES (0401, "Особенности работы.", "Система С.К. Magi (マギ, «волхвы») — трио суперкомпьютеров, созданных доктором Наоко Акаги в ходе её исследования био-компьютеров в Gehirn.[1] В органические компьютеры седьмого поколения Magi были имплантированы три различных аспекта личности доктора Наоко Акаги с использованием операционной системы переноса личности. Вайшей задачей будет инспектирование и управление компьютером. Magi использует ту же систему переноса личности, что и Евангелионы. ") """)



    conn.commit()
except sqlite3.Error as error:
    print("Error", error)
finally:
    if(conn):
        conn.close()