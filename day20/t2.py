from copy import deepcopy
from functools import reduce
from math import lcm

with open("input.txt") as f:
    lines = [l.strip("\n") for l in f.readlines()]

machines = {}
conjunction_modules = []
for l in lines:
    name, connector = l.split(" -> ")
    connector = connector.split(", ")
    if name == "broadcaster":
        machines[name] = {"c": connector, "type": "b"}
    elif name[0] == "%":
        machines[name[1:]] = {"c": connector, "type": "%", "status": "off"}
    elif name[0] == "&":
        machines[name[1:]] = {"c": connector, "type": "&", "status": {}}
        conjunction_modules.append(name[1:])

for name, state in machines.items():
    for output in state["c"]:
        if output in conjunction_modules:
            machines[output]["status"][name] = "low"

machines["rx"] = {"c": [], "type": "???", "status": None}
print(machines["cl"])

cl_min_button_press = {key: 0 for key in machines["cl"]["status"].keys()}
print(cl_min_button_press)

original_state = deepcopy(machines)

count_pulse = {"low": 0, "high": 0}
for button_push in range(1000000000):
    next_state = [["btn", "broadcaster", "low"]]
    stage_i = 0
    while len(next_state) != 0:
        stage_i += 1
        state = next_state
        next_state = []
        for pulse_from, name, pulse in state:
            count_pulse[pulse] += 1
            current_machine = machines[name]
            if current_machine["type"] == "b":
                next_state += [[name, c, pulse] for c in current_machine["c"]]
            elif current_machine["type"] == "%":
                if pulse == "low":
                    if current_machine["status"] == "off":
                        current_machine["status"] = "on"
                        next_state += [[name, c, "high"] for c in current_machine["c"]]
                    else:
                        current_machine["status"] = "off"
                        next_state += [[name, c, "low"] for c in current_machine["c"]]
            elif current_machine["type"] == "&":
                current_machine["status"][pulse_from] = pulse
                if "low" not in list(current_machine["status"].values()):
                    next_state += [[name, c, "low"] for c in current_machine["c"]]
                else:
                    next_state += [[name, c, "high"] for c in current_machine["c"]]
            if name == "cl" and "high" in current_machine["status"].values():
                for status in current_machine["status"]:
                    if (
                        current_machine["status"][status] == "high"
                        and cl_min_button_press[status] == 0
                    ):
                        cl_min_button_press[status] = button_push + 1
                        print(button_push + 1, current_machine["status"])

                if 0 not in cl_min_button_press.values():
                    print(cl_min_button_press)
                    print(lcm(*cl_min_button_press.values()))
                    exit()
