package src.LR.LR2;
import java.util.Arrays;
// Юрцук Константин Сергеевич
// Лабораторная работа №2
// Вариант: 26

/*2.2. Обработка массива с ветвлением в теле цикла

Разработать программу вычисления требуемой величины на основе
заданного одномерного массива. Имейте в виду, что в некоторых задачах
возможны несколько вариантов ответов.*/

public class LR2 {
    public static void main(String[] args) {
        double [] X = {1, 6, 3, 4, 5};
        double [] Y = new double [5];
        int i = 0;
        int count_X = 0;

        for (i = 0; i <= (X.length - 1); i++) {
            System.out.println(X[i]);
            
            if (X[i] <= 0) {
                Y[i] = 0;
            }
            else if (X[i] > 0) {
                Y[i] = Math.pow(X[i], 2);
            }

            if (X[i] == 0) {
                count_X++;
            }

            System.out.println("Вывод значений в итерации: " + "\nX: " + X[i] + "\nY: " + Y[i]);

        }

        System.out.println("Вывод количества X, ранвых нулю: " + count_X);
        

        // System.out.printf("Сумма ряда: %.6f\n", sum);
        // System.out.printf("Контрольная формула: %.6f\n", control);
    }
}