class Borg:
    """Borg class making class attributes global"""
    _shared_state = {} #Attribute dictionary

    def __init__(self):
        self.__dict__ = self._shared_state

class Singleton(Borg):

    def __init__(self, **kwargs):
        Borg.__init__(self)
        self._shared_state.update(kwargs)
    
    def __str__(self):
        return str(self._shared_state)

if __name__ == '__main__':
    x = Singleton(HTTP = "Hyper Text Transfer Protocol")
    print(x)

    y = Singleton(SNMP = "Simple Network Management Protocol")
    print(y)