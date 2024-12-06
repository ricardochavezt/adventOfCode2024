import fileinput

rules = {}
reverse_rules = {}

def is_correctly_ordered(l):
    for i in range(len(l)):
        list_left, list_right = l[:i], l[i+1:]
        # there should be no rules with l[i] on the left side and any of the items in list_left on the *right* side
        if (rule := rules.get(l[i])):
            if any([x in rule for x in list_left]):
                return False
        # there should be no rules with l[i] on the right side and any of the items in list_right on the *left* side
        if (reverse_rule := reverse_rules.get(l[i])):
            if any([x in reverse_rule for x in list_right]):
                return False
    return True

def sort_by_rules(l):
    if len(l) <= 1:
        return l
    # good ol' quicksort
    pivot = l[0]
    left, right = [], []
    rule = rules.get(pivot, [])
    for elem in l[1:]:
        if elem in rule:
            right.append(elem)
        else:
            left.append(elem)
    return sort_by_rules(left) + [pivot] + sort_by_rules(right)

rule_parsing = True
total = 0
total_corrected_updates = 0
for line in fileinput.input():
    if len(line.strip()) == 0:
        rule_parsing = False
        continue

    if rule_parsing:
        rule = [int(s) for s in line.strip().split("|")]
        rules.setdefault(rule[0], []).append(rule[1])
        reverse_rules.setdefault(rule[1], []).append(rule[0])
    else:
        update = [int(s) for s in line.strip().split(",")]
        if is_correctly_ordered(update):
            total += update[len(update) // 2]
        else:
            sorted_update = sort_by_rules(update)
            total_corrected_updates += sorted_update[len(sorted_update) // 2]

print("Total:", total)
print("Total - corrected updates:", total_corrected_updates)