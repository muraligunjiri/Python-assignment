roads = [('Mysore', 'Mandya', 66),
         ('Mysore', 'Chennapatna', 28),
         ('Mysore', 'Nanjangud', 60),
         ('Mysore', 'Bandipur', 34),
         ('Mysore', 'Nagarhole', 34),
         ('Mysore', 'Somnathpur', 3),
         ('Mysore', 'Bylakuppe', 108),
         ('Mandya', 'Chennapatna', 22),
         ('Mandya', 'Nanjangud', 12),
         ('Mandya', 'Bandipur', 91),
         ('Mandya', 'Nagarhole', 121),
         ('Mandya', 'Somnathpur', 111),
         ('Mandya', 'Bylakuppe', 71),
         ('Chennapatna', 'Nanjangud', 39),
         ('Chennapatna', 'Bandipur', 113),
         ('Chennapatna', 'Nagarhole', 130),
         ('Chennapatna', 'Somnathpur', 35),
         ('Chennapatna', 'Bylakuppe', 40),
         ('Nanjangud', 'Bandipur', 63),
         ('Nanjangud', 'Nagarhole', 21),
         ('Nanjangud', 'Somnathpur', 57),
         ('Nanjangud', 'Bylakuppe', 83),
         ('Bandipur', 'Nagarhole', 9),
         ('Bandipur', 'Somnathpur', 50),
         ('Bandipur', 'Bylakuppe', 60),
         ('Nagarhole', 'Somnathpur', 27),
         ('Nagarhole', 'Bylakuppe', 81),
         ('Somnathpur', 'Bylakuppe', 90)]

names = []
for i, j, distance in roads:
    names.append(i)
    names.append(j)

names = list(set(names))
print(names)
ways = dict()

for i, j, distances in roads:
    ways[i + ' to ' + j] = distances
    ways[j + ' to ' + i] = distances
print(ways)

# to make route
for index, i in enumerate(names):
    distance = 0
    route = []
    s = i + ' -> '
    for j in names:
        if i == j:
            continue
        distance += ways[i + ' to ' + j]
        s = s + j + ' -> '
    route.append((s, distance))

# To find shortestes path
    shortpath = None
    shortdistance = None
    if index == 0:
        shortpath = s
        shortdistance = distance
    if distance < shortdistance:
        shortdistance = distance
        shortpath = s

print(route)

print(shortpath, shortdistance)
