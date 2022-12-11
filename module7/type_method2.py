class Player:
    life = True

    @classmethod
    def to_revive(cls):
        cls.life = False

print(Player.life)