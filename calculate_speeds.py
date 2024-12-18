import os
from time import perf_counter_ns
from src.PythonFramework.Misc import getDate

def makeTable(results):
    
    lines = [['|Year'] + [f'|{day}' for day in range(1, 26)] + ['|%']]
    lines.append([f'|---' for day in range(0, 27)])
    years = getDate()[2] - 2015 + 1
    for year in range(years):
        year = 2015 + year
        yearresults = {}
        if f'year{year}' in results:
            yearresults = results[f'year{year}']
        result = [f'|{yearresults[f"Day{day}"]}' if f'Day{day}' in yearresults else '|-' for day in range(1, 26)]
        lines.append([f'|{year}'] + result + [f'|{round((len(yearresults))/25*100, 1)}'])
    with open('./speeds.md', 'w+') as file:
        file.write('### Years completed & times\n')
        file.write('In python, averaged over 10 runs on my laptop\n\n')
        file.write('\n'.join([''.join(line) for line in lines]))
        file.write(f'\n\nTotal completed: {round(sum([len(results[year]) for year in results])/(years*25)*100, 1)}%')
        file.close()


def calculateSpeeds(year='2024', specific_day=''):
    seconds = ['μs', 'ms', 's']
    results = {}
    dirs = [dir for dir in os.listdir('./src/') if dir.startswith('year'+year)]
    for dir in dirs:
        results[dir] = {}
        days = [day for day in os.listdir(f'./src/{dir}/') if day.startswith('Day'+specific_day) and day[3:].isnumeric()]
        for day in days:
            if not os.path.exists(f'./src/{dir}/{day}/{day}.py'):
                continue
            runtimes = []
            for i in range(1):
                start = perf_counter_ns()
                os.system(f'cd ./src/{dir}/{day} && python {day}.py >nul')
                end = perf_counter_ns()
                runtimes.append(end - start)
            runtime = sum(runtimes) // len(runtimes)
            for sec in seconds:
                if runtime // 100 < 1000:
                    break
                runtime //= 1000
            results[dir][day] = f'{round(runtime/1000, 1)} {sec}'
            print(f'{dir[4:]} {day}: {round(runtime/1000, 1)} {sec}')
    makeTable(results)


calculateSpeeds(year='', specific_day='')