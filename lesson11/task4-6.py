class StoreHouse:
    def __init__(self, length, width, height, num_of_cells):
        self.length = length
        self.width = width
        self.height = height
        self.num_of_cells = num_of_cells                            # количество ячеек для хранения
        self.store = {}                                             # парк имеющихся девайсов
        self.in_work = {}                                           # количество дейвайсов отданных в работу

    def receiving(self, device, count):                             # получаем технику на склад
        try:
            count == int(count)                                     # проверяем что число инт
        except:
            print(f'You send invalid count of device {device.name}. Please, try again') # если нет выводим сообщение
        else:
            if device.name not in self.store:
                self.store[device.name] = count
                self.num_of_cells -= count
            elif self.num_of_cells < count:
                print(f"We don't have free places for {count} devices. {self.num_of_cells} places is free")
            else:
                self.store[device.name] += count                    # количество девайса задаем
                self.num_of_cells -= count                          # количество ячеек уменьшаем



    def take_devices(self, device, company, count):                 # отдаем в работу девайсы
        try:
            count == int(count)
        except:
            print(f'You send invalid count of device {device.name}. Please, try again')
        else:
            if device.name not in self.store:                       # если такого имени не существует на складе
                print("We don't have this devices")
            elif self.store[device.name] < count:                   # если количество передаваемых девайсов меньше чем есть на складе
                print("We don't have so much devices")
            elif device.name not in self.in_work:                   # если такие девайсы еще не отданы в работу
                self.in_work[device.name] = {company: count}        # создаем словарь компания: число
                self.store[device.name] -= count                    # уменьшаем количество девайсов на складе
                self.num_of_cells += count                          # увеличиваем количество свободных мест на складе
            else:
                if company in self.in_work[device.name]:            # если компания уже брала такие девайсы, просто добавялем количество
                    self.in_work[device.name][company] += count
                else:
                    self.in_work[device.name][company] = count      # если у компании не было таких девайсов просто присваиваем скольок нужно
                self.store[device.name] -= count
                self.num_of_cells += count

class OrgDevice:
    def __init__(self, name, max_format):
        self.name = name
        self.max_format = max_format

class Printer(OrgDevice):
    def __init__(self, name, max_format, is_color):
        super().__init__(name, max_format)
        self.is_color = is_color

class Scanner(OrgDevice):
    def __init__(self, name, max_format, resolution):
        super().__init__(name, max_format)
        self.resolution = resolution

class Xerox(OrgDevice):
    def __init__(self, name, max_format, count_of_cycle):
        super().__init__(name, max_format)
        self.count_of_cycle = count_of_cycle

Moscow_store = StoreHouse(200, 500, 5, 1000)                            # проверка кода
HP_1010 = Printer('HP_1010', 'A4', True)
Canon_MX320 = Printer('Canon_MX320', 'A3', True)
print(Moscow_store.num_of_cells)
Moscow_store.receiving(HP_1010, 5)
Moscow_store.receiving(Canon_MX320, 15)
Oculus_10 = Scanner('Oculus_FX7', 'A2', '2048x3560')
Moscow_store.receiving(Oculus_10, 20)
Moscow_store.receiving(Oculus_10, 10)
Moscow_store.receiving(Oculus_10, 1000)
print(Moscow_store.store)
print(Moscow_store.num_of_cells)
print()
print('---------In progress-----------')
Moscow_store.take_devices(HP_1010, 'Yandex', 1)
Moscow_store.take_devices(HP_1010, 'VK', 2)
Moscow_store.take_devices(HP_1010, 'VK', 2)
Moscow_store.take_devices(Oculus_10, 'Papa Roach', 10)
Moscow_store.receiving(Canon_MX320, 'nine')
print(Moscow_store.in_work)
print(Moscow_store.store)
print(Moscow_store.num_of_cells)
