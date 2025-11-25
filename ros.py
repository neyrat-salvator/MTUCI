# Здесь вписать по варианту
w = 89570.00
hm = 30.00
# Тут последние 5 столбцов в таблице с вариантами
x1 = 0.71
x2 = 0.8
x3 =  1.00
x4 = 0.69
x5 = 0.68
# Тут просто расчеты
x1_len = 100.00 / 1000.00
x1_vel = 64.00 * 1000.00
x2_len = 400.00
x2_vel = 64.00 * 1000.00
x3_len = 72000.00
x3_vel = 2048.00 * 1000.00
x4_len = 1450.00
x4_vel = 512.00 * 1000.00
x5_len = 100.00 / 1000.00
x5_vel = 64.00 * 1000.00
v_distr_sc = 300000.00
v_distr_foc = 200000.00
v_distr_tp = 180000.00
Lbyte = w + hm
lb = Lbyte * 8.00
tran_list_global: list = []
distr_list_global: list = []
total_list: list = []

# Расчет передачи
def count_tran(x_vel):
    outer_value = (lb / x_vel) * 1000.00
    tran_list_global.append(outer_value)
        
    return outer_value

# Расчет распределения
def count_distr(x, x_len, v_distr):
    outer_value = (x_len / (x * v_distr)) * 1000.00
    distr_list_global.append(outer_value)
    
    return outer_value

# Суммирование с добавлением в итоговый лист
def sum_list(value_list: list):
    outer_sum = 0
    for value in value_list:
        outer_sum += value
        total_list.append(value)
    
    return outer_sum

x1_tran = count_tran(x_vel=x1_vel)
x2_tran = count_tran(x_vel=x2_vel)
x3_tran = count_tran(x_vel=x3_vel)
x4_tran = count_tran(x_vel=x4_vel)
x5_tran = count_tran(x_vel=x5_vel)
sum_tran = sum_list(value_list=tran_list_global)

x1_distr = count_distr(x=x1, x_len=x1_len, v_distr=v_distr_tp)
x2_distr = count_distr(x=x2, x_len=x2_len, v_distr=v_distr_tp)
x3_distr = count_distr(x=x3, x_len=x3_len, v_distr=v_distr_sc)
x4_distr = count_distr(x=x4, x_len=x4_len, v_distr=v_distr_foc)
x5_distr = count_distr(x=x5, x_len=x5_len, v_distr=v_distr_tp)
sum_distr = sum_list(value_list=distr_list_global)

total_sum = sum(tran_list_global+distr_list_global)
total_list.append(total_sum)

# Вывод в терминал
for value in total_list:
    print(f'{round(value, 4)}')