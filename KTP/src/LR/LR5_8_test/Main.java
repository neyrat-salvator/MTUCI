package src.LR.LR5_8;


import java.io.*;
import java.util.*;

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

// Родительский класс "Аптека"
class Pharmacy {
    private String name;
    private String address;
    private String city;
    private String directorFullName;

    public Pharmacy(String name, String address, String city, String directorFullName) {
        this.name = name;
        this.address = address;
        this.city = city;
        this.directorFullName = directorFullName;
    }

    public String getName() {
        return name;
    }

    public String getAddress() {
        return address;
    }

    public String getCity() {
        return city;
    }

    public String getDirectorFullName() {
        return directorFullName;
    }
}

// Дочерний класс "Клиенты аптеки"
class PharmacyClient extends Pharmacy {
    private String clientFullName;
    private double discountPercentage;

    public PharmacyClient(String name, String address, String city, String directorFullName, String clientFullName, double discountPercentage) {
        super(name, address, city, directorFullName);
        this.clientFullName = clientFullName;
        this.discountPercentage = discountPercentage;
    }

    public String getClientFullName() {
        return clientFullName;
    }

    public double getDiscountPercentage() {
        return discountPercentage;
    }
}

// Дочерний класс "Лекарственный фонд аптеки"
class PharmacyMedicine extends Pharmacy {
    private String medicineName;
    private String medicineType;
    private double medicinePrice;
    private String countryOfOrigin;

    public PharmacyMedicine(String name, String address, String city, String directorFullName, String medicineName, String medicineType, double medicinePrice, String countryOfOrigin) {
        super(name, address, city, directorFullName);
        this.medicineName = medicineName;
        this.medicineType = medicineType;
        this.medicinePrice = medicinePrice;
        this.countryOfOrigin = countryOfOrigin;
    }

    public String getMedicineName() {
        return medicineName;
    }

    public String getMedicineType() {
        return medicineType;
    }

    public double getMedicinePrice() {
        return medicinePrice;
    }

    public String getCountryOfOrigin() {
        return countryOfOrigin;
    }

    @Override
    public String toString() {
        return "Medicine Name: " + medicineName +
                ", Medicine Type: " + medicineType +
                ", Medicine Price: " + medicinePrice +
                ", Country of Origin: " + countryOfOrigin;
    }
}

// Дочерний класс "Продажи"
class PharmacySale extends Pharmacy {
    private String medicineName;
    private double medicinePrice;
    private String clientFullName;
    private int quantity;
    private double totalAmount;

    public PharmacySale(String name, String address, String city, String directorFullName, String medicineName, double medicinePrice, String clientFullName, int quantity, double totalAmount) {
        super(name, address, city, directorFullName);
        this.medicineName = medicineName;
        this.medicinePrice = medicinePrice;
        this.clientFullName = clientFullName;
        this.quantity = quantity;
        this.totalAmount = totalAmount;
    }

    public String getMedicineName() {
        return medicineName;
    }

    public double getMedicinePrice() {
        return medicinePrice;
    }

    public String getClientFullName() {
        return clientFullName;
    }

    public int getQuantity() {
        return quantity;
    }

    public double getTotalAmount() {
        return totalAmount;
    }
}

// Класс для хранения списка лекарств
class MedicineList {
    private List<PharmacyMedicine> medicines;

    public MedicineList() {
        this.medicines = new ArrayList<>();
    }

    public void addMedicine(PharmacyMedicine medicine) {
        medicines.add(medicine);
    }

    public void printMedicines() {
        for (PharmacyMedicine medicine : medicines) {
            System.out.println(medicine);
        }
    }

    public void sortMedicinesByName() {
        Collections.sort(medicines, Comparator.comparing(PharmacyMedicine::getMedicineName));
    }

    public void saveToFile(String filename) {
        try (PrintWriter writer = new PrintWriter(new FileWriter(filename))) {
            for (PharmacyMedicine medicine : medicines) {
                writer.println(medicine.getName() + "," + medicine.getMedicineName() + "," + medicine.getMedicineType() + "," + medicine.getMedicinePrice() + "," + medicine.getCountryOfOrigin());
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
                    String name = parts[0];
                    String medicineName = parts[1];
                    String medicineType = parts[2];
                    double medicinePrice = Double.parseDouble(parts[3]);
                    String countryOfOrigin = parts[4];
                    PharmacyMedicine medicine = new PharmacyMedicine(name, "", "", "", medicineName, medicineType, medicinePrice, countryOfOrigin);
                    medicines.add(medicine);
                }
            }
        } catch (IOException e) {
            System.out.println("Error loading from file: " + e.getMessage());
        }
    }
}

// Пользовательское меню
public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        MedicineList medicineList = new MedicineList();

        while (true) {
            System.out.println("Menu:");
            System.out.println("1. Add Medicine");
            System.out.println("2. Print Medicines");
            System.out.println("3. Sort Medicines by Name");
            System.out.println("4. Save Medicines to File");
            System.out.println("5. Load Medicines from File");
            System.out.println("6. Exit");
            System.out.print("Choose an option: ");
            int choice = scanner.nextInt();
            scanner.nextLine(); // Consume newline

            switch (choice) {
                case 1:
                    System.out.print("Enter Pharmacy Name: ");
                    String pharmacyName = scanner.nextLine();
                    System.out.print("Enter Pharmacy Address: ");
                    String pharmacyAddress = scanner.nextLine();
                    System.out.print("Enter Pharmacy City: ");
                    String pharmacyCity = scanner.nextLine();
                    System.out.print("Enter Director Full Name: ");
                    String directorFullName = scanner.nextLine();
                    System.out.print("Enter Medicine Name: ");
                    String medicineName = scanner.nextLine();
                    System.out.print("Enter Medicine Type: ");
                    String medicineType = scanner.nextLine();
                    System.out.print("Enter Medicine Price: ");
                    double medicinePrice = 0.0;
                    try {
                        medicinePrice = scanner.nextDouble();
                    } catch (java.util.InputMismatchException e) {
                        System.out.println("Invalid input for Medicine Price. Please enter a valid number.");
                        scanner.nextLine(); // Consume invalid input
                        continue; // Skip the rest of the loop
                    }
                    scanner.nextLine(); // Consume newline
                    System.out.print("Enter Country of Origin: ");
                    String countryOfOrigin = scanner.nextLine();

                    PharmacyMedicine medicine = new PharmacyMedicine(pharmacyName, pharmacyAddress, pharmacyCity, directorFullName, medicineName, medicineType, medicinePrice, countryOfOrigin);
                    medicineList.addMedicine(medicine);
                    break;
                case 2:
                    medicineList.printMedicines();
                    break;
                case 3:
                    medicineList.sortMedicinesByName();
                    System.out.println("Medicines sorted by name.");
                    break;
                case 4:
                    System.out.print("Enter filename to save: ");
                    String saveFilename = scanner.nextLine();
                    medicineList.saveToFile(saveFilename);
                    System.out.println("Medicines saved to file.");
                    break;
                case 5:
                    System.out.print("Enter filename to load: ");
                    String loadFilename = scanner.nextLine();
                    medicineList.loadFromFile(loadFilename);
                    System.out.println("Medicines loaded from file.");
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