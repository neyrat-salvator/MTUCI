from ros_tasks.floaterror import check_float


class Bit:
    
    def __init__(self, value: float):
        self.name: str = 'Бит(-а)'
        self.value: float = check_float(value=value)
        
    def __str__(self):
        outer_text: str = f'{self.value} {self.name}'
        return outer_text
        
    def to_byte(self):
        converted_value: float = self.value / 8.00
        return Byte(value=converted_value)
    
    def to_kilobit(self):
        converted_value: float = self.value / 1000.00
        return KiloBit(value=converted_value)
    
    def to_kilobyte(self):
        converted_value: float = self.value / (8.00 * 1000.00)
        return KiloByte(value=converted_value)
    
    def to_megabit(self):
        converted_value: float = self.value / 1000000.00
        return MegaBit(value=converted_value)
    
    def to_megabyte(self):
        converted_value: float = self.value / (8.00 * 1000000.00)
        return MegaByte(value=converted_value)
    
    def to_gigabit(self):
        converted_value: float = self.value / 1000000000.00
        return GigaBit(value=converted_value)
    
    def to_gigabyte(self):
        converted_value: float = self.value / (8.00 * 1000000000.00)
        return GigaByte(value=converted_value)


class KiloBit:
    
    def __init__(self, value: float):
        self.name: str = 'Килобит(-а)'
        self.value: float = check_float(value=value)
        
    def __str__(self):
        outer_text: str = f'{self.value} {self.name}'
        return outer_text
        
    def to_bit(self):
        converted_value: float = self.value * 1000.00
        return Bit(value=converted_value)
    
    def to_byte(self):
        converted_value: float = (self.value * 1000.00) / 8.00
        return Byte(value=converted_value)
    
    def to_kilobyte(self):
        converted_value: float = self.value / 8.00
        return KiloByte(value=converted_value)
    
    def to_megabit(self):
        converted_value: float = self.value / 1000.00
        return MegaBit(value=converted_value)
    
    def to_megabyte(self):
        converted_value: float = self.value / (8.00 * 1000.00)
        return MegaByte(value=converted_value)
    
    def to_gigabit(self):
        converted_value: float = self.value / 1000000.00
        return GigaBit(value=converted_value)
    
    def to_gigabyte(self):
        converted_value: float = self.value / (8.00 * 1000000.00)
        return GigaByte(value=converted_value)


class MegaBit:
    
    def __init__(self, value: float):
        self.name: str = 'Мегабит(-а)'
        self.value: float = check_float(value=value)
        
    def __str__(self):
        outer_text: str = f'{self.value} {self.name}'
        return outer_text
        
    def to_bit(self):
        converted_value: float = self.value * 1000000.00
        return Bit(value=converted_value)
    
    def to_byte(self):
        converted_value: float = (self.value * 1000000.00) / 8.00
        return Byte(value=converted_value)
    
    def to_kilobit(self):
        converted_value: float = self.value * 1000.00
        return KiloBit(value=converted_value)
    
    def to_kilobyte(self):
        converted_value: float = (self.value * 1000.00) / 8.00
        return KiloByte(value=converted_value)
    
    def to_megabyte(self):
        converted_value: float = self.value * 8.00
        return MegaByte(value=converted_value)
    
    def to_gigabit(self):
        converted_value: float = self.value / 1000.00
        return GigaBit(value=converted_value)
    
    def to_gigabyte(self):
        converted_value: float = self.value / (8.00 * 1000.00)
        return GigaByte(value=converted_value)


class GigaBit:
    
    def __init__(self, value: float):
        self.name: str = 'Гигабит(-а)'
        self.value: float = check_float(value=value)
        
    def __str__(self):
        outer_text: str = f'{self.value} {self.name}'
        return outer_text
        
    def to_bit(self):
        converted_value: float = self.value * 1000000000.00
        return Bit(value=converted_value)
    
    def to_byte(self):
        converted_value: float = (self.value * 1000000000.00) / 8.00
        return Byte(value=converted_value)
    
    def to_kilobit(self):
        converted_value: float = self.value * 1000000.00
        return KiloBit(value=converted_value)
    
    def to_kilobyte(self):
        converted_value: float = (self.value * 1000000.00) / 8.00
        return KiloByte(value=converted_value)
    
    def to_megabit(self):
        converted_value: float = self.value * 1000.00
        return MegaBit(value=converted_value)
    
    def to_megabyte(self):
        converted_value: float = (self.value * 1000.00) / 8.00
        return MegaByte(value=converted_value)
    
    
class Byte:
    
    def __init__(self, value: float):
        self.name: str = 'Байт(-а)'
        self.value: float = check_float(value=value)
        
    def __str__(self):
        outer_text: str = f'{self.value} {self.name}'
        return outer_text
    
    def to_bit(self):
        converted_value: float = self.value * 8.00
        return Bit(value=converted_value)
       
    def to_kilobit(self):
        converted_value: float = (self.value * 8.00) / 1000.00
        return KiloBit(value=converted_value)
    
    def to_kilobyte(self):
        converted_value: float = self.value / 1024.00
        return KiloByte(value=converted_value)
    
    def to_megabit(self):
        converted_value: float = (self.value * 8.00) / 1000000.00
        return MegaBit(value=converted_value)
    
    def to_megabyte(self):
        converted_value: float = self.value / (1024.00 * 1024.00)
        return MegaByte(value=converted_value)
    
    def to_gigabit(self):
        converted_value: float = (self.value * 8.00) / 1000000000.00
        return GigaBit(value=converted_value)
    
    def to_gigabyte(self):
        converted_value: float = self.value / (1024.00 * 1024.00 * 1024.00)
        return GigaByte(value=converted_value)


class KiloByte:
    
    def __init__(self, value: float):
        self.name: str = 'Килобайт(-а)'
        self.value: float = check_float(value=value)
        
    def __str__(self):
        outer_text: str = f'{self.value} {self.name}'
        return outer_text
    
    def to_bit(self):
        converted_value: float = self.value * 8.00 * 1024.00
        return Bit(value=converted_value)
    
    def to_byte(self):
        converted_value: float = self.value / 1024.00
        return Byte(value=converted_value)
        
    def to_kilobit(self):
        converted_value: float = self.value * 8.00
        return KiloBit(value=converted_value)
    
    def to_megabit(self):
        converted_value: float = (self.value * 8.00) / 1000.00
        return MegaBit(value=converted_value)
    
    def to_megabyte(self):
        converted_value: float = self.value / 1024.00
        return MegaByte(value=converted_value)
    
    def to_gigabit(self):
        converted_value: float = (self.value * 8.00) / 1000000.00
        return GigaBit(value=converted_value)
    
    def to_gigabyte(self):
        converted_value: float = self.value / (1024.00 * 1024.00)
        return GigaByte(value=converted_value)


class MegaByte:
    
    def __init__(self, value: float):
        self.name: str = 'Мегабайт(-а)'
        self.value: float = check_float(value=value)
        
    def __str__(self):
        outer_text: str = f'{self.value} {self.name}'
        return outer_text
    
    def to_bit(self):
        converted_value: float = self.value * 8.00 * 1024.00 * 1024.00
        return Bit(value=converted_value)
    
    def to_byte(self):
        converted_value: float = self.value * 1024.00 * 1024.00
        return Byte(value=converted_value)
    
    def to_kilobit(self):
        converted_value: float = self.value * 8.00 * 1024.00
        return KiloBit(value=converted_value)
    
    def to_kilobyte(self):
        converted_value: float = self.value * 8.00 * 1024.00
        return KiloByte(value=converted_value)
    
    def to_megabit(self):
        converted_value: float = self.value * 8.00
        return MegaBit(value=converted_value)
    
    def to_gigabit(self):
        converted_value: float = (self.value * 8.00) / 1000.00
        return GigaBit(value=converted_value)
    
    def to_gigabyte(self):
        converted_value: float = self.value / 1024.00
        return GigaByte(value=converted_value)


class GigaByte:
    
    def __init__(self, value: float):
        self.name: str = 'Гигабайт(-а)'
        self.value: float = check_float(value=value)
        
    def __str__(self):
        outer_text: str = f'{self.value} {self.name}'
        return outer_text
    
    def to_bit(self):
        converted_value: float = self.value * 8.00 * 1024.00 * 1024.00 * 1024.00
        return Bit(value=converted_value)
    
    def to_byte(self):
        converted_value: float = self.value * 1024.00 * 1024.00 * 1024.00
        return Byte(value=converted_value)
        
    def to_kilobit(self):
        converted_value: float = self.value * 8.00 * 1024.00 * 1024.00
        return KiloBit(value=converted_value)
    
    def to_kilobyte(self):
        converted_value: float = self.value * 1024.00 * 1024.00
        return KiloByte(value=converted_value)
    
    def to_megabit(self):
        converted_value: float = self.value * 8.00 * 1024.00
        return MegaBit(value=converted_value)
    
    def to_megabyte(self):
        converted_value: float = self.value * 1024.00
        return MegaByte(value=converted_value)
    
    def to_gigabit(self):
        converted_value: float = self.value * 8.00
        return GigaBit(value=converted_value)


class BitBySecond:
    
    def __init__(self, value: float):
        self.name: str = 'Бит(-а) в секунду'
        self.value: float = check_float(value=value)
        
    def __str__(self):
        outer_text: str = f'{self.value} {self.name}'
        return outer_text
    
    def to_byte_by_second(self):
        converted_value: float = self.value / 8.00
        return ByteBySecond(value=converted_value)
    
    def to_kilobit_by_second(self):
        converted_value: float = self.value / 1000.0
        return KiloBitBySecond(value=converted_value)
    
    def to_kilobyte_by_second(self):
        converted_value: float = self.value / (8.00 * 1000.00)
        return KiloByteBySecond(value=converted_value)
    
    def to_megabit_by_second(self):
        converted_value: float = self.value / 1000000.0
        return MegaBitBySecond(value=converted_value)
    
    def to_megabyte_by_second(self):
        converted_value: float = self.value / (8.00 * 1000000.00)
        return MegaByteBySecond(value=converted_value)
    
    def to_gigabit_by_second(self):
        converted_value: float = self.value / 1000000000.0
        return GigaBitBySecond(value=converted_value)
    
    def to_gigabyte_by_second(self):
        converted_value: float = self.value / (8.00 * 1000000000.00)
        return GigaByteBySecond(value=converted_value)


class KiloBitBySecond:
    
    def __init__(self, value: float):
        self.name: str = 'Килобит(-а) в секунду'
        self.value: float = check_float(value=value)
        
    def __str__(self):
        outer_text: str = f'{self.value} {self.name}'
        return outer_text
    
    def to_bit_by_second(self):
        converted_value: float = self.value * 1000.0
        return BitBySecond(value=converted_value)
    
    def to_byte_by_second(self):
        converted_value: float = (self.value * 1000.00) / 8.00
        return ByteBySecond(value=converted_value)
    
    def to_kilobyte_by_second(self):
        converted_value: float = self.value / 8.00
        return KiloByteBySecond(value=converted_value)
    
    def to_megabit_by_second(self):
        converted_value: float = self.value / 1000.0
        return MegaBitBySecond(value=converted_value)
    
    def to_megabyte_by_second(self):
        converted_value: float = self.value / (8.00 * 1000.00)
        return MegaByteBySecond(value=converted_value)
    
    def to_gigabit_by_second(self):
        converted_value: float = self.value / 1000000.0
        return GigaBitBySecond(value=converted_value)
    
    def to_gigabyte_by_second(self):
        converted_value: float = self.value / (8.00 * 1000000.00)
        return GigaByteBySecond(value=converted_value)


class MegaBitBySecond:
    
    def __init__(self, value: float):
        self.name: str = 'Мегабит(-а) в секунду'
        self.value: float = check_float(value=value)
        
    def __str__(self):
        outer_text: str = f'{self.value} {self.name}'
        return outer_text
    
    def to_bit_by_second(self):
        converted_value: float = self.value * 1000000.0
        return BitBySecond(value=converted_value)
    
    def to_byte_by_second(self):
        converted_value: float = (self.value * 1000000.00) / 8.00
        return ByteBySecond(value=converted_value)
    
    def to_kilobit_by_second(self):
        converted_value: float = self.value * 1000.0
        return KiloBitBySecond(value=converted_value)
    
    def to_kilobyte_by_second(self):
        converted_value: float = (self.value * 1000.00) / 8.00
        return KiloByteBySecond(value=converted_value)
    
    def to_megabyte_by_second(self):
        converted_value: float = self.value / 8.00
        return KiloByteBySecond(value=converted_value)
    
    def to_gigabit_by_second(self):
        converted_value: float = self.value / 1000.0
        return GigaBitBySecond(value=converted_value)
    
    def to_gigabyte_by_second(self):
        converted_value: float = self.value / (8.00 * 1000.00)
        return GigaByteBySecond(value=converted_value)


class GigaBitBySecond:
    
    def __init__(self, value: float):
        self.name: str = 'Гигабит(-а) в секунду'
        self.value: float = check_float(value=value)
        
    def __str__(self):
        outer_text: str = f'{self.value} {self.name}'
        return outer_text
    
    def to_bit_by_second(self):
        converted_value: float = self.value * 1000000000.0
        return BitBySecond(value=converted_value)
    
    def to_byte_by_second(self):
        converted_value: float = (self.value * 1000000000.00) / 8.00
        return ByteBySecond(value=converted_value)
    
    def to_kilobit_by_second(self):
        converted_value: float = self.value * 1000000.0
        return KiloBitBySecond(value=converted_value)
    
    def to_kilobyte_by_second(self):
        converted_value: float = (self.value * 1000000.00) / 8.00
        return KiloByteBySecond(value=converted_value)
    
    def to_megabit_by_second(self):
        converted_value: float = self.value * 1000.0
        return MegaBitBySecond(value=converted_value)
    
    def to_megabyte_by_second(self):
        converted_value: float = (self.value * 1000.0) / 8.00
        return KiloByteBySecond(value=converted_value)
    
    def to_gigabyte_by_second(self):
        converted_value: float = self.value / 8.00
        return GigaByteBySecond(value=converted_value)


class ByteBySecond:
    
    def __init__(self, value: float):
        self.name: str = 'Байт(-а) в секунду'
        self.value: float = check_float(value=value)
        
    def __str__(self):
        outer_text: str = f'{self.value} {self.name}'
        return outer_text
    
    def to_bit_by_second(self):
        converted_value: float = self.value * 8.00
        return BitBySecond(value=converted_value)
       
    def to_kilobit_by_second(self):
        converted_value: float = (self.value * 8.00) / 1000.00
        return KiloBitBySecond(value=converted_value)
    
    def to_kilobyte_by_second(self):
        converted_value: float = self.value / 1024.00
        return KiloByteBySecond(value=converted_value)
    
    def to_megabit_by_second(self):
        converted_value: float = (self.value * 8.00) / 1000000.00
        return MegaBit(value=converted_value)
    
    def to_megabyte_by_second(self):
        converted_value: float = self.value / (1024.00 * 1024.00)
        return MegaByte(value=converted_value)
    
    def to_gigabit_by_second(self):
        converted_value: float = (self.value * 8.00) / 1000000000.00
        return GigaBitBySecond(value=converted_value)
    
    def to_gigabyte_by_second(self):
        converted_value: float = self.value / (1024.00 * 1024.00 * 1024.00)
        return GigaByteBySecond(value=converted_value)
    

class KiloByteBySecond:
    
    def __init__(self, value: float):
        self.name: str = 'Килобайт(-а) в секунду'
        self.value: float = check_float(value=value)
        
    def __str__(self):
        outer_text: str = f'{self.value} {self.name}'
        return outer_text
    
    def to_bit_by_second(self):
        converted_value: float = self.value * 8.00 * 1024.00
        return BitBySecond(value=converted_value)
    
    def to_byte_by_second(self):
        converted_value: float = self.value / 1024.00
        return ByteBySecond(value=converted_value)
        
    def to_kilobit_by_second(self):
        converted_value: float = self.value * 8.00
        return KiloBitBySecond(value=converted_value)
    
    def to_megabit_by_second(self):
        converted_value: float = (self.value * 8.00) / 1000.00
        return MegaBitBySecond(value=converted_value)
    
    def to_megabyte_by_second(self):
        converted_value: float = self.value / 1024.00
        return MegaByteBySecond(value=converted_value)
    
    def to_gigabit_by_second(self):
        converted_value: float = (self.value * 8.00) / 1000000.00
        return GigaBitBySecond(value=converted_value)
    
    def to_gigabyte_by_second(self):
        converted_value: float = self.value / (1024.00 * 1024.00)
        return GigaByteBySecond(value=converted_value)


class MegaByteBySecond:
    
    def __init__(self, value: float):
        self.name: str = 'Мегабайт(-а) в секунду'
        self.value: float = check_float(value=value)
        
    def __str__(self):
        outer_text: str = f'{self.value} {self.name}'
        return outer_text
    
    def to_bit_by_second(self):
        converted_value: float = self.value * 8.00 * 1024.00 * 1024.00
        return BitBySecond(value=converted_value)
    
    def to_byte_by_second(self):
        converted_value: float = self.value * 1024.00 * 1024.00
        return ByteBySecond(value=converted_value)
    
    def to_kilobit_by_second(self):
        converted_value: float = self.value * 8.00 * 1024.00
        return KiloBitBySecond(value=converted_value)
    
    def to_kilobyte_by_second(self):
        converted_value: float = self.value * 8.00 * 1024.00
        return KiloByteBySecond(value=converted_value)
    
    def to_megabit_by_second(self):
        converted_value: float = self.value * 8.00
        return MegaBitBySecond(value=converted_value)
    
    def to_gigabit_by_second(self):
        converted_value: float = (self.value * 8.00) / 1000.00
        return GigaBitBySecond(value=converted_value)
    
    def to_gigabyte_by_second(self):
        converted_value: float = self.value / 1024.00
        return GigaByteBySecond(value=converted_value)


class GigaByteBySecond:
    
    def __init__(self, value: float):
        self.name: str = 'Гигабайт(-а)'
        self.value: float = check_float(value=value)
        
    def __str__(self):
        outer_text: str = f'{self.value} {self.name}'
        return outer_text
    
    def to_bit_by_second(self):
        converted_value: float = self.value * 8.00 * 1024.00 * 1024.00 * 1024.00
        return BitBySecond(value=converted_value)
    
    def to_byte_by_second(self):
        converted_value: float = self.value * 1024.00 * 1024.00 * 1024.00
        return ByteBySecond(value=converted_value)
        
    def to_kilobit_by_second(self):
        converted_value: float = self.value * 8.00 * 1024.00 * 1024.00
        return KiloBitBySecond(value=converted_value)
    
    def to_kilobyte_by_second(self):
        converted_value: float = self.value * 1024.00 * 1024.00
        return KiloByteBySecond(value=converted_value)
    
    def to_megabit_by_second(self):
        converted_value: float = self.value * 8.00 * 1024.00
        return MegaBitBySecond(value=converted_value)
    
    def to_megabyte_by_second(self):
        converted_value: float = self.value * 1024.00
        return MegaByteBySecond(value=converted_value)
    
    def to_gigabit_by_second(self):
        converted_value: float = self.value * 8.00
        return GigaBitBySecond(value=converted_value)


class MicroSecond:
    
    def __init__(self, value: float):
        self.name: str = 'Микросекунд(-а/-ы)'
        self.value: float = check_float(value=value)
        
    def __str__(self):
        outer_text: str = f'{self.value} {self.name}'
        return outer_text
    
    def to_millisecond(self):
        converted_value: float = self.value / 1000.00
        return MilliSecond(value=converted_value)
       
    def to_second(self):
        converted_value: float = self.value / 1000000.00
        return Second(value=converted_value)
    
    def to_minute(self):
        converted_value: float = self.value / 60000000.00
        return Minute(value=converted_value)


class MilliSecond:
    
    def __init__(self, value: float):
        self.name: str = 'Миллисекунд(-а/-ы)'
        self.value: float = check_float(value=value)
        
    def __str__(self):
        outer_text: str = f'{self.value} {self.name}'
        return outer_text
            
    def to_microsecond(self):
        converted_value: float = self.value * 1000.00
        return MicroSecond(value=converted_value)
    
    def to_second(self):
        converted_value: float = self.value / 1000.00
        return Second(value=converted_value)
    
    def to_minute(self):
        converted_value: float = self.value / 60000.00
        return Minute(value=converted_value)


class Second:
    
    def __init__(self, value: float):
        self.name: str = 'Секунд(-а/-ы)'
        self.value: float = check_float(value=value)
        
    def __str__(self):
        outer_text: str = f'{self.value} {self.name}'
        return outer_text
            
    def to_microsecond(self):
        converted_value: float = self.value * 1000000.00
        return MicroSecond(value=converted_value)
    
    def to_millisecond(self):
        converted_value: float = self.value * 1000.00
        return MilliSecond(value=converted_value)
    
    def to_minute(self):
        converted_value: float = self.value / 60.00
        return Minute(value=converted_value)


class Minute:
    
    def __init__(self, value: float):
        self.name: str = 'Минут(-а/-ы)'
        self.value: float = check_float(value=value)
        
    def __str__(self):
        outer_text: str = f'{self.value} {self.name}'
        return outer_text
    
    def to_microsecond(self):
        converted_value: float = self.value * 60000000.00
        return MicroSecond(value=converted_value)
    
    def to_millisecond(self):
        converted_value: float = self.value * 60000.00
        return MilliSecond(value=converted_value)
    
    def to_second(self):
        converted_value: float = self.value * 60.00
        return Second(value=converted_value)


class MilliMetre:
    
    def __init__(self, value: float):
        self.name: str = 'Миллиметр(-а)'
        self.value: float = check_float(value=value)
        
    def __str__(self):
        outer_text: str = f'{self.value} {self.name}'
        return outer_text
            
    def to_metere(self):
        converted_value: float = self.value / 1000.00
        return Metre(value=converted_value)
    
    def to_kilometre(self):
        converted_value: float = self.value / 1000000.00
        return KiloMetre(value=converted_value)


class Metre:
    
    def __init__(self, value: float):
        self.name: str = 'Метр(-а)'
        self.value: float = check_float(value=value)
        
    def __str__(self):
        outer_text: str = f'{self.value} {self.name}'
        return outer_text
            
    def to_millimetere(self):
        converted_value: float = self.value * 1000.00
        return MilliMetre(value=converted_value)
    
    def to_kilometre(self):
        converted_value: float = self.value / 1000.00
        return KiloMetre(value=converted_value)


class KiloMetre:
    
    def __init__(self, value: float):
        self.name: str = 'Километр(-а)'
        self.value: float = check_float(value=value)
        
    def __str__(self):
        outer_text: str = f'{self.value} {self.name}'
        return outer_text
            
    def to_metere(self):
        converted_value: float = self.value * 1000.00
        return Metre(value=converted_value)
    
    def to_millimetre(self):
        converted_value: float = self.value * 1000000.00
        return MilliMetre(value=converted_value)


class MetreBySecond:
    
    def __init__(self, value: float):
        self.name: str = 'Метр(-а) в секунду'
        self.value: float = check_float(value=value)
        
    def __str__(self):
        outer_text: str = f'{self.value} {self.name}'
        return outer_text
    
    def to_kilometere_by_second(self):
        converted_value: float = self.value / 1000.00
        return KiloMetreBySecond(value=converted_value)


class KiloMetreBySecond:
    
    def __init__(self, value: float):
        self.name: str = 'Километр(-а) в секунду'
        self.value: float = check_float(value=value)
        
    def __str__(self):
        outer_text: str = f'{self.value} {self.name}'
        return outer_text
    
    def to_metere_by_second(self):
        converted_value: float = self.value * 1000.00
        return MetreBySecond(value=converted_value)


class Satellite:
    
    def __init__(self):
        self.name: str = 'Спутниковая связь'
        self.value: KiloMetreBySecond = KiloMetreBySecond(value=300000.00)
        
    def __str__(self):
        outer_text: str = f'{self.value} {self.name}'
        return outer_text


class FiberOptic:
    
    def __init__(self):
        self.name: str = 'Оптоволокно'
        self.value: KiloMetreBySecond = KiloMetreBySecond(value=200000.00)
        
    def __str__(self):
        outer_text: str = f'{self.value} {self.name}'
        return outer_text


class TwistedPair:
    
    def __init__(self):
        self.name: str = 'Витая пара'
        self.value: KiloMetreBySecond = KiloMetreBySecond(value=180000.00)
        
    def __str__(self):
        outer_text: str = f'{self.value} {self.name}'
        return outer_text


class Coefficient:
    
    def __init__(self, value: float):
        self.name: str = 'Коэффициент'
        self.value: float = check_float(value=value)
        
    def __str__(self):
        outer_text: str = f'{self.value} {self.name}'
        return outer_text


class NumberOfSubject:
    
    def __init__(self, value: float):
        self.name: str = 'Штук(-а/-и)'
        self.value: float = check_float(value=value) // 1
        
    def __str__(self):
        outer_text: str = f'{self.value} {self.name}'
        return outer_text


class MessageByPocket:
    
    def __init__(self, value: float):
        self.name: str = 'Сообщение на пакет'
        self.value: float = check_float(value=value)
        
    def __str__(self):
        outer_text: str = f'{self.value} {self.name}'
        return outer_text


class BitBySignal:
    
    def __init__(self, value: float):
        self.name: str = 'Бит на сигнал'
        self.value: float = check_float(value=value)
        
    def __str__(self):
        outer_text: str = f'{self.value} {self.name}'
        return outer_text