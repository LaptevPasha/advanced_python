import json
import urllib.request


class Money(object):
    def converter(self, new_currency):
        if not self.json_string:
            with urllib.request.urlopen(self.url) as response:
                self.json_string = response.read()
                self.parsed_json = json.loads(self.json_string)
        y = (self.parsed_json['quotes']['USD' + self.currency])
        x = (self.parsed_json['quotes']['USD' + new_currency])
        self.value = x / y * self.value
        self.currency = new_currency

    def __init__(self, value, currency="USD"):
        self.value = value
        self.currency = currency
        self.url = ("http://apilayer.net/api/live?access_key="
                    "86a06d07fe74a7b67016bf603803a605")
        self.json_string = None
        self.parsed_json = None

    def __str__(self):
        return str(self.value) + ' ' + self.currency

    def __add__(self, other):
        if isinstance(other, Money):
            other.converter(self.currency)
            return Money(self.value + other.value, self.currency)
        else:
            return Money(self.value + other, self.currency)

    def __mul__(self, other):
        return Money(self.value * other, self.currency)

    __rmul__ = __mul__
    __radd__ = __add__


x = Money(10, "BYN")
y = Money(11)
z = Money(12.34, "EUR")
print(z + 3.11 * x + y * 0.8)

lst = [Money(10, "BYN"), Money(11), Money(12.01, "JPY")]
s = sum(lst)
print(s)
