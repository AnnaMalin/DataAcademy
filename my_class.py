class djur:

    def __init__(self, antal_ben, läte):
        self.ben = antal_ben
        self.läte = läte

    def gör_ditt_läte(self):
        print('djuret låter: ' + self.läte)


hund = djur(4, 'woof')
anka = djur (2,'kvack')

hund.gör_ditt_läte()
print(hund.läte)
