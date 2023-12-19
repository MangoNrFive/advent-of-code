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

total_rating_accepted = 0
for part in PARTS:
	workflow = "in"
	while workflow not in ["A", "R"]:
		for process in WORKFLOWS[workflow]:
			rating = part[process["factor"]]
			if process["symbol"] == ">" and rating > process["value"] or process["symbol"] == "<" and rating < process["value"]:
				workflow = process["target"]
				break
	if workflow == "A":
		total_rating_accepted += sum(part.values())

print(total_rating_accepted)
