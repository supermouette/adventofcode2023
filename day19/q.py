with open("input.txt") as f:
    lines = [l.strip("\n") for l in f.readlines()]

rules = {"R": [], "A": []}

for i, l in enumerate(lines):
    if l == "":
        first_part = i + 1
        break
    name, raw_ruleset = l.split("{")
    ruleset = []
    for raw_rule in raw_ruleset[:-1].split(","):
        splited_rule = raw_rule.split(":")
        ruleset.append(splited_rule)
    rules[name] = ruleset

parts = []

for l in lines[first_part:]:
    parts.append(
        eval(
            l.replace("=", ":")
            .replace("x", '"x"')
            .replace("m", '"m"')
            .replace("a", '"a"')
            .replace("s", '"s"')
        )
    )

accepted = []

for p in parts:
    rule_name = "in"
    while rule_name not in ("R", "A"):
        for rule in rules[rule_name]:
            if len(rule) == 1:
                rule_name = rule[0]
                break
            else:
                func = lambda x, m, a, s: rule[1] if eval(rule[0]) else None
                if (output := func(**p)) is not None:
                    rule_name = output
                    break

    if rule_name == "A":
        accepted.append(p)

print(sum([sum(list(p.values())) for p in accepted]))
