'''Без использования библиотек, создать класс для представления информации о времени. Ваш класс должен иметь
возможности установки времени и изменения его отдельных полей (час, минута,
секунда) с проверкой допустимости вводимых значений. В случае недопустимых
значений полей нужно установить максимально допустимое значение.
Создать методы изменения времени на заданное количество часов, минут и секунд.'''


class Time:
    def __init__(self, h=0, m=0, s=0):
        self.hours = h
        self.minutes = m
        self.seconds = s

    @property
    def hours(self):
        return self.hours
    @hours.setter
    def _set_hours(self, value):
        if 0 <= value <= 23:
            self._hours = value
        else:
            raise ValueError

    @property
    def minutes(self):
        return self.minutes
    @minutes.setter
    def _set_minutes(self, value):
        if 0 <= value <= 59:
            self._minutes = value
        else:
            raise ValueError

    @property
    def seconds(self):
        return self.seconds
    @second.setter
    def _set_seconds(self, value):
        if 0 <= value <= 59:
            self._seconds = value
        else:
            raise ValueError

            
    def offsethours(self, n_hours):
        act_hours = self._hours + n_hours
        self._hours = act_hours%24

    def offsetminutes(self, n_minutes):
        act_minutes = self._minutes + n_minutes
        self._minutes = act_minutes%60

    def offsetseconds(self, n_seconds):
        act_seconds = self._seconds + n_seconds
        self._seconds = act_seconds%60



    def __repr__(self):
        return f'<Time {self.hours}h {self.minutes}m {self.seconds}s>'

    def __str__(self):
        return f'{self.hours}:{self.minutes}:{self.seconds}'
