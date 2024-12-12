package src.LR.LR4;

import java.util.Arrays;
import java.util.List;

// Юрцук Константин Сергеевич
// Лабораторная работа №4
// Вариант: 26

/*6.2. Обработка текста

Дан текст. Текст разбит на слова, предполагается, что слово – это
группа символов, не содержащая пробелов и отдел􀉺нная пробелами от
других слов. Текст может содержать и несколько предложений, признаком
конца предложения является точка. Составить программу для обработки
текстовой информации по поставленному условию.

Текст содержит наряду с другой информацией целые числа. Опреде-
лить самое большое и самое маленькое целое число.
*/

public class LR4 {

    // Метод для преобразования текста в число
    static int writeNumberFromListString(List<String> stringNumber, int value) {

        // Проверка на наличие числа на входе
        if (stringNumber.get(value) != "") {
            int numberFromListString = Integer.parseInt(stringNumber.get(value));
            return numberFromListString;
        } else {
            return 0;
        }
    }

    // Основной метод класса
    public static void main(String[] args) {

        // Исходные данные для алгоритма

        // Текст, откуда будут искаться числа
        String text = "Какой-то текст и цифры в нём 5";
        // 2, 3, 100, 6, 10, 1, 2

        // начальные значения максимального и минимального числа
        int maxNumber = 0;
        int minNumber = 0;

        // Переменная для контроля значений в цикле
        int i;

        // Удаление всех символов кроме чисел
        text = text.replaceAll("[^0-9]+", " ");

        // Формирования списка из полученных чисел со знаком-разделителем в виде пробела
        List<String> newText = Arrays.asList(text.trim().split(" "));

        // Цикл с реализацией нужного алгоритма
        for (i = 0, maxNumber = 0, minNumber = 0; i <= (newText.size() - 1); i++) {

            // Инициирование переменной, в которую записывается рассматриваемое преобразованное число из текста в заданном списке
            int cycleNumber = writeNumberFromListString(newText, i);

            // Проверка на индекс цикла для дальнейшей проверки записи числа
            if (i != 0) {
                if (maxNumber <= cycleNumber) {
                    maxNumber = cycleNumber;
                }
                if (minNumber >= cycleNumber) {
                    minNumber = cycleNumber;
                }
            } else {
                maxNumber = cycleNumber;
                minNumber = cycleNumber;
            }
        }

        // Вывод искомых чисел
        System.out.println("Самое большое число: " + maxNumber);
        System.out.println("Самое маленькое число: " + minNumber);
    }
}