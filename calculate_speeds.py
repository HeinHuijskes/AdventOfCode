import os
from time import perf_counter_ns
from src.PythonFramework.Misc import getDate

def makeTable(results):
    seconds = ['μs', 'ms', 's']
    lines = [['|Year'] + [f'|{day}' for day in range(1, 26)] + ['|%']]
    lines.append([f'|---' for day in range(0, 27)])
    years = getDate()[2] - 2015 + 1
    for year in range(years):
        year = 2015 + year
        yearresults = {}
        if f'year{year}' in results:
            yearresults = results[f'year{year}']
        times = []
        for day in range(1, 26):
            if f'Day{day}' in yearresults:
                runtime = yearresults[f"Day{day}"]
                if runtime > 10**12: # >1000 s
                    result = f'|<span style="color:white">{round(yearresults[f"Day{day}"]/10**9, 1)} s</span>'
                elif runtime > 10**10: # >10 s
                    result = f'|<span style="color:red">{round(yearresults[f"Day{day}"]/10**9, 1)} s</span>'
                elif runtime > 10**8: # >=0.1s
                    result = f'|<span style="color:purple">{round(yearresults[f"Day{day}"]/10**9, 1)} s</span>'
                elif runtime > 10**5: # >0.1ms
                    result = f'|<span style="color:green">{round(yearresults[f"Day{day}"]/10**6, 1)} ms</span>'
                elif runtime > 10**2: # >0.1μs
                    result = f'|<span style="color:blue">{round(yearresults[f"Day{day}"]/10**3, 1)} μs</span>'
                else: # ns
                    result = f'|<span style="color:white">{round(yearresults[f"Day{day}"]/10**9, 1)} ns</span>'
            else:
                result = '|-'
            times.append(result)
        lines.append([f'|{year}'] + times + [f'|{round((len(yearresults))/25*100, 1)}'])
    with open('./speeds.md', 'w+') as file:
        file.write('### Years completed & times\n')
        file.write('In python, averaged over 10 runs on my laptop\n\n')
        file.write('\n'.join([''.join(line) for line in lines]))
        file.write(f'\n\nTotal completed: {round(sum([len(results[year]) for year in results])/(years*25)*100, 1)}%')
        file.close()


def calculateSpeeds(year='2024', specific_day='', iterations=1):
    results = {}
    dirs = [dir for dir in os.listdir('./src/') if dir.startswith('year'+year)]
    for dir in dirs:
        results[dir] = {}
        days = [day for day in os.listdir(f'./src/{dir}/') if day.startswith('Day'+specific_day) and day[3:].isnumeric()]
        for day in days:
            if not os.path.exists(f'./src/{dir}/{day}/{day}.py'):
                continue
            runtimes = []
            for i in range(iterations):
                start = perf_counter_ns()
                os.system(f'cd ./src/{dir}/{day} && python {day}.py >nul')
                end = perf_counter_ns()
                runtimes.append(end - start)
            runtime = sum(runtimes) // len(runtimes)
            results[dir][day] = runtime
            print(f'{dir[4:]} {day}: {round(runtime, 1)} ns')
    makeTable(results)


calculateSpeeds(year='2024', specific_day='')