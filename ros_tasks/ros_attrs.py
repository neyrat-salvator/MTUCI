from ros_tasks.ros_types import *


class SourceAttrsData:
    
    def __init__(self, name: str, value: object):
        """
        :param str name: Наименование переменной
        :param object value: Значение переменной. Писать не менее, чем с двумя знаками после точки (даже, если нули)
        """
        self.name: str = name
        self.value: object = value


class SourceHostToK:
    'Хост отправитель -> K'
    
    def __init__(self, var_number: int):
        self.name: str = 'Хост отправитель -> K'
        self.distance: SourceAttrsData = SourceAttrsData(name='Расстояние', value=Metre(value=100.00))
        self.transition_speed: SourceAttrsData = SourceAttrsData(name='Скорость передачи', value=KiloBitBySecond(value=64.00))
        self.channel_type: SourceAttrsData = SourceAttrsData(name='Тип линии', value=TwistedPair())
        self.all_values: list = [
            0.7, 
            0.69, 
            0.71, 
            0.7, 
            0.69, 
            0.72, 
            0.69, 
            0.69, 
            0.7, 
            0.7, 
            0.71, 
            0.68, 
            0.72, 
            0.71, 
            0.68, 
            0.71, 
            0.72, 
            0.68, 
            0.72, 
            0.72, 
            0.7, 
            0.68, 
            0.71, 
            0.69, 
            0.68
        ]
        self.value: SourceAttrsData = SourceAttrsData(name=self.name, value=Coefficient(value=self.all_values[var_number-1]))
        self.transition_time: MilliSecond = None
        self.distribution_time: MilliSecond = self.count_distr()
        
    def count_tran(self, size: Bit) -> MilliSecond:
        """Расчет времени передачи сообщения
        :param Bit size: Длина сущности"""
        transition_speed: KiloBitBySecond = self.transition_speed.value
        outer_value: MilliSecond = Second(value=(size.value / transition_speed.to_bit_by_second().value)).to_millisecond()
        self.transition_time: MilliSecond = outer_value
            
        return outer_value

    def count_distr(self) -> MilliSecond:
        """Расчет времени распространения. Оно уже посчитано в атрибуте self.distribution_time"""
        distance: Metre = self.distance.value
        coefficient: Coefficient = self.value.value
        channel_type: TwistedPair = self.channel_type.value
        outer_value: MilliSecond = Second(value=(distance.value / (coefficient.value * channel_type.value.value))).to_millisecond()
        
        return outer_value


class KToL:
    'K -> L'
    
    def __init__(self):
        self.name: str = 'K -> L'
        self.distance: SourceAttrsData = SourceAttrsData(name='Расстояние', value=KiloMetre(value=400.00))
        self.transition_speed: SourceAttrsData = SourceAttrsData(name='Скорость передачи', value=KiloBitBySecond(value=64.00))
        self.channel_type: SourceAttrsData = SourceAttrsData(name='Тип линии', value=TwistedPair())
        self.value: SourceAttrsData = SourceAttrsData(name=self.name, value=Coefficient(value=0.8))
        self.transition_time: MilliSecond = None
        self.distribution_time: MilliSecond = self.count_distr()
        
    def count_tran(self, size: Bit) -> MilliSecond:
        """Расчет времени передачи сообщения
        :param Bit size: Длина сущности"""
        transition_speed: KiloBitBySecond = self.transition_speed.value
        outer_value: MilliSecond = Second(value=(size.value / transition_speed.to_bit_by_second().value)).to_millisecond()
        self.transition_time: MilliSecond = outer_value
            
        return outer_value

    def count_distr(self) -> MilliSecond:
        """Расчет времени распространения. Оно уже посчитано в атрибуте self.distribution_time"""
        distance: Metre = self.distance.value
        coefficient: Coefficient = self.value.value
        channel_type: TwistedPair = self.channel_type.value
        outer_value: MilliSecond = Second(value=(distance.value / (coefficient.value * channel_type.value.value))).to_millisecond()
        
        return outer_value


class LToF:
    'L -> F'
    
    def __init__(self):
        self.name: str = 'L -> F'
        self.distance: SourceAttrsData = SourceAttrsData(name='Расстояние', value=KiloMetre(value=72000.00))
        self.transition_speed: SourceAttrsData = SourceAttrsData(name='Скорость передачи', value=KiloBitBySecond(value=2048.00))
        self.channel_type: SourceAttrsData = SourceAttrsData(name='Тип линии', value=Satellite())
        self.value: SourceAttrsData = SourceAttrsData(name=self.name, value=Coefficient(value=1.0))
        self.transition_time: MilliSecond = None
        self.distribution_time: MilliSecond = self.count_distr()
        
    def count_tran(self, size: Bit) -> MilliSecond:
        """Расчет времени передачи сообщения
        :param Bit size: Длина сущности"""
        transition_speed: KiloBitBySecond = self.transition_speed.value
        outer_value: MilliSecond = Second(value=(size.value / transition_speed.to_bit_by_second().value)).to_millisecond()
        self.transition_time: MilliSecond = outer_value
            
        return outer_value

    def count_distr(self) -> MilliSecond:
        """Расчет времени распространения. Оно уже посчитано в атрибуте self.distribution_time"""
        distance: Metre = self.distance.value
        coefficient: Coefficient = self.value.value
        channel_type: Satellite = self.channel_type.value
        outer_value: MilliSecond = Second(value=(distance.value / (coefficient.value * channel_type.value.value))).to_millisecond()
        
        return outer_value


class FToA:
    'F -> A'
    
    def __init__(self):
        self.name: str = 'F -> A'
        self.distance: SourceAttrsData = SourceAttrsData(name='Расстояние', value=KiloMetre(value=1450.00))
        self.transition_speed: SourceAttrsData = SourceAttrsData(name='Скорость передачи', value=KiloBitBySecond(value=512.00))
        self.channel_type: SourceAttrsData = SourceAttrsData(name='Тип линии', value=FiberOptic())
        self.value: SourceAttrsData = SourceAttrsData(name=self.name, value=Coefficient(value=0.69))
        self.transition_time: MilliSecond = None
        self.distribution_time: MilliSecond = self.count_distr()
        
    def count_tran(self, size: Bit) -> MilliSecond:
        """Расчет времени передачи сообщения
        :param Bit size: Длина сущности"""
        transition_speed: KiloBitBySecond = self.transition_speed.value
        outer_value: MilliSecond = Second(value=(size.value / transition_speed.to_bit_by_second().value)).to_millisecond()
        self.transition_time: MilliSecond = outer_value
            
        return outer_value

    def count_distr(self) -> MilliSecond:
        """Расчет времени распространения. Оно уже посчитано в атрибуте self.distribution_time"""
        distance: Metre = self.distance.value
        coefficient: Coefficient = self.value.value
        channel_type: FiberOptic = self.channel_type.value
        outer_value: MilliSecond = Second(value=(distance.value / (coefficient.value * channel_type.value.value))).to_millisecond()
        
        return outer_value


class AToDestinationHost:
    'A -> Хос получатель'
    
    def __init__(self, var_number: int):
        self.name: str = 'A -> Хос получатель'
        self.distance: SourceAttrsData = SourceAttrsData(name='Расстояние', value=Metre(value=100.00))
        self.transition_speed: SourceAttrsData = SourceAttrsData(name='Скорость передачи', value=KiloBitBySecond(value=64.00))
        self.channel_type: SourceAttrsData = SourceAttrsData(name='Тип линии', value=TwistedPair())
        self.all_values: list = [
            0.69, 
            0.72, 
            0.68, 
            0.69, 
            0.68, 
            0.71, 
            0.69, 
            0.68, 
            0.68, 
            0.69, 
            0.71, 
            0.72, 
            0.7, 
            0.69, 
            0.68, 
            0.72, 
            0.7, 
            0.72, 
            0.7, 
            0.71, 
            0.7, 
            0.7, 
            0.72, 
            0.71, 
            0.71
        ]
        self.value: SourceAttrsData = SourceAttrsData(name=self.name, value=Coefficient(value=self.all_values[var_number-1]))
        self.transition_time: MilliSecond = None
        self.distribution_time: MilliSecond = self.count_distr()
        
    def count_tran(self, size: Bit) -> MilliSecond:
        """Расчет времени передачи сообщения
        :param Bit size: Длина сущности"""
        transition_speed: KiloBitBySecond = self.transition_speed.value
        outer_value: MilliSecond = Second(value=(size.value / transition_speed.to_bit_by_second().value)).to_millisecond()
        self.transition_time: MilliSecond = outer_value
            
        return outer_value

    def count_distr(self) -> MilliSecond:
        """Расчет времени распространения. Оно уже посчитано в атрибуте self.distribution_time"""
        distance: Metre = self.distance.value
        coefficient: Coefficient = self.value.value
        channel_type: TwistedPair = self.channel_type.value
        outer_value: MilliSecond = Second(value=(distance.value / (coefficient.value * channel_type.value.value))).to_millisecond()
        
        return outer_value

        
class HeaderOfMessage:
    'hm (Заголовок сообщения)'
    
    def __init__(self):
        self.name: str = 'hm (Заголовок сообщения)'
        self.value: SourceAttrsData = SourceAttrsData(name=self.name, value=Byte(value=30.00))

    
class HeaderOfPocket:
    'hp (Заголовок пакета)'
    
    def __init__(self):
        self.name: str = 'hp (Заголовок пакета)'
        self.value: SourceAttrsData = SourceAttrsData(name=self.name, value=Byte(value=20.00))
        
        
class LightSpeed:
    'C (СКорость света в вакууме)'
    
    def __init__(self):
        self.name: str = 'C (Скорость света в вакууме)'
        self.value: SourceAttrsData = SourceAttrsData(name=self.name, value=KiloMetreBySecond(value=300000.00))
        

class WMeansFileSize:
    '''
    W (Размер сообщения)\n
    Зависит от номера варианта'''
    
    def __init__(self, var_number: int):
        self.name: str = 'W (Размер сообщения)'
        self.all_values: list = [
            10010.00, 
            39905.00,
            89570.00, 
            7680.00, 
            7500.00, 
            2540.00, 
            7680.00, 
            2540.00, 
            10240.00, 
            2540.00, 
            327675.00, 
            1480.00, 
            7500.00, 
            2720.00, 
            21760.00, 
            5030.00, 
            22320.00, 
            39905.00, 
            40830.00, 
            7500.00, 
            5030.00, 
            7460.00, 
            7500.00, 
            2880.00, 
            2560.00
            ]
        self.value: SourceAttrsData = SourceAttrsData(name=self.name, value=Byte(value=self.all_values[var_number-1]))


class MTUMeansPocketSize:
    '''
    MTU (Размер пакета)\n
    Зависит от номера варианта'''
    
    def __init__(self, var_number: int):
        self.name: str = 'MTU (Размер пакета)'
        self.all_values: list = [
            2002.00, 
            7981.00, 
            17914.00, 
            1536.00, 
            1500.00, 
            508.00, 
            1536.00, 
            508.00, 
            2048.00, 
            508.00, 
            65535.00, 
            296.00, 
            1500.00, 
            544.00, 
            4352.00, 
            1006.00, 
            4464.00, 
            7981.00, 
            8166.00, 
            1500.00, 
            1006.00, 
            1492.00, 
            1500.00, 
            576.00, 
            512.00
            ]
        self.value: SourceAttrsData = SourceAttrsData(name=self.name, value=Byte(value=self.all_values[var_number-1]))


class Pocket:
    
    def __init__(self, file_size: WMeansFileSize, pocket_size: MTUMeansPocketSize):
        self.name: str = 'Пакет(-а/-ов)'
        self.value: float = check_float(value=self.count_pocket(file_size=file_size, pocket_size=pocket_size))
        
    def __str__(self):
        outer_text: str = f'{self.value} {self.name}'
        return outer_text
    
    def count_pocket(self, file_size: WMeansFileSize, pocket_size: MTUMeansPocketSize):
        count_pocket: float = file_size.value.value.value / pocket_size.value.value.value
        
        return count_pocket