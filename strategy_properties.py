import copy



def filled_spot_count(matrix):
    sm = 0
    for row in matrix:
        for x in row:
            if x != 0:
                sm += 1
    return sm


def weighted_filled_spot_count(matrix):
    sm = 0
    for i, row in enumerate(matrix):
        for x in row:
            if x != 0:
                sm += len(matrix) - i
    return sm


def maximum_altitude(matrix):
    index = len(matrix)
    for i, row in enumerate(matrix):
        if sum(row) != 0:
            index = i
            break
    return len(matrix) - index


def hole_count(matrix):
    return len(find_holes(matrix))


def lines_cleared(matrix):
    sm = 0
    for row in matrix:
        check = True
        for x in row:
            if x == 0:
                check = False
        if check:
            sm += 1
    return sm


def altitude_delta(matrix):
    holes = []
    for i in range(len(matrix[0])):
        index = len(matrix)
        for j in range(len(matrix)):
            if matrix[j][i] != 0:
                index = len(matrix) - j
                break
        holes.append(index)
    return max(holes) - min(holes)


def get_pites(matrix):
    holes = []
    for i in range(len(matrix[0])):
        index = len(matrix)
        for j in range(len(matrix)):
            if matrix[j][i] != 0:
                index = len(matrix) - j
                break
        holes.append(index)
    ret = []
    ret.append(max(0, holes[1] - holes[0]))
    for i in range(1, len(matrix[0]) - 1):
        ret.append(max(0, min(holes[i + 1], holes[i - 1]) - holes[i]))
    ret.append(max(0, holes[-2] - holes[-1]))
    return ret


def deepest_pit(matrix):
    return max(get_pites(matrix))


def sum_of_pites(matrix):
    return sum(get_pites(matrix))


def horizontal_roughness(matrix):
    sm = 0
    for row in matrix:
        for i in range(len(row) - 1):
            if row[i] * row[i + 1] == 0 and row[i] + row[i + 1] != 0:
                sm += 1
    return sm


def vertical_roughness(matrix):
    sm = 0
    for j in range(len(matrix[0])):
        for i in range(len(matrix) - 1):
            if matrix[i][j] * matrix[i + 1][j] == 0 and matrix[i][j] + matrix[i + 1][j] != 0:
                sm += 1
    return sm


def get_params(matrix, prnt = True):
    if prnt:
        print("filled spot count : ", filled_spot_count(matrix))
        print("weighted filled spot count : ", weighted_filled_spot_count(matrix))
        print("maximum altitude ", maximum_altitude(matrix))
        print("hole count : ", hole_count(matrix))
        print("lines cleared : ", lines_cleared(matrix))
        print("altitude delta : ", altitude_delta(matrix))
        print("deepest pites : ", deepest_pit(matrix))
        print("sum of pites : ", sum_of_pites(matrix))
        print("horizontal roughness : ", horizontal_roughness(matrix))
        print("vertical roughness : ", vertical_roughness(matrix))


ATTRIBUTES = [filled_spot_count, weighted_filled_spot_count,
              maximum_altitude, hole_count, lines_cleared, altitude_delta,
              deepest_pit, sum_of_pites, horizontal_roughness, vertical_roughness]


def get_cost(w, matrix):
    return sum([f(matrix) * w[i] for i, f in enumerate(ATTRIBUTES)])


# def chose_placement(weights, shapes, matrix):
#     min_cost = sum(weights) * 10 ** 10
#     min_i = -1
#     min_shape = []
#     for shape in shapes:
#         for i in range(len(shape[0])):
#             undo = Logic.move_down(shape, [0,i], matrix)
#             if undo:
#                 cost = get_cost(weights, matrix)
#                 if cost < min_cost:
#                     min_cost = cost
#                     min_i = i
#                     min_shape = shape
#                 for do in undo:
#                     matrix[do[0]][do[1]] = do[2]
#     return min_cost, min_i, min_shape


def find_holes(matrix):
    ''' need to improve if shapes can pass obstecels'''
    m = len(matrix)
    n = len(matrix[0])
    matrix_c = copy.deepcopy(matrix)
    for i in range(n):
        if matrix_c[0][i] == 0:
            matrix_c[0][i] = -1
    for i in range(1, m):
        for j in range(0, n):
            if matrix[i][j] == 0 and (matrix_c[i - 1][j] == -1):
                matrix_c[i][j] = -1
    res = []
    for i in range(m):
        for j in range(n):
            if matrix_c[i][j] == 0:
                res.append([i, j])
    return res

#
# l = Logic()
# l.move_down([[0,1,0],[1,1,1]], [0,0])
# l.move_down([[0,1,0],[1,1,1]], [3,0])
# l.move_down([[1]],[6,0])
# l.move_down([[0,1,0],[1,1,1]],[0,0])
# l.move_down([[0,1,0],[1,1,1]],[3,0])
# l.move_down([[1]],[6,0])
#
# get_params(l.screen)
# for i in l.screen:
#     print(i)