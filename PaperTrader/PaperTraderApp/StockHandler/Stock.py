from PaperTraderApp.StockHandler.Observer import Observer
class Stock:
    def __init__(self, name, symbol, price):
        self.__name = name
        self.__symbol = symbol
        self.__price = price

        # Below is everthing for Observer
        self.observers = [] # List of observers attatched to this subject, right now will only be Stock

    def getName(self):
        return self.__name 

    def getSymbol(self):
        return self.__symbol

    def getPrice(self):
        return self.__price

    def _update(self, price):
        self.price = price

    def attach(self, observer):
        if not isinstance(observer, Observer):
            raise InvalidObserverException("Invalid observer type")
        observers.append(observer)
   
    def notifyObservers(self):
        for observer in observers:
            observer.update()

class InvalidObserverException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
