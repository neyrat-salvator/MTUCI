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

public class Events {

    public class Event extends Events {

        private String date;
        private String time;
    
        public class Birthday extends Event {
            private String hero;
            private String place;
            private int age;
    
            public Birthday(String hero, String place, int age) {
                this.hero = hero;
                this.place = place;
                this.age = age;
            }
    
            public String toString() {
                String birthdayString = hero + "исполняется " + age + ". День рождения пройдет в " + place;
                return birthdayString;
            }
        }
    
        public class Meeting extends Event {
            private String person;
            private String place;

            public Meeting(String person, String place) {
                this.person = person;
                this.place = place;
            }
    
            public String toString() {
                String metingString = "Встреча с " + person + "в " + place;
                return metingString;
            }
        }
    
        public class Custom extends Event {
            private String description;
    
            public Custom(String description) {
                this.description = description;
            }
    
            public String toString() {
                String customString = "Событие: " + description;
                return customString;
            }
        }
        
    }

    static String userWriteString() {
        try {
            Scanner in = new Scanner(System.in);
            String userText = in.nextLine();
            in.close();
            return userText;
        } catch (Exception e) {
            String errorMessage = "Допускается только текст без цифр и спецсимволов";
            return errorMessage;
        }
        
    }

    static int userWriteInt() {
        try {
            Scanner in = new Scanner(System.in);
            int userInt = in.nextInt();
            in.close();
            return userInt;
        } catch (Exception e) {
            return 0;
        }
        
    }

    static List<String> eventList = new ArrayList<String>();

    private void show() {
        System.out.println("Список программ:");
        for (int i = 0; i <= (eventList.size() - 1); i++) {
            System.out.println("Событие типа: " 
            + eventList.get(i).getClass() 
            + "\nДетали события:\n" 
            + eventList.get(i));
        }
    }

    private String add(String event, String date, String time) {

        switch (event) {
            case "Birthday":

                // Birthday sample = new ;


                System.out.println("У кого день рождения?");
                String heroString = userWriteString();
                if (heroString != "") {

                } else {
                    System.out.println("Недопустимо пустое имя");
                    return null;
                }


                System.out.println("Где празднуется день рождения?");

                System.out.println("Сколько лет имениннику?");
                
                return null;

            case "Meeting":

                System.out.println("С кем намечается встреча?");

                System.out.println("Где намечается встреча?");

                return null;
        
            default:

                System.out.println("Опишите событие:");

                return null;
        }
    }

    // Основной метод класса
    public static void main(String[] args) {

        // System.out.println(add());
    }
}