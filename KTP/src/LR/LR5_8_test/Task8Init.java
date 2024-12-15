package src.LR.LR5_8_test;

import java.util.ArrayList;
import java.util.List;

class TelevisionProgram {
    private String name;
    private String time;

    public TelevisionProgram(String name, String time) {
        this.name = name;
        this.time = time;
    }

    public String getName() {
        return name;
    }

    public String getTime() {
        return time;
    }

    public void printDetails() {
        System.out.println("Наименование: " + name + ", Время: " + time);
    }
}

class EducationalProgram extends TelevisionProgram {
    private String scienceField;

    public EducationalProgram(String name, String time, String scienceField) {
        super(name, time);
        this.scienceField = scienceField;
    }
    
    public String getScienceField() {
        return scienceField;
    }

    @Override
    public void printDetails() {
        super.printDetails();
        System.out.println("Область науки: " + scienceField);
    }
}

class KidsProgram extends TelevisionProgram {
    private int minAge;
    private int maxAge;

    public KidsProgram(String name, String time, int minAge, int maxAge) {
        super(name, time);
        this.minAge = minAge;
        this.maxAge = maxAge;
    }
    
    public int getMinAge() {
        return minAge;
    }

    public int getMaxAge() {
        return maxAge;
    }

    @Override
    public void printDetails() {
        super.printDetails();
        System.out.println("Минимальный возраст: " + minAge + ", Максимальный возраст: " + maxAge);
    }
}

class ShowProgram extends TelevisionProgram {
    private String theme;

    public ShowProgram(String name, String time, String theme) {
        super(name, time);
        this.theme = theme;
    }
    
    public String getTheme() {
        return theme;
    }

    @Override
    public void printDetails() {
        super.printDetails();
        System.out.println("Тема шоу: " + theme);
    }
}

class MovieProgram extends TelevisionProgram {
    private String description;
    private int year;

    public MovieProgram(String name, String time, String description, int year) {
        super(name, time);
        this.description = description;
        this.year = year;
    }
    
    public String getDescription() {
        return description;
    }

    public int getYear() {
        return year;
    }

    @Override
    public void printDetails() {
        super.printDetails();
        System.out.println("Описание: " + description + ", Год выпуска: " + year);
    }
}
