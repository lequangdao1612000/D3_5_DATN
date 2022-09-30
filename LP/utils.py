def check(ls):
    if not ls:
        return ""
    lp_most_dict = {}
    lp_set = set(ls)
    for lp in lp_set:
        lp_most_dict[ls.count(lp)] = lp
    text = lp_most_dict[max(lp_most_dict.keys())]
    return text
