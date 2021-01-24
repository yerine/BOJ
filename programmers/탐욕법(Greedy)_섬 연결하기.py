def solution(n, costs):
    answer = 0
    costs.sort(key = lambda x: x[2])
    routes = [costs[0][0]]
    while len(routes) != n:
        for i, cost in enumerate(costs):
            if (cost[0] in routes) and (cost[1] in routes):
                continue
            if cost[0] in routes:
                answer += cost[2]
                routes.append(cost[1])
                costs.pop(i)
                break
            elif cost[1] in routes:
                answer += cost[2]
                routes.append(cost[0])      
                costs.pop(i)
                break
    return answer