##Create a method of instance "shoot_arrow()" that let -1 amount arrows
#that has a instance character

class Character:
    def __init__(self, amount_arrows):
        self.amount_arrows = amount_arrows

    def shoot_arrow(self):
        self.amount_arrows = self.amount_arrows-1