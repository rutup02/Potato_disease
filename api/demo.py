def water_jug_dfs(jug1, jug2, target, path=[]):
    current_state = (jug1, jug2)

    if current_state == target:
        return path + [current_state]

    if current_state in path:
        return None

    # Try filling jug 1
    fill_jug1 = water_jug_dfs(capacity_jug1, jug2, target, path + [current_state, 'Fill Jug 1'])
    if fill_jug1:
        return fill_jug1

    # Try filling jug 2
    fill_jug2 = water_jug_dfs(jug1, capacity_jug2, target, path + [current_state, 'Fill Jug 2'])
    if fill_jug2:
        return fill_jug2

    # Try emptying jug 1
    empty_jug1 = water_jug_dfs(0, jug2, target, path + [current_state, 'Empty Jug 1'])
    if empty_jug1:
        return empty_jug1

    # Try emptying jug 2
    empty_jug2 = water_jug_dfs(jug1, 0, target, path + [current_state, 'Empty Jug 2'])
    if empty_jug2:
        return empty_jug2

    # Try pouring water from jug 1 to jug 2
    pour_jug1_to_jug2 = water_jug_dfs(max(0, jug1 - (capacity_jug2 - jug2)), min(capacity_jug2, jug2 + jug1), target,
                                       path + [current_state, 'Pour Jug 1 to Jug 2'])
    if pour_jug1_to_jug2:
        return pour_jug1_to_jug2

    # Try pouring water from jug 2 to jug 1
    pour_jug2_to_jug1 = water_jug_dfs(min(capacity_jug1, jug1 + jug2), max(0, jug2 - (capacity_jug1 - jug1)), target,
                                       path + [current_state, 'Pour Jug 2 to Jug 1'])
    if pour_jug2_to_jug1:
        return pour_jug2_to_jug1

    return None

# Example usage:
capacity_jug1 = 4
capacity_jug2 = 3
target_amount = 2

initial_state = (0, 0)
target_state = (target_amount, 0)

result = water_jug_dfs(*initial_state, target_state)

if result:
    print("Solution:")
    for step, action in enumerate(result[1:]):
        print(f"Step {step + 1}: {action}")
else:
    print("No solution found.")
