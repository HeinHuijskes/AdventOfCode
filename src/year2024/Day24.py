import sys
sys.path.append('../../src')

from PythonFramework.Day import Day
import PythonFramework.Algorithms as algs


class Day24(Day):
    def parse(self, data):
        data = '\n'.join(data)
        initial, gates = data.split('\n\n')
        initial = [line.split(': ') for line in initial.split('\n')]
        initial = {gate: val=='1' for gate, val in initial}
        gates = [line.split(' -> ') for line in gates.split('\n')]
        gates = [(gate, operation.split(' ')) for operation, gate in gates]
        z_wires = [gate[0] for gate in gates if gate[0].startswith('z')]
        return initial, gates, z_wires
    
    def logic(self, wire1, gate, wire2, wires):
        wire1, wire2 = wires[wire1], wires[wire2]
        if gate == 'AND':
            return wire1 & wire2
        elif gate == 'XOR':
            return wire1 ^ wire2
        else: # OR gate
            return wire1 | wire2

    def solvePartOne(self, data):
        wires, gates, z_wires = data
        length = len(z_wires)
        while length > 0:
            # print(len(gates), length)
            unused_gates = []
            for out_wire, (wire1, gate, wire2) in gates:
                if wire1 in wires and wire2 in wires:
                    wires[out_wire] = self.logic(wire1, gate, wire2, wires)
                    if out_wire.startswith('z'):
                        length -= 1
                else:
                    unused_gates.append((out_wire, (wire1, gate, wire2)))
            gates = unused_gates

        result = 0
        for i, z_wire in enumerate(sorted(z_wires)):
            wire = wires[z_wire]
            result = result ^ (wire << i)

        return result

    def printGate(self, adder, wires):
        gatemap = {'XOR': '^', 'AND': '&', 'OR': '|', None: 'None'}
        def gate(wire):
            if wire == None:
                return ',  ### = ### # ###'
            wire1, gate, wire2 = wires[wire]
            return f',  {wire} = {wire1} {gatemap[gate]} {wire2}'
        string = f'{adder[0]}, {adder[1]}, {adder[2]}'
        for i in range(3, len(adder)):
            string += gate(adder[i])
        print(string)

    def printGates(self, full_adders, wires):
        for adder in full_adders:
            self.printGate(adder, wires)

    def addInput(self, wires, full_adders, add_index, fa_index, gate_type):
        for out_wire in wires:
            wire1, gate, wire2 = wires[out_wire]
            for adder in full_adders:
                index = int(adder['i'])
                abc = adder[add_index]
                if abc == None:
                    continue
                if (wire1 == abc or wire2 == abc) and gate == gate_type:
                    full_adders[index][fa_index] = out_wire
                    break

    def solvePartTwo(self, data):
        # 0   1    2    3                4                5                6                7
        # nr, x##, y##, z## = bbb ^ cin, aaa = x## & y##, bbb = x## ^ y##, ccc = bbb & cin, out = ccc | aaa
        swapped = []
        initial, gates, z_wires = data
        length = len(z_wires)
        full_adders = [{}]*len(z_wires)
        for i, out_wire in enumerate(initial[:length]):
            full_adders[i]['x'] = out_wire
            full_adders[i]['i'] = i
        for i, out_wire in enumerate(initial[length:]):
            full_adders[i+length]['y'] = out_wire
            full_adders[i+length]['i'] = i
        wires = {out_wire: (wire1, gate, wire2) for out_wire, (wire1, gate, wire2) in gates}

        # Add all x^y and z##=... inputs, based on x and y and z
        for out_wire in wires:
            wire1, gate, wire2 = wires[out_wire]
            index = int(out_wire[1:])
            if out_wire.startswith('z'):
                full_adders[index]['z'] = out_wire
            if (wire1.startswith('x') or wire1.startswith('y')) and gate == 'XOR':
                full_adders[index]['x^y'] = out_wire

        # Find incorrect zs and swap them back
        for adder in full_adders:
            z = adder['z']
            # Look at the z assignment, this should be "z## = x^y ^ cin"
            if z == None or 'x^y' not in adder['x^y'] or adder['i'] == 0 or adder['i'] == 45:
                continue
            bbb = adder['x^y']
            z_gate = wires[z]
            if z_gate[1] == 'XOR' and (z_gate[0] == bbb or z_gate[2] == bbb):
                continue
            for out_wire in wires:
                wire1, gate, wire2 = wires[out_wire]
                if (wire1 == bbb or wire2 == bbb) and gate == 'XOR':
                    wires[out_wire] = wires[z]
                    wires[z] = (wire1, gate, wire2)
                    swapped += [z, out_wire]
                    break

        # Add all x&y inputs, based on x and y
        for out_wire in wires:
            wire1, gate, wire2 = wires[out_wire]
            if (wire1.startswith('x') or wire1.startswith('y')) and gate == 'AND':
                index = int(wire1[1:])
                full_adders[index]['x&y'] = out_wire

        # Add ccc= x^y & cin inputs, based on finding x^y
        self.addInput(wires, full_adders, 'x^y', 'ccc', 'AND')
        # Add out= (x^y & cin) | x&y inputs, based on finding x&y
        self.addInput(wires, full_adders, 'x&y', 'out', 'AND')

        for adder in full_adders:
            ccc = adder['ccc']
            if ccc != None or adder['i'] == 0 or adder['i'] == 45:
                continue
            # ccc is None, so bbb is wrong. Find a new bbb where "z## = bbb ^ cin" and "ccc = bbb & cin"
            z, index = adder['z'], adder['i']
            wire1, gate, wire2 = wires[z]
            # c_out of previous adder is c_in for this adder
            c_in = full_adders[index-1][7]
            if wire1 == c_in:  # z## = bbb ^ cin
                bbb = wire2
            else:
                bbb = wire1 
            wrong_bbb = adder['bbb']
            swapped += [bbb, wrong_bbb]

        self.printGates(full_adders, wires)
        print(f'##, x##, y##,  z## = bbb ^ cin,  aaa = x## & y##,  bbb = x## ^ y##,  ccc = bbb & cin,  out = ccc | aaa')
        return ','.join(sorted(swapped)) 



Day24(24).getResult(testOnly=False)
