def get_res(branch, subs):
	total=0
	for k,v in subs.items():
		if branch == "CSE" and k in ["C","java"]:
			total+=v
	return total

sub={"C":20, "java":20, "math":10}
total=get_res("CSE", sub)
