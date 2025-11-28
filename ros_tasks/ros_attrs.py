from ros_tasks.ros_types import *


class SourceAttrsData:
    
    def __init__(self, name: str, 
                 value: 
                     Bit | 
                     KiloBit | 
                     MegaBit | 
                     GigaBit | 
                     BitBySecond | 
                     KiloBitBySecond | 
                     MegaBitBySecond | 
                     GigaBitBySecond | 
                     Byte | 
                     KiloByte | 
                     MegaByte | 
                     GigaByte | 
                     ByteBySecond | 
                     KiloByteBySecond | 
                     MegaByteBySecond | 
                     GigaByteBySecond | 
                     MilliSecond | 
                     MicroSecond | 
                     Second | 
                     Minute | 
                     MilliMetre | 
                     Metre | 
                     KiloMetre | 
                     MetreBySecond | 
                     KiloMetreBySecond | 
                     Satellite | 
                     FiberOptic | 
                     TwistedPair | 
                     Coefficient | 
                     NumberOfSubject | 
                     MessageByPocket | 
                     BitBySignal
                     ):
        """
        :param str name: Наименование переменной
        :param object value: Значение переменной. Писать не менее, чем с двумя знаками после точки (даже, если нули)
        """
        self.name: str = name
        self.value = value


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
        self.name: str = 'Заголовок сообщения'
        self.value: SourceAttrsData = SourceAttrsData(name=self.name, value=Byte(value=30.00))

    
class HeaderOfPocket:
    'hp (Заголовок пакета)'
    
    def __init__(self):
        self.name: str = 'Заголовок пакета'
        self.value: SourceAttrsData = SourceAttrsData(name=self.name, value=Byte(value=20.00))
        
        
class LightSpeed:
    'C (СКорость света в вакууме)'
    
    def __init__(self):
        self.name: str = 'Скорость света в вакууме'
        self.value: SourceAttrsData = SourceAttrsData(name=self.name, value=KiloMetreBySecond(value=300000.00))
        

class WMeansFileSize:
    '''
    W (Размер сообщения)\n
    Зависит от номера варианта'''
    
    def __init__(self, var_number: int):
        self.name: str = 'Размер сообщения'
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


class BasicPocketSize:
    '''
    MTU - Размер пакета
    '''
    
    def __init__(self, var_number: int):
        self.name: str = 'Размер пакета'
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


class MMeansFileShare:
    '''
    m - Количество файлов
    '''
    
    def __init__(self):
        self.name: str = 'Количество файлов'
        self.value: SourceAttrsData = SourceAttrsData(name=self.name, value=NumberOfSubject(value=100.00))
        
    def __str__(self):
        outer_text: str = f'{self.value} {self.name}'
        return outer_text


class PMeansTransitionReliability:
    '''
    p - Надежность передачи
    '''
    
    def __init__(self, var_number: int):
        self.name: str = 'Надежность передачи'
        self.all_values: list[float] = [
            0.99998, 
            0.999994, 
            0.999997, 
            0.999965, 
            0.99997, 
            0.99995, 
            0.99997, 
            0.99991, 
            0.999978, 
            0.9999, 
            0.9999994, 
            0.9999, 
            0.99997, 
            0.99994, 
            0.99999, 
            0.99996, 
            0.99999, 
            0.999994, 
            0.999994, 
            0.99997, 
            0.99996, 
            0.99997, 
            0.99997, 
            0.99992, 
            0.99991
        ]
        self.value: SourceAttrsData = SourceAttrsData(name=self.name, value=Coefficient(value=self.all_values[var_number-1]))
        
    def __str__(self):
        outer_text: str = f'{self.value} {self.name}'
        return outer_text


class ChannelLenght:
    '''
    L - Длина канала
    '''
    
    def __init__(self, var_number: int):
        self.name: str = 'Длина канала'
        self.all_values: list[float] = [
            400.0, 
            300.0, 
            850.0, 
            900.0, 
            650.0, 
            1050.0, 
            1400.0, 
            1250.0, 
            800.0, 
            1200.0, 
            700.0, 
            1000.0, 
            550.0, 
            500.0, 
            1300.0, 
            1350.0, 
            1450.0, 
            1150.0, 
            950.0, 
            750.0, 
            450.0, 
            350.0, 
            600.0, 
            1100.0, 
            1500.0, 
            400.0
        ]
        self.value: SourceAttrsData = SourceAttrsData(name=self.name, value=KiloMetre(value=self.all_values[var_number-1]))
        
    def __str__(self):
        outer_text: str = f'{self.value} {self.name}'
        return outer_text


class LightspeedCoefficient:
    '''
    k - Коэффициент скорости света
    '''
    
    def __init__(self, var_number: int):
        self.name: str = 'Коэффициент скорости света'
        self.all_values: list[float] = [
            0.7, 
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
        self.value: SourceAttrsData = SourceAttrsData(name=self.name, value=KiloMetreBySecond(value=self.all_values[var_number-1]))
        
    def __str__(self):
        outer_text: str = f'{self.value} {self.name}'
        return outer_text


class BasicPocketSize2:
    '''
    MTU - Размер пакета
    '''
    
    def __init__(self, var_number: int):
        self.name: str = 'Размер пакета'
        self.all_values: list = [
            1024.0, 
            1120.0, 
            1408.0, 
            1600.0, 
            1376.0, 
            1280.0, 
            1440.0, 
            1152.0, 
            1344.0, 
            1184.0, 
            1216.0, 
            1088.0, 
            1536.0, 
            1472.0, 
            1568.0, 
            1792.0, 
            1248.0, 
            1728.0, 
            1312.0, 
            1824.0, 
            1632.0, 
            1760.0, 
            1696.0, 
            1664.0, 
            1056.0, 
            1504.0
            ]
        self.value: SourceAttrsData = SourceAttrsData(name=self.name, value=Byte(value=self.all_values[var_number-1]))


class RequiredLightSpeed:
    '''
    V - Требуемая скорость света
    '''
    
    def __init__(self, var_number: int):
        self.name: str = 'Требуемая скорость света'
        self.all_values: list = [
            50000.0, 
            20480.0, 
            12288.0, 
            13312.0, 
            9216.0, 
            7168.0, 
            8192.0, 
            11264.0, 
            3072.0, 
            18432.0, 
            14336.0, 
            6144.0, 
            10240.0, 
            16384.0, 
            4096.0, 
            21504.0, 
            5120.0, 
            2048.0, 
            1024.0, 
            24576.0, 
            19456.0, 
            23552.0, 
            15360.0, 
            25600.0, 
            22528.0, 
            17408.0
            ]
        self.value: SourceAttrsData = SourceAttrsData(name=self.name, value=KiloBitBySecond(value=self.all_values[var_number-1]))


class ModulationType:
    '''
    Вид модуляции QAM
    '''
    
    def __init__(self, var_number: int):
        self.name: str = 'Вид модуляции'
        self.all_values: list = [
            '1024 QAM', 
            '512 QAM', 
            'BPSK', 
            '256 QAM', 
            '64 QAM', 
            '64 QAM', 
            'QPSK', 
            '128 QAM', 
            '128 QAM', 
            '256 QAM', 
            '1024 QAM', 
            '32 QAM', 
            '32 QAM', 
            '16 QAM', 
            '16 QAM', 
            'BPSK', 
            '64 QAM', 
            'QPSK', 
            '256 QAM', 
            '1024 QAM', 
            '8 QAM', 
            '512 QAM', 
            '128 QAM', 
            '32 QAM', 
            '16 QAM', 
            '8 QAM'
            ]
        self.value: str = self.all_values[var_number-1]


class SignalSpeed:
    '''
    ф - Сигнальная скорость
    '''
    
    def __init__(self, modulation_type: ModulationType):
        self.name: str = 'Вид модуляции'
        self.all_values: dict = {
            'BPSK': 1.0, 
            'QPSK': 2.0, 
            '8 QAM': 3.0, 
            '16 QAM': 4.0, 
            '32 QAM': 5.0, 
            '64 QAM': 6.0, 
            '128 QAM': 7.0, 
            '256 QAM': 8.0, 
            '512 QAM': 9.0, 
            '1024 QAM': 10.0
            }
        self.modulation_type_value: float = self.all_values.get(modulation_type.value)
        self.value: SourceAttrsData = SourceAttrsData(name=self.name, value=BitBySignal(value=self.modulation_type_value))


class Pocket:
    '''
    n - Количество пакетов
    '''
    
    def __init__(self, file_size: WMeansFileSize, pocket_size: BasicPocketSize):
        self.name: str = 'Пакет(-а/-ов)'
        self.value: float = check_float(value=self.count_pocket(file_size=file_size, pocket_size=pocket_size))
        
    def __str__(self):
        outer_text: str = f'{self.value} {self.name}'
        return outer_text
    
    def count_pocket(self, file_size: WMeansFileSize, pocket_size: BasicPocketSize):
        count_pocket: float = file_size.value.value.value / pocket_size.value.value.value
        
        return count_pocket


class PocketBySecond:
    '''
    N_пакетов - Количество пакетов в секунду
    '''
    
    def __init__(self, required_speed: RequiredLightSpeed, bit_by_ip_pocket: Bit):
        self.name: str = 'Пакет(-а/-ов) в секунду'
        self.value: float = check_float(value=self.count_pocket(required_speed=required_speed, bit_by_ip_pocket=bit_by_ip_pocket))
        
    def __str__(self):
        outer_text: str = f'{self.value} {self.name}'
        return outer_text
    
    def count_pocket(self, required_speed: RequiredLightSpeed, bit_by_ip_pocket: Bit):
        count_pocket: float = required_speed.value.value.to_bit_by_second().value / bit_by_ip_pocket.value
        
        return count_pocket


class PocketSpace:
    '''
    t_инт - Межпакетный интервал
    '''
    
    def __init__(self, required_speed: RequiredLightSpeed):
        self.name: str = 'Межпакетный интервал'
        self.all_values: list[dict] = [
            {'Скорость': MegaBitBySecond(value=10.0).to_bit_by_second(), 'Требуемое время': MicroSecond(value=9.6)}, 
            {'Скорость': MegaBitBySecond(value=100.0).to_bit_by_second(), 'Требуемое время': MicroSecond(value=0.96)}, 
            {'Скорость': GigaBitBySecond(value=1.0).to_bit_by_second(), 'Требуемое время': MicroSecond(value=0.096)}, 
            {'Скорость': GigaBitBySecond(value=10.0).to_bit_by_second(), 'Требуемое время': MicroSecond(value=0.0096)}
        ]
        self.current_time: MicroSecond = self.compare_speed(speed=BitBySecond(value=required_speed.value))
        self.value: SourceAttrsData = SourceAttrsData(name=self.name, value=self.current_time)
    
    def compare_speed(self, speed: BitBySecond):
        for index, value in enumerate(self.all_values, start=0):
            for value_key, value_value in value.items():
                if value_key == 'Скорость':
                    value_value: BitBySecond
                    if speed.value >= value_value.value:
                        continue
                    else: 
                        return self.all_values[index-1].get('Требуемое время')


class SignalByPocket:
    '''
    m_сиг/пакет - Сигналов на пакет
    '''
    
    def __init__(self, bit_by_ip_pocket: Bit, signal_speed: SignalSpeed):
        self.name: str = 'Сигналов на пакет'
        self.value: float = check_float(value=self.count_pocket(bit_by_ip_pocket=bit_by_ip_pocket, signal_speed=signal_speed))
        
    def __str__(self):
        outer_text: str = f'{self.value} {self.name}'
        return outer_text
    
    def count_pocket(self, bit_by_ip_pocket: Bit, signal_speed: SignalSpeed):
        count_pocket: float = bit_by_ip_pocket.value / (2.00**signal_speed.value.value.value)
        
        return count_pocket


class SignalBySecond:
    '''
    M_сиг - Общее количество сигналов
    '''
    
    def __init__(self, pocket_by_second: PocketBySecond, signal_by_pocket: SignalByPocket):
        self.name: str = 'Общее количество сигналов'
        self.value: float = check_float(value=self.count_pocket(pocket_by_second=pocket_by_second, signal_by_pocket=signal_by_pocket))
        
    def __str__(self):
        outer_text: str = f'{self.value} {self.name}'
        return outer_text
    
    def count_pocket(self, pocket_by_second: PocketBySecond, signal_by_pocket: SignalByPocket):
        count_pocket: float = pocket_by_second.value * signal_by_pocket.value
    
        return count_pocket


class Bod:
    '''
    B - Сигнальная скорость (в Бодах)
    '''
    
    def __init__(self, value: float=None, 
                 signal_by_second: SignalBySecond=None, 
                 distribution_time: Second=None, 
                 pocket_space: PocketSpace=None):
        self.name: str = 'Сигнальная скорость (в Бодах)'
        if value == None:
            self.value: float = check_float(value=self.count_signal_speed(
                signal_by_second=signal_by_second, distribution_time=distribution_time, pocket_space=pocket_space))
        else:
            self.value: float = value
        
    def __str__(self):
        outer_text: str = f'{self.value} {self.name}'
        return outer_text
    
    def count_signal_speed(self, signal_by_second: SignalBySecond, distribution_time: Second, pocket_space: PocketSpace):
        count_pocket: float = signal_by_second.value / (1.0-distribution_time.value-pocket_space.value.value.value)
    
        return count_pocket
    
    def to_mbod(self):
        outer_value: float = self.value / 1000000.0
        
        return MBod(value=outer_value)
    

class MBod:
    '''
    MBod - Сигнальная скорость (в мегабодах)
    '''
    
    def __init__(self, value: float):
        self.name: str = 'Сигнальная скорость (в Бодах)'
        self.value: float = check_float(value=value)
        
    def __str__(self):
        outer_text: str = f'{self.value} {self.name}'
        return outer_text
    
    def to_bod(self):
        outer_value: float = self.value * 1000000.0
        
        return Bod(value=outer_value)