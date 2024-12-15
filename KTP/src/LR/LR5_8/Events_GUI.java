package src.LR.LR5_8;

import java.io.*;
import java.util.*;
import javax.swing.*;

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

// Родительский класс "Событие"
class Event {
    private String date;
    private String time;

    public Event(String date, String time) {
        this.date = date;
        this.time = time;
    }

    public String getDate() {
        return date;
    }

    public String getTime() {
        return time;
    }

    @Override
    public String toString() {
        return "Event Date: " + date + 
        ", Event Time: " + time;
    }
}

// Дочерний класс "День рождения"
class Birthday extends Event {
    private String hero;
    private String place;
    private int age;

    public Birthday(String date, String time, String hero, String place, int age) {
        super(date, time);
        this.hero = hero;
        this.place = place;
        this.age = age;
    }

    public String getHero() {
        return hero;
    }

    public String getPlace() {
        return place;
    }

    public int getAge() {
        return age;
    }
}

// Дочерний класс "Встреча"
class Meeting extends Event {
    private String person;
    private String place;

    public Meeting(String date, String time, String person, String place) {
        super(date, time);
        this.person = person;
        this.place = place;
    }

    public String getPerson() {
        return person;
    }

    public String getPlace() {
        return place;
    }
}

// Класс для хранения списка событий
class EventList {
    private List<Event> events;

    public EventList() {
        this.events = new ArrayList<>();
    }

    public void addEvent(Event event) {
        events.add(event);
    }

    public void printEvents() {
        for (Event event : events) {
            System.out.println(event);
        }
    }

    public void sortEventsByDate() {
        Collections.sort(events, Comparator.comparing(Event::getDate));
    }

    public void saveToFile(String filename) {
        try (PrintWriter writer = new PrintWriter(new FileWriter(filename))) {
            for (Event event : events) {
                writer.println(event.getDate() + "," + event.getTime());
            }
        } catch (IOException e) {
            System.out.println("Error saving to file: " + e.getMessage());
        }
    }

    public void loadFromFile(String filename) {
        try (Scanner scanner = new Scanner(new File(filename))) {
            while (scanner.hasNextLine()) {
                String line = scanner.nextLine();
                String[] parts = line.split(",");
                if (parts.length == 5) {
                    String eventDate = parts[0];
                    String eventTime = parts[1];
                    Event event = new Event(eventDate, eventTime);
                    events.add(event);
                }
            }
        } catch (IOException e) {
            System.out.println("Error loading from file: " + e.getMessage());
        }
    }
}

// Пользовательское меню
public class Events_GUI {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        EventList eventList = new EventList();
        JFrame frame = new JFrame("Менеджер событий");

        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(300, 300);
        frame.setLocationRelativeTo(null);
        JButton button = new JButton("Тестовая кнопка");
        frame.getContentPane().add(button);
        frame.setVisible(true);

        while (true) {
            System.out.println("Menu:");
            System.out.println("1. Add Event");
            System.out.println("2. Print Events");
            System.out.println("3. Sort Events by Date");
            System.out.println("4. Save Events to File");
            System.out.println("5. Load Events from File");
            System.out.println("6. Exit");
            System.out.print("Choose an option: ");
            int choice = scanner.nextInt();
            scanner.nextLine(); // Consume newline

            switch (choice) {
                case 1:
                    System.out.print("Enter Event Date: ");
                    String eventDate = scanner.nextLine();
                    System.out.print("Enter Event Time: ");
                    String eventTime = scanner.nextLine();
                    scanner.nextLine(); // Consume newline

                    Event event = new Event(eventDate, eventTime);
                    eventList.addEvent(event);
                    break;
                case 2:
                    eventList.printEvents();
                    break;
                case 3:
                    eventList.sortEventsByDate();
                    System.out.println("Events sorted by Date.");
                    break;
                case 4:
                    System.out.print("Enter filename to save: ");
                    String saveFilename = scanner.nextLine();
                    eventList.saveToFile(saveFilename);
                    System.out.println("Events saved to file.");
                    break;
                case 5:
                    System.out.print("Enter filename to load: ");
                    String loadFilename = scanner.nextLine();
                    eventList.loadFromFile(loadFilename);
                    System.out.println("Events loaded from file.");
                    break;
                case 6:
                    System.out.println("Exiting...");
                    scanner.close();
                    System.exit(0);
                default:
                    System.out.println("Invalid option. Please try again.");
            }
        }
    }
}