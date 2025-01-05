import sys
sys.path.append('../../src')

from PythonFramework.Day import Day
import PythonFramework.Algorithms as algs

import math


class Day21(Day):
    weapons = [['Dagger', 8, 4, 0], ['Shortsword', 10, 5, 0], ['Warhammer', 25, 6, 0], ['Longsword', 40, 7, 0], ['Greataxe', 74, 8, 0]]
    armors = [['Leather', 13, 0, 1],['Chainmail', 31, 0, 2],['Splintmail', 53, 0, 3],['Bandedmail', 75, 0, 4],['Platemail', 102, 0, 5]]
    rings = [['Damage +1', 25, 1, 0],['Damage +2', 50, 2, 0],['Damage +3', 100, 3, 0],['Defense +1', 20, 0, 1],['Defense +2', 40, 0, 2],['Defense +3', 80, 0, 3]]

    def parse(self, data):
        hitpoints = int(data[0].split('Hit Points: ')[1])
        damage = int(data[1].split('Damage: ')[1])
        armor = int(data[2].split('Armor: ')[1])
        return hitpoints, damage, armor
    
    def simulate(self, hp, dmg, arm, bhp, bdmg, barm):
        boss_damage = max(1, bdmg-arm)
        player_damage = max(1, dmg-barm)
        boss_turns = math.ceil(hp / boss_damage)
        player_turns = math.ceil(bhp / player_damage)
        return player_turns <= boss_turns
    
    def getAllOptions(self):
        queue = []
        for weapon in self.weapons:
            queue.append([weapon])
        new_equipment = []
        for armor in self.armors:
            for item in queue:
                new_equipment.append(item+[armor])
        queue += new_equipment
        new_equipment = []
        for item in queue:
            for i, ring in enumerate(list(self.rings)):
                new_equipment.append(item+[ring])
                for j, ring2 in enumerate(list(self.rings)[i+1:]):
                    if ring != ring2:
                        new_equipment.append(item+[ring, ring2])
        queue += new_equipment
        return queue
    
    def donEquipment(self, equipment):
        return [sum([item[i] for item in equipment]) for i in [1, 2, 3]]
    
    def solve(self, data, condition):
        boss_hp, boss_dmg, boss_arm = data
        player_hp = 100
        queue = self.getAllOptions()
        previous_cost = None
        for equipment in queue:
            cost, damage, armor = self.donEquipment(equipment)
            player_wins = self.simulate(player_hp, damage, armor, boss_hp, boss_dmg, boss_arm)
            if condition(player_wins, previous_cost, cost):
                previous_cost = cost
        return previous_cost

    def solvePartOne(self, data):
        condition = (lambda win, previous, cost: win and (previous == None or previous > cost))
        return self.solve(data, condition)

    def solvePartTwo(self, data):
        condition = (lambda win, previous, cost: not win and (previous == None or previous < cost))
        return self.solve(data, condition)


Day21(21).getResult(testOnly=False)
