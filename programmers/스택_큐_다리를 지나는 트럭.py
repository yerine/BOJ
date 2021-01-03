
def solution(bridge_length, weight, truck_weights):
    answer = 0
    on_bridge = [0] * bridge_length
    
    while on_bridge:
        answer += 1
        on_bridge.pop(0)
        if truck_weights:
            if sum(on_bridge) + truck_weights[0] <= weight:
                on_bridge.append(truck_weights.pop(0))
            else:
                on_bridge.append(0)
                
    return answer

def solution(bridge_length, weight, truck_weights):
    answer = 0
    on_bridge = [0] * bridge_length
    curr_weight = 0
    
    while truck_weights:
        answer += 1
        curr_weight -= on_bridge.pop(0)
        
        if curr_weight + truck_weights[0] <= weight:
            truck_weight = truck_weights.pop(0)
            on_bridge.append(truck_weight)
            curr_weight += truck_weight
        else:
            on_bridge.append(0)
    
    answer += bridge_length

    return answer