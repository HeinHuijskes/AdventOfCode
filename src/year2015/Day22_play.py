import sys
sys.path.append('../../src')

from random import choice
from Day22 import Spells, Entity, Player, Boss
from time import sleep


def output(string='', pause=0.2):
    print(string)
    sleep(pause)


class Game:
    player: Player
    boss: Boss
    playerTurn = True
    boss_names = ['Henry', 'Maximus The Destroyer', 'Big Papa', 'Lex Luthor']
    player_names = ['Hank', 'Marcus The Crusader', 'Zion', 'Low The Wyke II']

    def printStats(self, entity: Entity):
        output(f'{entity.name}: {entity.hp} hp, {entity.mana} mana, {entity.armor} armor')

    def triggerEffects(self):
        self.player.triggerEffects()
        self.boss.triggerEffects()

    def takePlayerTurn(self):
        self.printStats(self.player)
        self.printStats(self.boss)
        output(f'\nWhat action would you like to take?', pause=1)
        options = [spell for spell in Spells.list if spell not in self.player.effects and spell not in self.boss.effects]
        for option in options:
            output(f'- {option} ({Spells.cost[option]})')
        while True:
            spell = input('Spell: ')
            if spell not in Spells.list:
                output(f'Unknown spell')
            elif spell not in options:
                output('Spell not available yet')
            elif Spells.cost[spell] > self.player.mana:
                output(f'Not enough mana')
            else:
                output(f'Cast spell: {spell}')
                self.player.castSpell(spell, self.boss)
                break

    def playGame(self, hp, damage):
        self.boss = Boss(hp, damage, name=choice(self.boss_names))
        self.player = Player(name=choice(self.player_names))
        minimum_mana = min(Spells.cost.values())
        while self.player.hp > 0 and self.boss.hp > 0:
            self.triggerEffects()
            if not self.playerTurn:
                hp = self.player.hp
                self.boss.dealDamage(self.player)
                output(f'{self.boss.name} attacked {self.player.name} for {hp - self.player.hp} damage!')
            elif self.player.mana >= minimum_mana:
                self.takePlayerTurn()
            else:
                output('Not enough mana!')
            self.playerTurn = not self.playerTurn
            output(pause=1)
        if self.player.hp <= 0:
            output(f'Player lost!')
        else:
            output(f'Player won!')


Game().playGame(55, 8)
