import os
import json
from time import perf_counter_ns
from src.PythonFramework.Misc import getDate


star = '🌟'


def run():
    # calculate()
    format()


def calculate():
    # results = calculateAllSpeeds(1)
    results = {}
    for year in [2024]:
        results[year] = {}
        for day in [21, 22]:
            results[year][day] = calculateSpeedDay(day, year)
        # results[year] = calculateSpeedYear(year)
    storeAsJSON(results, overwrite=False)


def format():
    results = getJSONResults()

    totals = calculateCompletionTotals(results)
    completion = formatCompletionResults(results)
    completion_table = makeCompletionTable(completion, totals)

    totals = calculateTimeTotals(results)
    time = formatTimeResults(results)
    time_table = makeTimeTable(time, totals)
    
    with open('style.html', 'r') as file:
        styles = file.readlines()
        file.close()

    saveFormatted(styles, time_table, completion_table)
    return


def getJSONResults():
    with open('./stats/speeds.json', 'r') as file:
        return json.load(file)


def formatTime(result):
    s, m, e = '<span class="', '">`', '`</span>'
    # 1000s, 100s, 10s, 1s, 1ms, 1μs, 0ns
    scales = [10**12, 10**11, 10**10, 10**9, 10**6, 10**3, 1]
    colours = ['horrendous', 'bad', 'decent', 'good', 'perfect', 'insane', 'impossible']
    times = ['s', 'ms', 'μs', 'ns']
    for i, scale in enumerate(scales):
        if result >= scale:
            if i < 3:
                result = result * 10**(3-i)
            result = round(result / scale, 1)
            break
    return s + colours[i] + m + str(result) + times[max(3, i)-3] + e


def formatCompletion(result, tot=50):
    return f'{result}/{tot}'
    s, m, e = '<span class="', '">', '</span>'
    colours = ['bad', 'decent', 'good', 'quitegood', 'perfect']
    scales = [0, 10, 30, 49, 50]
    for i, scale in enumerate(scales):
        if result/tot*50 <= scale:
            break
    p = f' ({round(result/tot*100, 1)}%)'
    return s + colours[i] + m + str(result) + '/' + str(tot) + e  # + p


def calculateTimeTotals(results):
    years = {}
    days = {}
    for year in results:
        if year not in years:
            years[year] = 0
        for day in results[year]:
            if day not in days:
                days[day] = 0
            result = int(results[year][day])
            years[year] += result
            days[day] += result
    return years, days, sum(years.values())


def calculateCompletionTotals(results):
    years = {}
    days = {}
    for year in results:
        if year not in years:
            years[year] = 0
        for day in results[year]:
            if day not in days:
                days[day] = 0
            years[year] += 2
            days[day] += 2
    totalDays = (getDate()[2] - 2015 + 1)*25
    return years, days, (sum(days.values()), totalDays*2)


def formatTimeResults(results):
    formatted = {}
    for year in results:
        formatted_year = []
        for day in range(1, 26):
            if str(day) in results[year]:
                formatted_year.append(formatTime(results[year][str(day)]))
            else:
                formatted_year.append('-')
        formatted[year] = formatted_year
    return formatted


def formatCompletionResults(results):
    formatted = {}
    for year in results:
        formatted_year = []
        for day in range(1, 26):
            if str(day) in results[year]:
                formatted_year.append(f'{star}{star}')
            else:
                formatted_year.append('-')
        formatted[year] = formatted_year
    return formatted


def makeTimeTable(results, totals):
    lines = []
    line = [year for year in results]
    lines.append(f'|Day|{"|".join(line)}|Total|')

    line = [':-:' for i in range(len(results)+1)]
    lines.append(f'|-:|{"|".join(line)}|')

    years_totals, days_totals, total_total = totals
    line = [formatTime(years_totals[year]) for year in results]
    lines.append(f'|All|{"|".join(line)}|{formatTime(total_total)}|')

    for day in range(25):
        line = [results[year][day] for year in results]
        day_total = '-'
        if str(day+1) in days_totals:
            day_total = formatTime(days_totals[str(day+1)])
        lines.append(f'|{day+1}|{"|".join(line)}|{day_total}|')
    
    return lines


def makeCompletionTable(results, totals):
    lines = []
    line = [year for year in results]
    lines.append(f'|Day|{"|".join(line)}|Total|')

    line = [':-:' for i in range(len(results)+1)]
    lines.append(f'|-:|{"|".join(line)}|')

    years_totals, days_totals, (stars, total_stars) = totals
    line = [formatCompletion(years_totals[year]) for year in results]
    lines.append(f'|%|{"|".join(line)}|{formatCompletion(stars,total_stars)}|')

    for day in range(25):
        line = [results[year][day] for year in results]
        day_total = '-'
        if str(day+1) in days_totals:
            day_total = f'{days_totals[str(day+1)]}{star}'
        lines.append(f'|{day+1}|{"|".join(line)}|{day_total}|')
    
    return lines


def saveFormatted(styles, times, completion):
    with open('./stats/output.md', 'w+', encoding="utf-8") as file:
        file.write(''.join(styles))
        file.write(f'\n\n### Completion\n')
        file.write('\n'.join(completion))
        file.write(f'\n\n\n### Time\n')
        file.write('In python, ran on my laptop. I _want_ to say I took the average of 10 runs, but I probaly did not.\n\n')
        file.write('\n'.join(times))
        file.close()


def calculateSpeedDay(day, year=2024, iterations=1):
    runtimes = []
    for i in range(iterations):
        start = perf_counter_ns()
        os.system(f'cd ./src/year{year}/Day{day} && python Day{day}.py >nul')
        end = perf_counter_ns()
        runtimes.append(end - start)
    result = sum(runtimes) // len(runtimes)
    print(f'{year} day {day} [avg over {iterations} iterations]: {round(result/10**6, 3)} ms')
    return result


def calculateSpeedYear(year=2024, iterations=1):
    results = {}
    for day in range(1, 26):
        if not os.path.exists(f'./src/year{year}/Day{day}/Day{day}.py'):
            continue
        results[day] = calculateSpeedDay(day, year, iterations)
    return results


def calculateAllSpeeds(iterations=10):
    results = {}
    for year in range(2015, getDate()[2]+1):
        if not os.path.exists(f'./src/year{year}'):
            continue
        results[year] = calculateSpeedYear(year, iterations)
    return results


def storeAsJSON(data, overwrite=False):
    with open('./stats/speeds.json', 'r') as file:
        json_results = json.load(file)
        file.close()
    with open('./stats/speeds.json', 'w') as file:
        for year in data:
            if str(year) not in json_results:
                json_results[str(year)] = {}
            for day in data[year]:
                if overwrite or not str(day) in json_results[str(year)]:
                    json_results[str(year)][str(day)] = data[year][day]
        file.write(json.dumps(json_results))
        file.close()


run()
