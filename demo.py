def demo1(text):
    print text,"dit is een demo"

def som(par1, par2):
    print "som van", par1, "en", par2, "=", par1 + par2
    
def verschil(par1, par2):
    print "verschil van", par1, "en", par2, "=", par1 - par2

if __name__ == "__main__":
    print "Start"
    demo1('Hallo')
    som(33, 66)
    verschil(55, 44)
    