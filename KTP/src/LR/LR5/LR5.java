package src.LR.LR5;
// Юрцук Константин Сергеевич
// Лабораторная работа №4 НАСЛЕДОВАНИЕ И ПОЛИМОРФИЗМ
// Вариант: 1 (26)

/*Реализовать предметную область:
1 Записная книжка. Создать родительский класс «Событие» (дата, время) и дочерние классы:
- «День рождения» (именинник, место проведения праздника и возраст);
- «Встреча» (человек с которым назначена встреча и место встречи);
- «Другое» (описание).
Реализовать класс для хранения списка событий с методом добавления события и методом печати списка событий.*/

public class LR5 {
    public static void main(String[] args) {
        double x = 0.5;
        double eps = Math.E;

        double sum = 0;
        double term;
        int n = 1;

        do {
            term = ((2 * n * Math.pow(x, (4 * n + 2))) / factorial(2 * n + 1));
            sum += term;
            n++;
        } while (Math.abs(term) > eps);

        double control = (Math.sin(Math.pow(x, 2)) - Math.pow(x, 2) * Math.cos(Math.pow(x, 2)));

        System.out.printf("Сумма ряда: %.6f\n", sum);
        System.out.printf("Контрольная формула: %.6f\n", control);
    }
}