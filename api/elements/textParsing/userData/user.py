__version__ = '0.0.1a'

class User:
    id = None
    activeModule = None
    previus_module = None
    allowTeachers = []

    def __init__(self, userId):
        self.id = userId
        self.isInGame = False

    def set_previus_module(self, module_name):
        self.previus_module = module_name

    def activateModule(self, moduleName):
        self.activeModule = moduleName

    def exitFromModule(self):
        self.activeModule = None
