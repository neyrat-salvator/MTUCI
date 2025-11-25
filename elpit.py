from student import Student
from elpit_attrs.attrs import *


class Elpit:
    
    def __init__(self, student: Student):
        self.discipline_name: str = 'Электропитание устройств и систем инфокоммуникаций'
        self.variants: GradeBookAttrs = GradeBookAttrs(grade_book=student.grade_book)
        self.work_place: WorkPlaces = WorkPlaces(var_number=self.variants.pre_last_symbol)
        self.avg_power: AvgPower = AvgPower(var_number=self.variants.pre_last_symbol)
        self.power_index: PowerIndex = PowerIndex(var_number=self.variants.pre_last_symbol)
        self.avg_using: AvgUsing = AvgUsing(var_number=self.variants.pre_last_symbol)
        self.age_voltage: AgeVoltage = AgeVoltage(var_number=self.variants.last_symbol)
        self.dc_power: DCPower = DCPower(var_number=self.variants.last_symbol)
        self.voltage_lost: VoltageLost = VoltageLost(var_number=self.variants.last_symbol)
        self.outer_temp: OuterTemp = OuterTemp(var_number=self.variants.last_symbol)
        self.avg_using: AvgUsing = AvgUsing(var_number=self.variants.last_symbol)
        
    def __str__(self):
        outer_text: str = f'Выбраны следующие параметры:\n'
        print(f'')
        for attr_key, attr_value in vars(self).items():
            outer_text += f'\n{attr_key}: {attr_value}'
        
        return outer_text
    

class GradeBookAttrs:
    
    def __init__(self, grade_book: str):
        self.pre_last_symbol: int = int(grade_book[-1])
        self.last_symbol: int = int(grade_book[0])