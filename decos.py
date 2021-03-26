def typer(t):
    def _typer(f):
        def inner(*args, **kwargs):
            r = f(*args, **kwargs)
	    print args
	    print kwargs
            return t(r)
        return inner
    return _typer

@typer(str)
def c():
    return 42

@typer(int)
def edad(valor):
    return valor * 2

print edad(16)
