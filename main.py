from importlib  import reload
import mymodule
reload(mymodule)
a=mymodule.addition()
a.add(12,24)
a=mymodule.subtraction()
a.sub(4,2)
a=mymodule.division()
a.div(4,2)