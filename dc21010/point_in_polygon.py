def point_in_polygon(boundaries, point):
    counter = 0
    n = len(boundaries)

    p1 = boundaries[0]
    for i in range(1, n+1):
        p2 = boundaries[i%n]
        if (point[1] > min(p1[1], p2[1])):
            if (point[1] <= max(p1[1], p2[1])):
                if (point[0] <= max(p1[0], p2[0])):
                    if (p1[1] != p2[1]):
                        xinters = (point[1]-p1[1])*(p2[0]-p1[0])/(p2[1]-p1[1])+p1[0]
                        if (p1[0] == p2[0] or point[0] <= xinters):
                            counter += 1
        p1 = p2
    return counter % 2 == 1

