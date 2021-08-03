class Korean:
    """Korean speaker"""
    def __init__(self):
        self.name = "Korean"
    
    def speak_korean(self):
        return "An-neyong?"

class British:
    """English speaker"""
    def __init__(self) -> None:
        self.name = "British"

    #Note the different method name here!
    def speak_english(self):
        return "Hello!"

class Adapter:
    """This changes the generic method name to individualized method names"""
    def __init__(self,object,**adapted_method):
        """Change the name of the method"""
        self._object = object
        self.__dict__.update(adapted_method)

    def __getattr__(self,attr):
        """Simply return the rest of attributes!"""
        return getattr(self._object, attr)

if __name__ == '__main__':
    objects = []
    korean = Korean()
    briish = British()
    objects.append(Adapter(korean, speak=korean.speak_korean))
    objects.append(Adapter(briish, speak=briish.speak_english))

    for obj in objects:
        print("{} says '{}'\n".format(obj.name,obj.speak()))