import math
from copy import deepcopy


with open('input2.txt') as f:
	lines = f.readlines()


WORKFLOWS = {}
PARTS = []
for line in lines:
	if line[0] == "\n":
		pass
	elif line[0] == "{":
		p = {}
		for r in line.strip()[1:-1].split(","):
			r_key, r_value = r.split("=")
			p[r_key] = int(r_value)
		PARTS.append(p)
	else:
		workflow = []
		workflow_key, processes = line.strip()[:-1].split("{")

		for process in processes.split(","):
			if ":" in process:
				condition, success_target = process.split(":")
				condition_factor = condition[0]
				condition_symbol = condition[1]
				condition_value = int(condition[2:])
			else:
				condition_factor = "x"
				condition_symbol = ">"
				condition_value = 0
				success_target = process
			workflow.append({"factor": condition_factor, "symbol": condition_symbol, "value": condition_value, "target": success_target})
		WORKFLOWS[workflow_key] = workflow

accepted = []
pendings = [{
	"workflow": "in",
	"ratings": {
		"x": [0, 4001],
		"m": [0, 4001],
		"a": [0, 4001],
		"s": [0, 4001],
	}
}]
while pendings:
	pending = pendings.pop(0)
	if pending["workflow"] == "A":
		accepted.append(pending["ratings"])
		continue
	elif pending["workflow"] == "R":
		continue

	for process in WORKFLOWS[pending["workflow"]]:
		if any(bound[0] + 2 >= bound[1] for bound in pending["ratings"].values()):
			break

		other = deepcopy(pending)

		p_factor = process["factor"]
		p_symbol = process["symbol"]
		p_value = process["value"]
		if p_symbol == ">":
			other["ratings"][p_factor][0] = max(other["ratings"][p_factor][0], p_value)
			pending["ratings"][p_factor][1] = min(pending["ratings"][p_factor][1], p_value+1)
		elif p_symbol == "<":
			other["ratings"][p_factor][1] = min(other["ratings"][p_factor][1], p_value)
			pending["ratings"][p_factor][0] = max(pending["ratings"][p_factor][0], p_value-1)
		else:
			raise ValueError("unknown symbol")

		other["workflow"] = process["target"]
		pendings.append(other)

total_accepted = 0
for a in accepted:
	print(a)
	total_accepted += math.prod(upper - lower - 1 for lower, upper in a.values())

print(total_accepted)
