matrix = [
    [0, 66, 47, 0, 101, 52, 47],   # London
    [66, 0, 0, 40, 0, 0, 0],    # Ipswich
    [47, 0, 0, 58, 88, 0, 0],   # Cambridge
    [0, 40, 58, 0, 0, 0, 0],     # Norwich
    [101, 0, 88, 0, 0, 0, 0],     # Birmingham
    [52, 0, 0, 0, 0, 0, 0],    # Oxford
    [47, 0, 0, 0, 0, 0, 0]      # Brighton
]


locations = ["London", "Ipswich", "Cambridge", "Norwich", "Birmingham", "Oxford", "Brighton"]

for i in range(7):
    neighbors = [locations[j] for j in range(7) if matrix[i][j] != 0]
    print(f"{locations[i]}: {', '.join(neighbors)}")
