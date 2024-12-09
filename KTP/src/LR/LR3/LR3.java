package src.LR.LR3;
// Юрцук Константин Сергеевич
// Лабораторная работа №1
// Вариант: 26

/*1.10. Вычисление функции разложением её в ряд

Составить программу нахождения суммы ряда с заданной точностью
eps. Использовать рекуррентные соотношения при вычислении очередного
элемента ряда. Предусмотреть вычисление по контрольной формуле.
Суммы рассматриваемых рядов конечны для значений x, абсолютная
величина которых меньше единицы, причем сумма начальных элементов
ряда отличается от суммы бесконечного ряда на величину, которая не пре-
восходит абсолютной величины eps. Абсолютная величина суммы всех
отброшенных членов ряда меньше eps.*/

public class LR3 {
    static int factorial(int n) {
        int res = 1, i;
        for (i = 2; i <= n; i++) {
            res *= i;
        }
        return res;
    }

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