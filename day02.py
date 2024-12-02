import fileinput

num_safe_reports = 0
num_safe_reports_problem_dampener = 0

def check_safe_report(report):
    prev_difference = report[1] - report[0]
    safe_report = True
    for i in range(1, len(report)):
        difference = report[i] - report[i-1]
        if abs(difference) < 1 or abs(difference) > 3: # not safe
            safe_report = False
            break
        if difference * prev_difference < 0: # quick way to check if sign has changed
            safe_report = False
            break
        prev_difference = difference

    return safe_report

for line in fileinput.input():
    report = [int(l) for l in line.strip().split()]
    if check_safe_report(report):
        num_safe_reports += 1
    else:
        for i in range(len(report)):
            if check_safe_report(report[:i] + report[i+1:]):
                num_safe_reports_problem_dampener += 1
                break

print("Number of safe reports:", num_safe_reports)
print("Number of safe reports - Problem Dampener activated:", num_safe_reports + num_safe_reports_problem_dampener)