from src.PythonFramework.Day import Day


class Day24(Day):
    def parse(self, data):
        data = '\n'.join(data)
        initial, gates = data.split('\n\n')
        initial = [line.split(': ') for line in initial.split('\n')]
        gates = [line.split(' -> ') for line in gates.split('\n')]
        gates = [(gate, operation.split(' ')) for operation, gate in gates]
        z_wires = [gate[0] for gate in gates if gate[0].startswith('z')]
        return initial, gates, z_wires

    def solvePartOne(self, data):
        wires, gates, z_wires = data
        logic = {'AND': (lambda x, y: x & y), 'XOR': (lambda x, y: x ^ y), 'OR': (lambda x, y: x | y)}
        wires = {gate: val=='1' for gate, val in wires}
        while len(gates) > 0:
            unused_gates = []
            for out_wire, (wire1, gate, wire2) in gates:
                if wire1 in wires and wire2 in wires:
                    wires[out_wire] = logic[gate](wires[wire1], wires[wire2])
                else:
                    unused_gates.append((out_wire, (wire1, gate, wire2)))
            gates = unused_gates
        return sum([wires[z] << i for i, z in enumerate(sorted(z_wires))])

    def findOutputWire(self, wires, wire1, wire2, gate):
        for output_wire in wires:
            w1, g, w2 = wires[output_wire]
            if g == gate and ((w1 == wire1 and w2 == wire2) or (w2 == wire1 and w1 == wire2)):
                return output_wire
            if wire2 == None and g == gate and (w1 == wire1 or w2 == wire1):
                return output_wire
            
    def swap(self, wires, wire1, wire2, swapped, wrong):
        swapped += [wire1, wire2]
        w1, g, w2 = wires[wire1]
        wires[wire1] = wires[wire2]
        wires[wire2] = (w1, g, w2)

    def checkWires(self, wires, bbb, out, swapped, x, y, z):
        wire1, gate, wire2 = wires[z]
        if ((bbb != wire1 and bbb != wire2) or gate != 'XOR') and out != None:  # Something is wrong, z, bbb or cin is incorrect
            if (out != wire1 and out != wire2) or gate != 'XOR':  # cin or the gate does not match either: z must be assigned wrong
                actual_z = self.findOutputWire(wires, bbb, out, 'XOR')
                self.swap(wires, actual_z, z, swapped, 'z')
                return bbb 
            else:  # bbb is wrong, swap with the right wire
                if out == wire1:
                    correct = wire2
                else:
                    correct = wire1
                self.swap(wires, correct, bbb, swapped, 'x^y')
                return correct
        return bbb

    def solvePartTwo(self, data):
        swapped = []
        initial, gates, z_wires = data
        initial = [x[0] for x in initial]
        wires = {out_wire: (wire1, gate, wire2) for out_wire, (wire1, gate, wire2) in gates}
        out = None
        for x in initial[:len(initial)//2]:
            index = x[1:]
            z, y = f'z{index}', f'y{index}'
            bbb = self.findOutputWire(wires, x, y, 'XOR')
            bbb = self.checkWires(wires, bbb, out, swapped, x, y, z)
            aaa = self.findOutputWire(wires, x, y, 'AND')
            ccc = self.findOutputWire(wires, bbb, out, 'AND')
            out = self.findOutputWire(wires, ccc, aaa, 'OR')
        return ','.join(sorted(swapped)) 
