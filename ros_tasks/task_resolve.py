from ros_tasks.ros_attrs import *
from ros_tasks.ros_types import *


class ROSTask1:
    
    def __init__(self, variant: int):
        self.variant: int = variant
        self.task_number: int = 1
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
        outer_text: str = f"""Параметры задачи №{self.task_number}:
        
        1. Вариант: {self.variant}
        2. {self.lightspeed.name}: {round(number=self.lightspeed.value.value.value, ndigits=4)} {self.lightspeed.value.value.name}
        3. {self.w.name}: {round(number=self.w.value.value.value, ndigits=4)} {self.w.value.value.name}
        4. Длина сообщения: {round(number=self.message_size.value, ndigits=4)} {self.message_size.name}
        5. {self.hp.name}: {round(number=self.hp.value.value.value, ndigits=4)} {self.hp.value.value.name}
        6. {self.hm.name}: {round(number=self.hm.value.value.value, ndigits=4)} {self.hm.value.value.name}
        7. {self.shtk.name}:
        - Время передачи: {round(number=self.shtk.transition_time.value, ndigits=4)} {self.shtk.transition_time.name}
        - Время распространения: {round(number=self.shtk.distribution_time.value, ndigits=4)} {self.shtk.distribution_time.name}
        8. {self.ktl.name}:
        - Время передачи: {round(number=self.ktl.transition_time.value, ndigits=4)} {self.ktl.transition_time.name}
        - Время распространения: {round(number=self.ktl.distribution_time.value, ndigits=4)} {self.ktl.distribution_time.name}
        9. {self.ltf.name}:
        - Время передачи: {round(number=self.ltf.transition_time.value, ndigits=4)} {self.ltf.transition_time.name}
        - Время распространения: {round(number=self.ltf.distribution_time.value, ndigits=4)} {self.ltf.distribution_time.name}
        10. {self.fta.name}:
        - Время передачи: {round(number=self.fta.transition_time.value, ndigits=4)} {self.fta.transition_time.name}
        - Время распространения: {round(number=self.fta.distribution_time.value, ndigits=4)} {self.fta.distribution_time.name}
        11. {self.atdh.name}:
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
        self.task_number: int = 2
        self.lightspeed: LightSpeed = LightSpeed()
        self.w: WMeansFileSize = WMeansFileSize(var_number=self.variant)
        self.mtu: BasicPocketSize = BasicPocketSize(var_number=self.variant)
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
        outer_text: str = f"""Параметры задачи №{self.task_number}:
        
        1. Вариант: {self.variant}
        2. {self.lightspeed.name}: {round(number=self.lightspeed.value.value.value, ndigits=4)} {self.lightspeed.value.value.name}
        3. {self.w.name}: {round(number=self.w.value.value.value, ndigits=4)} {self.w.value.value.name}
        4. {self.mtu.name}: {round(number=self.mtu.value.value.value, ndigits=4)} {self.mtu.value.value.name}
        5. {self.count_pocket.name}: {round(number=self.count_pocket.value, ndigits=4)} 
        6. Длина сообщения: {round(number=self.message_size.value, ndigits=4)} {self.message_size.name}
        7. Длина пакета: {round(number=self.pocket_size.value, ndigits=4)} {self.pocket_size.name}
        8. {self.hp.name}: {round(number=self.hp.value.value.value, ndigits=4)} {self.hp.value.value.name}
        9. {self.hm.name}: {round(number=self.hm.value.value.value, ndigits=4)} {self.hm.value.value.name}
        10. {self.shtk.name}:
        - Время передачи: {round(number=self.shtk.transition_time.value, ndigits=4)} {self.shtk.transition_time.name}
        - Время распространения: {round(number=self.shtk.distribution_time.value, ndigits=4)} {self.shtk.distribution_time.name}
        11. {self.ktl.name}:
        - Время передачи: {round(number=self.ktl.transition_time.value, ndigits=4)} {self.ktl.transition_time.name}
        - Время распространения: {round(number=self.ktl.distribution_time.value, ndigits=4)} {self.ktl.distribution_time.name}
        12. {self.ltf.name}:
        - Время передачи: {round(number=self.ltf.transition_time.value, ndigits=4)} {self.ltf.transition_time.name}
        - Время распространения: {round(number=self.ltf.distribution_time.value, ndigits=4)} {self.ltf.distribution_time.name}
        13. {self.fta.name}:
        - Время передачи: {round(number=self.fta.transition_time.value, ndigits=4)} {self.fta.transition_time.name}
        - Время распространения: {round(number=self.fta.distribution_time.value, ndigits=4)} {self.fta.distribution_time.name}
        14. {self.atdh.name}:
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


class ROSTask3(ROSTask1):
    
    def __init__(self, variant: int):
        super().__init__(variant=variant)
        self.task_number: int = 3
        self.m: MMeansFileShare = MMeansFileShare()
        self.p: PMeansTransitionReliability = PMeansTransitionReliability(var_number=self.variant)
        self.w: WMeansFileSize = WMeansFileSize(var_number=self.variant)
        self.mtu: BasicPocketSize = BasicPocketSize(var_number=self.variant)
        self.count_pocket: Pocket = Pocket(file_size=self.w, pocket_size=self.mtu)
        self.hp: HeaderOfPocket = HeaderOfPocket()
        self.hm: HeaderOfMessage = HeaderOfMessage()
        self.message_size: Bit = Byte(value=(self.w.value.value.value + self.hm.value.value.value)).to_bit()
        self.pocket_size: Bit = Byte(value=(self.mtu.value.value.value + self.hp.value.value.value)).to_bit()
        self.ctgmt: MessageByPocket = self.chance_to_guarantee_transition(size=self.message_size)
        self.ctgpt: MessageByPocket = self.chance_to_guarantee_transition(size=self.pocket_size)
        self.total_count_transmitted_messages: NumberOfSubject = NumberOfSubject(value=(self.m.value.value.value / self.ctgmt.value))
        self.pocket_number_by_one_recipient: NumberOfSubject = NumberOfSubject(value=(self.w.value.value.value / self.mtu.value.value.value))
        self.total_count_of_pocket: NumberOfSubject = NumberOfSubject(value=(self.m.value.value.value * self.count_pocket.value))
        self.total_count_transmitted_pocket: NumberOfSubject = NumberOfSubject(value=(self.total_count_of_pocket.value / self.ctgpt.value))
        self.total_message_transition_time: MilliSecond = MilliSecond(value=(self.total_count_transmitted_messages.value * self.total_transition.value))
        self.transition_speed_list: list[float] = [
            self.shtk.transition_speed.value.to_bit_by_second().value, 
            self.ktl.transition_speed.value.to_bit_by_second().value, 
            self.ltf.transition_speed.value.to_bit_by_second().value, 
            self.fta.transition_speed.value.to_bit_by_second().value, 
            self.atdh.transition_speed.value.to_bit_by_second().value
        ]
        self.one_pocket_transition_time: MilliSecond = Second(value=(self.pocket_size.value / min(self.transition_speed_list))).to_millisecond()
        self.total_pocket_transition_time: MilliSecond = MilliSecond(value=(self.total_count_transmitted_pocket.value * self.one_pocket_transition_time.value))
        self.total_saved_time_second: Second = MilliSecond(value=(self.total_message_transition_time.value - self.total_pocket_transition_time.value)).to_second()
        self.total_saved_time_minute: Minute = MilliSecond(value=(self.total_message_transition_time.value - self.total_pocket_transition_time.value)).to_minute()
        
    def __str__(self):
        outer_text: str = f"""Параметры задачи №{self.task_number}:
        
        1. Вариант: {self.variant}
        2. {self.m.name}: {round(number=self.m.value.value.value, ndigits=4)} {self.m.value.value.name}
        3. {self.p.name}: {round(number=self.p.value.value.value, ndigits=4)} {self.p.value.value.name}
        3. {self.w.name}: {round(number=self.w.value.value.value, ndigits=4)} {self.w.value.value.name}
        4. {self.mtu.name}: {round(number=self.mtu.value.value.value, ndigits=4)} {self.mtu.value.value.name}
        5. {self.count_pocket.name}: {round(number=self.count_pocket.value, ndigits=4)} 
        6. Длина сообщения: {round(number=self.message_size.value, ndigits=4)} {self.message_size.name}
        7. Длина пакета: {round(number=self.pocket_size.value, ndigits=4)} {self.pocket_size.name}
        8. {self.hp.name}: {round(number=self.hp.value.value.value, ndigits=4)} {self.hp.value.value.name}
        9. {self.hm.name}: {round(number=self.hm.value.value.value, ndigits=4)} {self.hm.value.value.name}
        10. Шанс гарантированной доставки сообщения: {round(number=self.ctgmt.value, ndigits=4)} {self.ctgmt.name}
        11. Шанс гарантированной доставки пакета: {round(number=self.ctgpt.value, ndigits=4)} {self.ctgpt.name}
        12. Общее число переданных сообщений: {round(number=self.total_count_transmitted_messages.value, ndigits=4)} {self.total_count_transmitted_messages.name}
        13. Количество пакетов на одного получателя: {round(number=self.pocket_number_by_one_recipient.value, ndigits=4)} {self.pocket_number_by_one_recipient.name}
        14. Общее количество пакетов: {round(number=self.total_count_of_pocket.value, ndigits=4)} {self.total_count_of_pocket.name}
        15. Общее число переданных пакетов: {round(number=self.total_count_transmitted_pocket.value, ndigits=4)} {self.total_count_transmitted_pocket.name}
        16. Время передачи одного сообщения: {round(number=self.total_transition.value, ndigits=4)} {self.total_transition.name}
        17. Общее время передачи сообщений: {round(number=self.total_message_transition_time.value, ndigits=4)} {self.total_message_transition_time.name}
        18. Время передачи одного пакета: {round(number=self.one_pocket_transition_time.value, ndigits=4)} {self.one_pocket_transition_time.name}
        19. Общее время передачи пакетов: {round(number=self.total_pocket_transition_time.value, ndigits=4)} {self.total_pocket_transition_time.name}
        20. Экономия времени передачи (секунд): {round(number=self.total_saved_time_second.value, ndigits=4)} {self.total_saved_time_second.name}
        21. Экономия времени передачи (минут): {round(number=self.total_saved_time_minute.value, ndigits=4)} {self.total_saved_time_minute.name}
        """

        return outer_text
    
    def chance_to_guarantee_transition(self, size: Bit):
        counted_value: float = self.p.value.value.value ** size.value
        message_by_pocket: MessageByPocket = MessageByPocket(value=counted_value)
        
        return message_by_pocket


class ROSTask4:
    
    def __init__(self, variant: int):
        self.variant: int = variant
        self.task_number: int = 4
        self.lightspeed: LightSpeed = LightSpeed()
        self.channel_lenght: ChannelLenght = ChannelLenght(var_number=self.variant)
        self.lightspeed_coefficient: LightspeedCoefficient = LightspeedCoefficient(var_number=self.variant)
        self.mtu: BasicPocketSize2 = BasicPocketSize2(var_number=self.variant)
        self.required_speed: RequiredLightSpeed = RequiredLightSpeed(var_number=self.variant)
        self.pocket_space: PocketSpace = PocketSpace(required_speed=self.required_speed.value.value)
        self.modulation_type: ModulationType = ModulationType(var_number=self.variant)
        self.signal_speed: SignalSpeed = SignalSpeed(modulation_type=self.modulation_type)
        self.distrib_signal_speed: KiloMetreBySecond = KiloMetreBySecond(
            value=((self.lightspeed.value.value.value * self.lightspeed_coefficient.value.value.value)/100.0))
        self.distrib_signal_time: Second = Second(value=(self.channel_lenght.value.value.value/self.distrib_signal_speed.value))
        self.bit_by_ip_pocket: Bit = self.mtu.value.value.to_bit()
        self.pocket_by_second: PocketBySecond = PocketBySecond(required_speed=self.required_speed, 
                                                               bit_by_ip_pocket=self.bit_by_ip_pocket)
        self.frequency_signal_time: Second = Second(value=(1.0/self.pocket_by_second.value))
        self.signal_generation_time: Second = Second(value=(
            self.frequency_signal_time.value-self.distrib_signal_time.value-self.pocket_space.value.value.value))
        self.signal_by_pocket: SignalByPocket = SignalByPocket(bit_by_ip_pocket=self.bit_by_ip_pocket, 
                                                               signal_speed=self.signal_speed)
        self.total_signal_count: SignalBySecond = SignalBySecond(pocket_by_second=self.pocket_by_second, 
                                                                 signal_by_pocket=self.signal_by_pocket)
        self.count_signal_speed: Bod = Bod(distribution_time=self.distrib_signal_time, 
                                           signal_by_second=self.total_signal_count, 
                                           pocket_space=self.pocket_space)
        self.count_signal_speed_mbod: MBod = Bod(value=self.count_signal_speed.value).to_mbod()
        
    def __str__(self):
        outer_text: str = f"""Параметры задачи №{self.task_number}:
        
        1. Вариант: {self.variant}
        2. {self.lightspeed.name}: {round(number=self.lightspeed.value.value.value, ndigits=4)} {self.lightspeed.value.value.name}
        3. {self.channel_lenght.name}: {round(number=self.channel_lenght.value.value.value, ndigits=4)} {self.channel_lenght.value.value.name}
        4. {self.lightspeed_coefficient.name}: {round(number=self.lightspeed_coefficient.value.value.value, ndigits=4)} {self.lightspeed.value.value.name}
        5. {self.mtu.name}: {round(number=self.mtu.value.value.value, ndigits=4)} {self.mtu.value.value.name}
        6. {self.required_speed.name}: {round(number=self.required_speed.value.value.value, ndigits=4)} {self.required_speed.value.value.name}
        7. {self.pocket_space.name}: {round(number=self.pocket_space.value.value.value, ndigits=4)} {self.pocket_space.value.value.name}
        8. {self.modulation_type.name}: {self.modulation_type.value}
        9. {self.signal_speed.name}: {round(number=self.signal_speed.value.value.value, ndigits=4)} {self.signal_speed.value.value.name}
        10. Скорость распространения сигнала: {round(number=self.distrib_signal_speed.value, ndigits=4)} {self.distrib_signal_speed.name}
        11. Время распространения сигнала: {round(number=self.distrib_signal_time.value, ndigits=4)} {self.distrib_signal_time.name}
        12. Биты в IP-пакете: {round(number=self.bit_by_ip_pocket.value, ndigits=4)} {self.bit_by_ip_pocket.name}
        13. Количество пакетов в секунду: {round(number=self.pocket_by_second.value, ndigits=4)} Пак/с
        14. Частота генерации сигналов: {round(number=self.frequency_signal_time.value, ndigits=6)} {self.frequency_signal_time.name}
        15. Время генерации сигналов: {round(number=self.signal_generation_time.value, ndigits=4)} {self.signal_generation_time.name}
        16. Соотношение сигналов на пакет: {round(number=self.signal_by_pocket.value, ndigits=4)} Сиг/Пакет 
        17. {self.total_signal_count.name}: {round(number=self.total_signal_count.value, ndigits=4)} Сиг/с
        18. {self.count_signal_speed.name}: {round(number=self.count_signal_speed.value, ndigits=4)} Бод
        19. {self.count_signal_speed_mbod.name}: {round(number=self.count_signal_speed_mbod.value, ndigits=4)} МБод
        """

        return outer_text