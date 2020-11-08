import requests
import random


class RandomNumbers:
    """ this class extracts [n] random numbers from [Random.org] """
    def __init__(self, n, xmin, xmax):
        self.n = n
        self.min = xmin
        self.max = xmax
        self.numbers = [ ]

        self.api_key = 'de0eefff-33d3-4f38-a690-6c8fa91db3b8' # Please go to {http://random.org} and obtain a valid
                                                                # api_key
        self.url = 'https://api.random.org/json-rpc/2/invoke'

    def __call__(self):
        json = {
            "jsonrpc": "2.0",
            "method": "generateIntegers",
            "params": {
                "apiKey": self.api_key,
                "n": self.n,
                "min": self.min,
                "max": self.max,
                "replacement": True,
            },
            "id": 23
        }
        res = requests.post(self.url, json=json)

        print(f"res.content: {res.content}")
        print(f"res.status_code: {res.status_code}")

        if res.status_code == 200:
            res_json = res.json()
            print(f"numbers:", res_json['result']['random']['data'])
            numbers = res_json['result']['random']['data']
            for number in numbers:
                yield number

    def convert(self, number):
        """ Convert an {integer} to a {floating point {number}} between 0.0 and 1.0"""
        if self.max > self.min and number <= self.max and number >= self.min:
            xrange = float(self.max - self.min)
            xnumber = (float(number) - float(self.min)) / xrange
            #print(f"xnumber: {xnumber}")
            return xnumber
        else:
            raise Exception(f"xmax < xmin")


def eye_random_number_provider():
    random = RandomNumbers(10, 1, 6)
    for index, number in enumerate(random()):
        print(f"[{index}] random -> {random.convert(number)}")
    print()

    for index, number in enumerate(random()):
        print(f"[{index}] random -> {random.convert(number)}")


#
#
#
class RandomNumberBag(tuple):
    def __new__(cls, n, *args, **kwargs):
        ret = super(RandomNumberBag, cls).__new__(cls, (0.0,) * n)

        return ret

    def __init__(self, n):
        self.n = n


class RandomSample:
    pass


def eye_random_number_bag():
    bag = RandomNumberBag(100)
    print(f"[bag/n] = {bag.n}")


if __name__ == "__main__":
    eyes = [
        eye_random_number_provider,
        eye_random_number_bag,
    ]
    ignored = [
        eye_random_number_bag,
    ]
    for eye in eyes:
        if eye not in ignored:
            eye()