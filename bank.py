class Account():
    def __init__(self, name,pan, deposit):
        self.NAME=name
        self.pan_number=pan
        self.__amount=deposit   #public, (_)protected,(__) private
        self.username=self.NAME.replace(' ','')+'100'
        self.password=pan.upper()+'@123'

    def setAmount(self,amt):
        self.__amount=self.__amount+amt

    def getAmount(self):
        return self.__amount