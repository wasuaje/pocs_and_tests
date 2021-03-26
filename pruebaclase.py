class myClass:
    def test(self):
        print "Hello"
    def test1(self):
        print "Hell world!" 


def main(ob):
        ip=raw_input("Enter 'test' or 'test1' : ")
        
        try:
            func=getattr(ob,ip)
        except AttributeError:
            print "No such function defined"
        try:
            func()
        except Exception as e:
            pass


ob=myClass()
main(ob)