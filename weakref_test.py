import weakref

interncache = weakref.WeakKeyDictionary()
class frozendict(dict):
    def __init__(self, initializer = None):
        super(frozendict, self).__init__()
        self.__hash = None
        if initializer is not None:
            for k,v in initializer.items():
                self[k] = v
    def __setitem__(self, k, v):
        if isinstance(v, dict):
            fv = frozendict(v)
            ifv = interncache.setdefault(fv,weakref.ref(fv))()
            super(frozendict, self).__setitem__(k, ifv if ifv is not None else fv)
        else:
            super(frozendict, self).__setitem__(k, v)
    def __hash__(self):
        if self.__hash is not None:
            return self.__hash
        else:
            self.__hash = hash(frozenset(self.items()))
            return self.__hash

fd = frozendict({1:{2:{'A': {'C' : 3}, 'B': 4}, 3:{'A': {'C' : 3}, 'B': 4}}})
print fd[1][2] is fd[1][3]
