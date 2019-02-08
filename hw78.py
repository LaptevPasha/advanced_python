class YourMetaClass(type):
    def __init__(self, name, bases, d):
        accessors = {}
        pref = ["get_", "set_"]
        for k in d.keys():
            v = getattr(self, k)
            for i in range(2):
                if k.startswith(pref[i]):
                    accessors.setdefault(k[4:], [None, None])[i] = v
        for name, (getter, setter) in accessors.items():
            setattr(self, name, property(getter, setter, None, ""))


class Example(metaclass=YourMetaClass):
    def __init__(self):
        self._x = None

    def get_x(self):
        return self._x

    def set_x(self, value):
        self._x = value

    def get_y(self):
        return 'y'


ex = Example()
ex.x = 255
print(ex.x)
print(ex.y)
