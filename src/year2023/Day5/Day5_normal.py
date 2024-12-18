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
    computed_ranges = []
    for r in ranges:
        computed_ranges.append([int(x) for x in r.split(' ') if x != ''])

    i = 0
    while i < len(sources):
        source = sources[i]
        length = sources[i+1]
        for destination, map_source, map_length in computed_ranges:

            # Check only sources that are within a maps range 
            if source + length - 1 > map_source and source < map_source + map_length - 1:
                # Optimized by adding whole ranges at the same time
                start = max(source, map_source)
                end = min(source + length-1, map_source + map_length-1)
                # Possible length is the room left within the map range
                possible_length = end - start
                leftover_length = start - source
                rightover_length = (source + length - 1) - end
                results.append(destination + (start - map_source))
                results.append(possible_length)
                if leftover_length > 0:
                    sources.append(source)
                    sources.append(leftover_length)
                if rightover_length > 0:
                    sources.append(end)
                    sources.append(rightover_length)
                # The ranges that do not fit this map have been appended to sources to be looked at later, 
                # so we can safely break and look at the next source
                length = 0
                break
        if length > 0:
            # There are no maps matching this source range
            results.append(source)
            results.append(length)
        i += 2
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
        results = []
        sources = seeds
        for m in maps:
            sources = getDestinations(sources, m)
        results = [x for i, x in enumerate(sources) if i%2==0]

        return min(results)


Day5().getResult(testOnly=False)
