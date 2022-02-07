import functools
def smallestSufficientTeam(req_skills: list[str], people: list[list[str]]) -> list[int]:
    def unionBits(xs):
        return functools.reduce(lambda a, b: a | b, xs, 0)
    skills = { s: 1 << i for i, s in enumerate(req_skills)}
    skills_needed = (1 << len(req_skills)) - 1
    people_skills = [unionBits([skills[s] for s in p]) for p in people]
    
    dp = {0: []}
    for person in range(len(people)):
        for skillset, workers in list(dp.items()):
            new_skillset = skillset | people_skills[person]
            if new_skillset not in dp or len(workers) + 1 < len(dp[new_skillset]):
                dp[new_skillset] = workers + [person]
    
    return dp[skills_needed]