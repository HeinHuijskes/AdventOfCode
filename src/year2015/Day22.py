import sys
sys.path.append('../../src')

from PythonFramework.Day import Day


class Spells:
    Magic_Missile, Drain, Shield, Poison, Recharge = 'Magic Missile', 'Drain', 'Shield', 'Poison', 'Recharge'
    cost = {Magic_Missile: 53, Drain: 73, Shield: 113, Poison: 173, Recharge: 229}
    list = [Magic_Missile, Drain, Shield, Poison, Recharge]


class Effect:
    def __init__(self, time, amount):
        self.time: int = time
        self.amount: int = amount


class Entity:
    def __init__(self, name="Entity", hp=0, armor=0, mana=0, damage=0):
        self.name: str = name
        self.hp: int = hp
        self.armor: int = armor
        self.mana: int = mana
        self.damage: int = damage
        self.effects: dict[str, Effect] = {}

    def triggerEffects(self):
        ended_effects = []
        for name, effect in self.effects.items():
            effect.time -= 1
            if name == Spells.Recharge:
                self.mana += effect.amount
            elif name == Spells.Poison:
                self.hp -= effect.amount
            if effect.time == 0:
                if name == Spells.Shield:
                    self.armor -= effect.amount
                ended_effects.append(name)
        for ended_effect in ended_effects:
            self.effects.pop(ended_effect)


class Player(Entity):
    def __init__(self, name="Player", hp=50, mana=500, armor=0):
        super().__init__(name, hp, armor, mana)

    def castSpell(self, spell, enemy: Entity):
        self.mana -= Spells.cost[spell]
        if spell == Spells.Magic_Missile:
            enemy.hp -= 4
        elif spell == Spells.Drain:
            self.hp += 2
            enemy.hp -= 2
        elif spell == Spells.Shield:
            self.armor = 7
            self.effects[Spells.Shield] = Effect(6, 7)
        elif spell == Spells.Poison:
            enemy.effects[Spells.Poison] = Effect(6, 3)
        elif spell == Spells.Recharge:
            self.effects[Spells.Recharge] = Effect(5, 101)


class Boss(Entity):
    def __init__(self, hp, damage, name="Boss"):
        super().__init__(name, hp, damage=damage)

    def dealDamage(self, target: Entity):
        target.hp -= max(1, self.damage - target.armor)


class Day22(Day):
    def parse(self, data):
        return int(data[0].split(': ')[1]), int(data[1].split(': ')[1])
    
    def copyEffects(self, entity: Entity, new_entity: Entity):
        new_entity.effects = {name: Effect(effect.time, effect.amount) for name, effect in entity.effects.items()}

    def createCopies(self, player: Player, boss: Boss):
        new_boss = Boss(hp=boss.hp, damage=boss.damage)
        self.copyEffects(boss, new_boss)
        new_player = Player(hp=player.hp, mana=player.mana, armor=player.armor)
        self.copyEffects(player, new_player)
        return new_player, new_boss

    def castNewSpells(self, player: Player, boss: Boss, mana_spent, lowest, queue: list):
        for spell in Spells.list:
            cost = Spells.cost[spell]
            if player.mana < cost or spell in player.effects or spell in boss.effects or cost + mana_spent > lowest:
                continue
            player_copy, boss_copy = self.createCopies(player, boss)
            player_copy.castSpell(spell, boss_copy)
            player_copy.triggerEffects()
            boss_copy.triggerEffects()
            boss_copy.dealDamage(player_copy)
            queue.append((player_copy, boss_copy, mana_spent+cost))

    def solve(self, hp, damage, hard_mode=False):
        lowest = 1000000
        queue = [(Player(), Boss(hp=hp, damage=damage), 0)]
        while len(queue) > 0:
            player, boss, mana_spent = queue.pop()
            if boss.hp <= 0:
                if mana_spent < lowest:
                    lowest = mana_spent
                continue
            if hard_mode:
                player.hp -= 1
                if player.hp <= 0:
                    continue
            player.triggerEffects()
            boss.triggerEffects()
            if player.hp <= 0:
                continue
            self.castNewSpells(player, boss, mana_spent, lowest, queue)
        return lowest

    def solvePartOne(self, data):
        hp, dmg = data
        return self.solve(hp, dmg)

    def solvePartTwo(self, data):
        hp, dmg = data
        return self.solve(hp, dmg, hard_mode=True)

if __name__ == '__main__':
    Day22(22).getResult(testOnly=False)
