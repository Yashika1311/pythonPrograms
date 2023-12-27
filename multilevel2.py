#Raheel Code ⬇️

class GrandFather:
    def _init_(self):
        self.name = " GrandFather"
        self._assets = 1500000

class Father(GrandFather):
    def _init_(self):
        super()._init_()
        self.name = self.name + " Father"
        self._inharitedAssets = self._assets 
        self._purchasedAssets = 200000
        self._totalAssets = self._inharitedAssets + self._purchasedAssets

class Child(Father):
    def _init_(self, name, assets):
        super()._init_()
        self.name = self.name + " " + name
        self.__inharitedAssets = self._totalAssets
        self.__purchasedAssets = assets
        self.totalAssets = self.inharitedAssets + self._purchasedAssets
    
    def displayData(self):
        print("Name: ", self.name)
        print("Assets: ", self._totalAssets)

obj = Child("Child",100000)
obj.displayData()