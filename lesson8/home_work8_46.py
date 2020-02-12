import json


class Warehouse:

    _dict = {}
    _id = 0
    _dict_out = {}

    @classmethod
    def get_next_id(cls):
        cls._id += 1
        return cls._id

    @classmethod
    def put(cls, item):
        if item.id is None:
            item.id = cls.get_next_id()
        if item.__class__.__name__ not in cls._dict:
            cls._dict[item.__class__.__name__] = {}
        cls._dict[item.__class__.__name__][item.id] = item

    @classmethod
    def to_json(cls):
        return json.dumps({'_dict': cls._dict, '_dict_out': cls._dict_out}, indent=4, default=lambda x: x.__dict__)

    @classmethod
    def get(cls, eq_cls, department):
        try:
            item = cls._dict[eq_cls.__name__].popitem()[1]
            cls._dict_out[item.id] = item
            return item
        except:
            raise Exception('нет такого')

    @classmethod
    def ret(cls, id):
        try:
            cls.put(cls._dict_out[id])
            del cls._dict_out[id]
        except:
            raise Exception('нет такого')


class OfficeEquipment:
    def __init__(self, name):
        self.name = name
        self.id = None

    def my_copy(self):
        print('делаю копию')


class Printer(OfficeEquipment):
    def __init__(self, name):
        super().__init__(name)

    def my_print(self):
        print('печатаю с компа')


class Scanner(OfficeEquipment):
    def __init__(self, name):
        super().__init__(name)

    def my_scan(self):
        print('передаю в комп')


class Xerox(OfficeEquipment):
    def __init__(self, name):
        super().__init__(name)

    def my_xerit(self):
        print('делаю фотокопию')


while True:
    try:
        op = int(input('сдать технику-1, получить технику-2, поставить на учет-3, распечатать содержимое склада-4, выход -0: '))

        if op == 0:
            break
        elif op == 4:
            print(Warehouse.to_json())

        elif op == 1:
            Warehouse.ret(int(input('введите id: ')))
        else:
            tip = int(input('принтер-1, сканер-2, ксерокс-3:'))
            eq_cls = Printer if tip == 1 else Scanner if tip == 2 else Xerox

            if op == 2:
                t = Warehouse.get(eq_cls, input('введите отдел: '))
                print(' id оборудования: ', t.id)

            elif op == 3:
                Warehouse.put(eq_cls(input('введите название: ')))

            else:
                print('не верное значение')


    except Exception as err:
        print(err)
