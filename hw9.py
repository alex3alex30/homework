'''Создайте класс который будет хранить параметры для
подключения к физическому юниту (например сервер). В своем
списке атрибутов он должен иметь минимальный набор
(unit_name, mac_address, ip_address, login, password).
Вы должны описать каждый из этих атрибутов в виде гетеров и
сеттеров (@property). У вас должна быть возможность
получения и переопределения этих атрибутов в классе.'''


class ConnHandler:
    __slots__ = ['_unit_name', '_mac_address', '_ip_address', '_login', '_password']

    def __init__(self, unit_name='', mac_address='', ip_address='', login='', password=''):
        self.unitname = unit_name
        self.macaddress = mac_address
        self.ipaddress = ip_address
        self.login = login
        self.password = password

    @property
    def unitname(self):
        return self._unit_name #read
    @unitname.setter
    def _set_unitname(self, new_value):
        self._unit_name = new_value #write


    @property
    def macaddress(self):
        return self._mac_address #read
    @macaddress.setter
    def _set_macaddress(self, new_value):
        self._mac_address = new_value #write

    @property
    def ipaddress(self):
        return self._ip_address #read
    @ipaddress.setter
    def _set_ipaddress(self, new_value):
        self._ip_address = new_value #write


    @property
    def login(self):
        return self._login #read
    @login.setter
    def _set_login(self, new_value):
        self._login = new_value #write


    @property
    def password(self):
        return self._password #read
    @password.setter
    def _set_password(self, new_value):
        self._password = new_value #write
