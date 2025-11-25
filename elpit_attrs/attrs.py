class WorkPlaces:
    
    def __init__(self, var_number: int):
        'Предпоследнее число зачетки'
        self.name: str = 'Число рабочих мест и серверов'
        self.all_values: list = [5, 8, 10, 12, 11, 9, 7, 15, 14, 13]
        self.current_value: int = self.all_values[var_number]
        self.unit: str = 'Nрм'
        
        
class AvgPower:
    
    def __init__(self, var_number: int):
        'Предпоследнее число зачетки'
        self.name: str = 'Средняя мощность на одно рабочее место'
        self.all_values: list = [200, 160, 180, 160, 200, 180, 240, 160, 180, 190]
        self.current_value: int = self.all_values[var_number]
        self.unit: str = 'P ср, Вт'


class PowerIndex:
    
    def __init__(self, var_number: int):
        'Предпоследнее число зачетки'
        self.name: str = 'Коэффициент мощности'
        self.all_values: list = [0.82, 0.8, 0.85, 0.84, 0.82, 0.85, 0.8, 0.85, 0.85, 0.84]
        self.current_value: float = self.all_values[var_number]
        self.unit: str = 'x'
      
        
class AvgUsing:
    
    def __init__(self, var_number: int):
        'Предпоследнее число зачетки'
        self.name: str = 'Среднее значение коэффициента использования'
        self.all_values: list = [0.9, 0.8, 0.8, 0.7, 0.7, 0.8, 0.9, 0.7, 0.7, 0.75]
        self.current_value: float = self.all_values[var_number]
        self.unit: str = 'Ки'


class AgeVoltage:
    
    def __init__(self, var_number: int):
        'Последнее число зачетки'
        self.name: str = 'Допустимые пределы изменения напряжения постоянного тока на вход аппаратуры'
        self.all_values: list = [5, 8, 10, 12, 11, 9, 7, 15, 14, 13]
        self.current_value: int = self.all_values[var_number]
        self.unit: str = 'Uимин..Uимакс'
        
        
class DCPower:
    
    def __init__(self, var_number: int):
        'Последнее число зачетки'
        self.name: str = 'Мощность потребляемая аппаратурой постоянного тока'
        self.all_values: list = [500, 100, 2000, 500, 1000, 2000, 1000, 300, 200, 300]
        self.current_value: int = self.all_values[var_number]
        self.unit: str = 'P ап., Вт'
        
        
class VoltageLost:
    
    def __init__(self, var_number: int):
        'Последнее число зачетки'
        self.name: str = 'Падение напряжения в ТРС'
        self.all_values: list = [1.0, 1.0, 0.8, 0.8, 0.9, 0.6, 0.6, 0.7, 1.0, 1.0]
        self.current_value: float = self.all_values[var_number]
        self.unit: str = 'ТРС, Uтрс'
        
        
class OuterTemp:
    
    def __init__(self, var_number: int):
        'Последнее число зачетки'
        self.name: str = 'Температура окружающей среды'
        self.all_values: list = [15, 20, 18, 15, 20, 17, 18, 20, 20, 20]
        self.current_value: float = self.all_values[var_number]
        self.unit: str = 'tокр, C'
        
        
class AvgUsing:
    
    def __init__(self, var_number: int):
        'Последнее число зачетки'
        self.name: str = 'Время автономной работы'
        self.all_values: list = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
        self.current_value: float = self.all_values[var_number]
        self.unit: str = 'tав'