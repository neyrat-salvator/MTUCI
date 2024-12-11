package src.LR.LR5_8;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

// Юрцук Константин Сергеевич
// Лабораторная работа №5 КОЛЛЕКЦИИ
// Лабораторная работа №7 ВВОД-ВЫВОД. ПАКЕТ JAVA.IO
// Лабораторная работа №8 ЛАБОРАТОРНАЯ РАБОТА №7. РАБОТА С ФАЙЛАМИ
// Вариант: 1 (26)

/*НАСЛЕДОВАНИЕ И ПОЛИМОРФИЗМ

Реализовать предметную область:
1 Записная книжка. Создать родительский класс «Событие» (дата, время) и дочерние классы:
- «День рождения» (именинник, место проведения праздника и возраст);
- «Встреча» (человек с которым назначена встреча и место встречи);
- «Другое» (описание).
Реализовать класс для хранения списка событий 
с методом добавления события и методом печати списка событий.

Выполнить преобразование класса в коллекцию.
Создать пользовательское меню. Организовать добавление объектов в коллекцию и 
вывод отсортированных объектов коллекции на экран с помощью меню.

Организовать сохранение объектов из коллекции в текстовый файл 
и загрузку объектов из текстового файла в коллек-цию. 
Изменить пользовательское меню для добавления работы с внешними файлами.
*/

class Event {

    String date;
    String time;

    class Birthday extends Event {
        String hero;
        String place;
        int age;

        static String toString(int value) {
            return String.valueOf(value);
        }
    }

    class Meeting extends Event {
        String person;
        String place;

        static String toString(int value) {
            return String.valueOf(value);
        }
    }

    class Custom extends Event {
        String description;

        static String toString(int value) {
            return String.valueOf(value);
        }
    }
    
}

public class LR5_8 extends Event {

    static List<String> events = new ArrayList<String>();

    static void show() {
        System.out.println("Список программ:");
        for (int i = 0; i <= (events.size() - 1); i++) {
            System.out.println(events.get(i));
        }
    }

    static void add() {
        System.out.println("Какое событие добавить? " + String event = );
    }

    // Основной метод класса
    public static void main(String[] args) {

    }
}