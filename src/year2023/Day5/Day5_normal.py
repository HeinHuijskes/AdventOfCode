import sys
sys.path.append('../../../src')

from PythonFramework.Day import Day


def getDestination(source, ranges):
    result = source
    for r in ranges:
        dest, src, l = (int(x) for x in r.split(' ') if x != '')
        if source >= src and source < src + l:
            result = dest + source - src
    return result


def getDestinations(sources, ranges):
    results = []
    # print(f'results: {results}')
    computed_ranges = []
    for r in ranges:
        computed_ranges.append((int(x) for x in r.split(' ') if x != ''))

    for i in range(0, len(sources), 2):
        source = sources[i]
        length = sources[i+1]
        for dest, src, l in computed_ranges:
            if source >= src and source < src + l:
                # Optimize by adding whole ranges at the same time
                # Possible length is the room left within the map range
                possible_length = src + l - source


                results[i] = dest + s - src
            else:
                # Add in a smart way a longer array that is outside of the maps range
                results.append(s)
    # print(f'new results: {results}')
    return results


class Day5(Day):
    def solvePartOne(self, data):
        seeds = [int(x) for x in data[0].split(': ')[1].split(' ')]
        lines = '\n'.join(data[2:])
        maps = [l.split('map:')[1].split('\n')[1:] for l in lines.split('\n\n')]
        results = []
        for s in seeds:
            source = s
            for m in maps:
                source = getDestination(source, m)
            results.append(source)
        
        return min(results)

    def solvePartTwo(self, data):
        seeds = [int(x) for x in data[0].split(': ')[1].split(' ')]
        lines = '\n'.join(data[2:])
        maps = [l.split('map:')[1].split('\n')[1:] for l in lines.split('\n\n')]
        # print(maps)
        results = []
        # for i in range(0, len(seeds), 2):
        #     seed = seeds[i]
        #     length = seeds[i+1]
        #     sources = [x for x in range(seed, seed+length)]
        sources = seeds
        for m in maps:
            print(m[0])
            sources = getDestinations(sources, m)
        results = sources
        # print(results)

        return min(results)


Day5().getResult(testOnly=False)
