from ros_tasks.ros_attrs import *
from ros_tasks.ros_types import *


class ROSTask1:
    
    def __init__(self, variant: int):
        self.variant: int = variant
        self.lightspeed: LightSpeed = LightSpeed()
        self.w: WMeansFileSize = WMeansFileSize(var_number=self.variant)
        self.hp: HeaderOfPocket = HeaderOfPocket()
        self.hm: HeaderOfMessage = HeaderOfMessage()
        self.shtk: SourceHostToK = SourceHostToK(var_number=self.variant)
        self.ktl: KToL = KToL()
        self.ltf: LToF = LToF()
        self.fta: FToA = FToA()
        self.atdh: AToDestinationHost = AToDestinationHost(var_number=self.variant)
        self.message_size: Bit = Byte(value=(self.w.value.value.value + self.hm.value.value.value)).to_bit()
        self.shtk.count_tran(size=self.message_size)
        self.ktl.count_tran(size=self.message_size)
        self.ltf.count_tran(size=self.message_size)
        self.fta.count_tran(size=self.message_size)
        self.atdh.count_tran(size=self.message_size)
        self.total_list_transition: list[float] = [
            self.shtk.transition_time.value, 
            self.ktl.transition_time.value, 
            self.ltf.transition_time.value, 
            self.fta.transition_time.value, 
            self.atdh.transition_time.value
        ]
        self.total_transition: MilliSecond = MilliSecond(value=sum(self.total_list_transition))
        self.total_list_distribution: list[float] = [
            self.shtk.distribution_time.value, 
            self.ktl.distribution_time.value, 
            self.ltf.distribution_time.value, 
            self.fta.distribution_time.value, 
            self.atdh.distribution_time.value
        ]
        self.total_distribution: MilliSecond = MilliSecond(value=sum(self.total_list_distribution))
        self.total_delay: MilliSecond = MilliSecond(value=sum([
            self.total_distribution.value, 
            self.total_transition.value
            ]))
        
    def __str__(self):
        outer_text: str = f"""Параметры задачи №1:
        
        1. Вариант: {self.variant}
        2. Скорость света: {round(number=self.lightspeed.value.value.value, ndigits=4)} {self.lightspeed.value.value.name}
        3. Размер файла: {round(number=self.w.value.value.value, ndigits=4)} {self.w.value.value.name}
        4. Длина сообщения: {round(number=self.message_size.value, ndigits=4)} {self.message_size.name}
        5. Размер заголовка пакета: {round(number=self.hp.value.value.value, ndigits=4)} {self.hp.value.value.name}
        6. Размер заголовка сообщения: {round(number=self.hm.value.value.value, ndigits=4)} {self.hm.value.value.name}
        7. Параметры для узла от источника до точке K:
        - Время передачи: {round(number=self.shtk.transition_time.value, ndigits=4)} {self.shtk.transition_time.name}
        - Время распространения: {round(number=self.shtk.distribution_time.value, ndigits=4)} {self.shtk.distribution_time.name}
        8. Параметры для узла от точки K до точки L:
        - Время передачи: {round(number=self.ktl.transition_time.value, ndigits=4)} {self.ktl.transition_time.name}
        - Время распространения: {round(number=self.ktl.distribution_time.value, ndigits=4)} {self.ktl.distribution_time.name}
        9. Параметры для узла от точки L до точки F:
        - Время передачи: {round(number=self.ltf.transition_time.value, ndigits=4)} {self.ltf.transition_time.name}
        - Время распространения: {round(number=self.ltf.distribution_time.value, ndigits=4)} {self.ltf.distribution_time.name}
        10. Параметры для узла от точки F до точки A:
        - Время передачи: {round(number=self.fta.transition_time.value, ndigits=4)} {self.fta.transition_time.name}
        - Время распространения: {round(number=self.fta.distribution_time.value, ndigits=4)} {self.fta.distribution_time.name}
        11. Параметры для узла от точки A до получателя:
        - Время передачи: {round(number=self.atdh.transition_time.value, ndigits=4)} {self.atdh.transition_time.name}
        - Время распространения: {round(number=self.atdh.distribution_time.value, ndigits=4)} {self.atdh.distribution_time.name}
        12. Общее время передачи: {round(number=self.total_transition.value, ndigits=4)} {self.total_transition.name}
        13. Общее время распространения: {round(number=self.total_distribution.value, ndigits=4)} {self.total_distribution.name}
        14. Общее время задержки: {round(number=self.total_delay.value, ndigits=4)} {self.total_delay.name}
        """
        
        return outer_text


class ROSTask2:
    
    def __init__(self, variant: int):
        self.variant: int = variant
        self.lightspeed: LightSpeed = LightSpeed()
        self.w: WMeansFileSize = WMeansFileSize(var_number=self.variant)
        self.mtu: MTUMeansPocketSize = MTUMeansPocketSize(var_number=self.variant)
        self.count_pocket: Pocket = Pocket(file_size=self.w, pocket_size=self.mtu)
        self.hp: HeaderOfPocket = HeaderOfPocket()
        self.hm: HeaderOfMessage = HeaderOfMessage()
        self.shtk: SourceHostToK = SourceHostToK(var_number=self.variant)
        self.ktl: KToL = KToL()
        self.ltf: LToF = LToF()
        self.fta: FToA = FToA()
        self.atdh: AToDestinationHost = AToDestinationHost(var_number=self.variant)
        self.message_size: Bit = Byte(value=(self.w.value.value.value + self.hm.value.value.value)).to_bit()
        self.pocket_size: Bit = Byte(value=(self.mtu.value.value.value + self.hp.value.value.value)).to_bit()
        self.shtk.count_tran(size=self.pocket_size)
        self.ktl.count_tran(size=self.pocket_size)
        self.ltf.count_tran(size=self.pocket_size)
        self.fta.count_tran(size=self.pocket_size)
        self.atdh.count_tran(size=self.pocket_size)
        self.total_list_transition: list[float] = [
            self.shtk.transition_time.value, 
            self.ktl.transition_time.value, 
            self.ltf.transition_time.value, 
            self.fta.transition_time.value, 
            self.atdh.transition_time.value
        ]
        self.total_transition: MilliSecond = MilliSecond(value=sum(self.total_list_transition))
        self.total_list_distribution: list[float] = [
            self.shtk.distribution_time.value, 
            self.ktl.distribution_time.value, 
            self.ltf.distribution_time.value, 
            self.fta.distribution_time.value, 
            self.atdh.distribution_time.value
        ]
        self.total_distribution: MilliSecond = MilliSecond(value=sum(self.total_list_distribution))
        self.total_delay: MilliSecond = MilliSecond(value=sum([
            self.total_distribution.value, 
            self.total_transition.value
            ]))
        self.most_slowly_pocket_time: MilliSecond = MilliSecond(value=max(self.total_list_transition))
        self.most_slowly_pocket_transition_time: MilliSecond = MilliSecond(value=self.count_max_value(values=self.total_list_transition))
        self.longest_time_transition: MilliSecond = MilliSecond(value=sum([
            self.most_slowly_pocket_transition_time.value, 
            self.total_transition.value
            ]))
        self.total_time_file_transition: MilliSecond = MilliSecond(value=sum([
            self.longest_time_transition.value, 
            self.total_distribution.value
        ]))
        
    def __str__(self):
        outer_text: str = f"""Параметры задачи №2:
        
        1. Вариант: {self.variant}
        2. Скорость света: {round(number=self.lightspeed.value.value.value, ndigits=4)} {self.lightspeed.value.value.name}
        3. Размер файла: {round(number=self.w.value.value.value, ndigits=4)} {self.w.value.value.name}
        4. Размер пакета: {round(number=self.mtu.value.value.value, ndigits=4)} {self.mtu.value.value.name}
        5. Количество пакетов: {round(number=self.count_pocket.value, ndigits=4)} 
        6. Длина сообщения: {round(number=self.message_size.value, ndigits=4)} {self.message_size.name}
        7. Длина пакета: {round(number=self.pocket_size.value, ndigits=4)} {self.pocket_size.name}
        8. Размер заголовка пакета: {round(number=self.hp.value.value.value, ndigits=4)} {self.hp.value.value.name}
        9. Размер заголовка сообщения: {round(number=self.hm.value.value.value, ndigits=4)} {self.hm.value.value.name}
        10. Параметры для узла от источника до точке K:
        - Время передачи: {round(number=self.shtk.transition_time.value, ndigits=4)} {self.shtk.transition_time.name}
        - Время распространения: {round(number=self.shtk.distribution_time.value, ndigits=4)} {self.shtk.distribution_time.name}
        11. Параметры для узла от точки K до точки L:
        - Время передачи: {round(number=self.ktl.transition_time.value, ndigits=4)} {self.ktl.transition_time.name}
        - Время распространения: {round(number=self.ktl.distribution_time.value, ndigits=4)} {self.ktl.distribution_time.name}
        12. Параметры для узла от точки L до точки F:
        - Время передачи: {round(number=self.ltf.transition_time.value, ndigits=4)} {self.ltf.transition_time.name}
        - Время распространения: {round(number=self.ltf.distribution_time.value, ndigits=4)} {self.ltf.distribution_time.name}
        13. Параметры для узла от точки F до точки A:
        - Время передачи: {round(number=self.fta.transition_time.value, ndigits=4)} {self.fta.transition_time.name}
        - Время распространения: {round(number=self.fta.distribution_time.value, ndigits=4)} {self.fta.distribution_time.name}
        14. Параметры для узла от точки A до получателя:
        - Время передачи: {round(number=self.atdh.transition_time.value, ndigits=4)} {self.atdh.transition_time.name}
        - Время распространения: {round(number=self.atdh.distribution_time.value, ndigits=4)} {self.atdh.distribution_time.name}
        15. Общее время передачи: {round(number=self.total_transition.value, ndigits=4)} {self.total_transition.name}
        16. Общее время распространения: {round(number=self.total_distribution.value, ndigits=4)} {self.total_distribution.name}
        17. Общее время задержки: {round(number=self.total_delay.value, ndigits=4)} {self.total_delay.name}
        18. Наиболее медленный пакет: {round(number=self.most_slowly_pocket_time.value, ndigits=4)} {self.most_slowly_pocket_time.name}
        19. Наиболее медленная передача пакетов: {round(number=self.most_slowly_pocket_transition_time.value, ndigits=4)} {self.most_slowly_pocket_transition_time.name}
        20. Общее время передачи пакетов: {round(number=self.longest_time_transition.value, ndigits=4)} {self.longest_time_transition.name}
        21. Общее время передачи файла: {round(number=self.total_time_file_transition.value, ndigits=4)} {self.total_time_file_transition.name}
        """

        return outer_text
    
    def count_max_value(self, values: list[float]):
        outer_value: float = (self.count_pocket.value-1.00)*max(values)
        
        return outer_value