from src.PythonFramework.Day import Day


class Day22(Day):
    def parse(self, data):
        return [int(x) for x in data]
    
    def updateSecret(self, secret):
        secret = ((secret * 64) ^ secret) % 16777216
        secret = (int(secret / 32 ) ^ secret) % 16777216
        return ((secret * 2048) ^ secret) % 16777216

    def solvePartOne(self, data):
        result = 0
        for secret in data:
            for i in range(2000):
                secret = self.updateSecret(secret)
            result += secret
        return result

    def solvePartTwo(self, data):
        buyers = []
        for secret in data:
            differences = []
            price = secret % 10
            for i in range(2000):
                secret = self.updateSecret(secret)
                old_price, price = price, secret % 10
                differences.append((price, price-old_price))
            buyers.append(differences)

        buyer_sequences = []
        all_sequences = set()
        for buyer in buyers:
            sequence_map = {}
            for i in range(3, 2000):
                sequence = (buyer[i-3][1], buyer[i-2][1], buyer[i-1][1], buyer[i][1])
                if sequence not in sequence_map:
                    sequence_map[sequence] = buyer[i][0]
                    all_sequences.add(sequence)
            buyer_sequences.append(sequence_map)

        highest = [0, None]
        for sequence in all_sequences:
            result = 0
            for sequence_map in buyer_sequences:
                if sequence in sequence_map:
                    result += sequence_map[sequence]
            if result > highest[0]:
                highest = (result, sequence)
        return highest[0]
