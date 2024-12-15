package src.LR.LR5_8_test;

import javax.swing.*;
import javax.swing.table.DefaultTableModel;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Comparator;
import java.util.List;

public class Task8Main {    
	private TelevisionSchedule schedule;

    public Task8Main() {
        schedule = new TelevisionSchedule();
        
        schedule.addProgram(new EducationalProgram("Наука и мы", "10:00", "Физика"));
        schedule.addProgram(new KidsProgram("Детская сказка", "12:00", 3, 7));
        schedule.addProgram(new ShowProgram("Ток-шоу", "14:00", "Звезды кино"));
        schedule.addProgram(new MovieProgram("Приключенческий фильм", "20:00", "Захватывающее приключение", 2022));
    }
    
    public void start() {
        JFrame frame = new JFrame("Телевизионное расписание");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(600, 400);

        JTabbedPane tabbedPane = new JTabbedPane();

        tabbedPane.addTab("Просмотр", createViewPanel());
        tabbedPane.addTab("Добавление", createAddPanel());

        frame.add(tabbedPane);
        frame.setVisible(true);
    }

    private JPanel createViewPanel() {
       JPanel panel = new JPanel(new BorderLayout());

        String[] columnNames = {"Название", "Время", "Тип", "Дополнительно"};
        DefaultTableModel tableModel = new DefaultTableModel(columnNames, 0);
        JTable table = new JTable(tableModel);

        JComboBox<String> sortOptions = new JComboBox<>(new String[]{"По времени", "По названию"});
        JButton refreshButton = new JButton("Обновить расписание");

        refreshButton.addActionListener(e -> {
            String selectedSort = (String) sortOptions.getSelectedItem();
            tableModel.setRowCount(0);

            List<TelevisionProgram> programs = schedule.getPrograms();
            if ("По времени".equals(selectedSort)) {
                programs.sort(Comparator.comparing(TelevisionProgram::getTime));
            } else if ("По названию".equals(selectedSort)) {
                programs.sort(Comparator.comparing(TelevisionProgram::getName));
            }

            for (TelevisionProgram program : programs) {
                if (program instanceof EducationalProgram) {
                    EducationalProgram ep = (EducationalProgram) program;
                    tableModel.addRow(new Object[]{ep.getName(), ep.getTime(), "Educational", ep.getScienceField()});
                } else if (program instanceof KidsProgram) {
                    KidsProgram kp = (KidsProgram) program;
                    tableModel.addRow(new Object[]{kp.getName(), kp.getTime(), "Kids", kp.getMinAge() + " - " + kp.getMaxAge()});
                } else if (program instanceof ShowProgram) {
                    ShowProgram sp = (ShowProgram) program;
                    tableModel.addRow(new Object[]{sp.getName(), sp.getTime(), "Show", sp.getTheme()});
                } else if (program instanceof MovieProgram) {
                    MovieProgram mp = (MovieProgram) program;
                    tableModel.addRow(new Object[]{mp.getName(), mp.getTime(), "Movie", mp.getDescription() + ", " + mp.getYear()});
                }
            }
        });

        panel.add(new JScrollPane(table), BorderLayout.CENTER);

        JPanel topPanel = new JPanel();
        topPanel.add(new JLabel("Сортировать:"));
        topPanel.add(sortOptions);
        topPanel.add(refreshButton);
        panel.add(topPanel, BorderLayout.NORTH);

        refreshButton.doClick();

        return panel;
    }

    private JPanel createAddPanel() {
        JPanel panel = new JPanel(new BorderLayout());

        JPanel fieldsPanel = new JPanel(new GridLayout(0, 2));
        JLabel nameLabel = new JLabel("Название:");
        JTextField nameField = new JTextField();

        JLabel timeLabel = new JLabel("Время:");
        JTextField timeField = new JTextField();

        JLabel typeLabel = new JLabel("Тип:");
        JComboBox<String> typeComboBox = new JComboBox<>(new String[]{"Educational", "Kids", "Show", "Movie"});

        JPanel dynamicPanel = new JPanel(new GridLayout(0, 2));

        typeComboBox.addActionListener(e -> {
            dynamicPanel.removeAll();
            String selectedType = (String) typeComboBox.getSelectedItem();
            if ("Educational".equals(selectedType)) {
                dynamicPanel.add(new JLabel("Область науки:"));
                dynamicPanel.add(new JTextField());
            } else if ("Kids".equals(selectedType)) {
                dynamicPanel.add(new JLabel("Мин. возраст:"));
                dynamicPanel.add(new JTextField());
                dynamicPanel.add(new JLabel("Макс. возраст:"));
                dynamicPanel.add(new JTextField());
            } else if ("Show".equals(selectedType)) {
                dynamicPanel.add(new JLabel("Тема шоу:"));
                dynamicPanel.add(new JTextField());
            } else if ("Movie".equals(selectedType)) {
                dynamicPanel.add(new JLabel("Описание:"));
                dynamicPanel.add(new JTextField());
                dynamicPanel.add(new JLabel("Год выпуска:"));
                dynamicPanel.add(new JTextField());
            }
            dynamicPanel.revalidate();
            dynamicPanel.repaint();
        });

        JButton addButton = new JButton("Добавить");
        addButton.addActionListener(e -> {
            try {
                String name = nameField.getText();
                String time = timeField.getText();
                String type = (String) typeComboBox.getSelectedItem();

                if (name.isEmpty() || time.isEmpty()) {
                    throw new IllegalArgumentException("Название и время не могут быть пустыми.");
                }

                Component[] components = dynamicPanel.getComponents();
                if ("Educational".equals(type)) {
                    String scienceField = ((JTextField) components[1]).getText();
                    if (scienceField.isEmpty()) {
                        throw new IllegalArgumentException("Область науки должна быть заполнена.");
                    }
                    schedule.addProgram(new EducationalProgram(name, time, scienceField));
                } else if ("Kids".equals(type)) {
                    int minAge;
                    int maxAge;
                    try {
                        minAge = Integer.parseInt(((JTextField) components[1]).getText());
                        maxAge = Integer.parseInt(((JTextField) components[3]).getText());
                    } catch (NumberFormatException ex) {
                        throw new IllegalArgumentException("Мин. и Макс. возраст должны быть числами.");
                    }
                    schedule.addProgram(new KidsProgram(name, time, minAge, maxAge));
                } else if ("Show".equals(type)) {
                    String theme = ((JTextField) components[1]).getText();
                    if (theme.isEmpty()) {
                        throw new IllegalArgumentException("Тема шоу должна быть заполнена.");
                    }
                    schedule.addProgram(new ShowProgram(name, time, theme));
                } else if ("Movie".equals(type)) {
                    String description = ((JTextField) components[1]).getText();
                    int year;
                    try {
                        year = Integer.parseInt(((JTextField) components[3]).getText());
                    } catch (NumberFormatException ex) {
                        throw new IllegalArgumentException("Год выпуска должен быть числом.");
                    }
                    schedule.addProgram(new MovieProgram(name, time, description, year));
                }

                nameField.setText("");
                timeField.setText("");
                for (Component component : components) {
                    if (component instanceof JTextField) {
                        ((JTextField) component).setText("");
                    }
                }
            } catch (IllegalArgumentException ex) {
                JOptionPane.showMessageDialog(panel, ex.getMessage(), "Ошибка", JOptionPane.ERROR_MESSAGE);
            }
        });

        fieldsPanel.add(nameLabel);
        fieldsPanel.add(nameField);
        fieldsPanel.add(timeLabel);
        fieldsPanel.add(timeField);
        fieldsPanel.add(typeLabel);
        fieldsPanel.add(typeComboBox);

        panel.add(fieldsPanel, BorderLayout.NORTH);
        panel.add(dynamicPanel, BorderLayout.CENTER);
        panel.add(addButton, BorderLayout.SOUTH);

        typeComboBox.setSelectedIndex(0);

        return panel;
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            new Task8Main().start();
        });
    }
}
