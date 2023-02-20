F, M, K = map(int, input().split())
maximum_teams = 0
possible_teams = []
for i in range(0, K+1):
    female = F - i
    male = M - (K-i)
    possible_teams.append(female//2)
    possible_teams.append(male)
    possible_team = min(possible_teams)
    possible_teams.clear()
    if possible_team > maximum_teams:
        maximum_teams = possible_team

print(maximum_teams)