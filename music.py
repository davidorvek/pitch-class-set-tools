import json
import random as r
from collections import Counter

aggregate = [0,1,2,3,4,5,6,7,8,9,10,11]

# JSON object containing the Forte numbers, prime forms (using Rahn's alogrith), interval vectors, Z partners, and Forte prime form for every pitch-class set
with open('/users/davidorvek/documents/python/music/set_class.json','r') as sc_file:
    sc = json.load(sc_file)


# JSON object containing the sum-class system for every set class
with open('/users/davidorvek/documents/python/music/sum_class_system.json', 'r') as sum_class_file:
    sum_class = json.load(sum_class_file)


# JSON object that allows every consonant triad to be converted into a pitch-class set
with open('/users/davidorvek/documents/python/music/triads.json','r') as triads_file:
    triads = json.load(triads_file)


# Interval class consonance values as seen in David Huron,
# "Interval-Class Content in Equally-Tempered Pitch-Class Sets: Common Scales Exhibit Optimum Tonal Consonance."
# Music Perception, 11 no. 3 (1994): 289–305
IC1_value = -1.428
IC2_value = -0.582
IC3_value = +0.594
IC4_value = +0.386
IC5_value = +1.240
IC6_value = -0.453


# Transposition:
# transposes a given pitch-class set n semitones
def trans(pc_set, n):
    result = [(pc + n) % 12 for pc in pc_set]
    return result


# Inversion:
# inverts a given pitch-class set about pitch-class axis n
def inv(pc_set, n):
    result = [(n - pc) % 12 for pc in pc_set]
    return result


# Multiplicative transformation:
# returns a new set by multiplying each pitch class in the set by n mod 12
def mult(pc_set, n):
    result = [(pc * n) % 12 for pc in pc_set]
    return result


# Finds the inversional index that relates a set whose root is a given interval from a given root
def find_i(root, interval):
    index = (root + (root - (5 - distance))) % 12
    return index


# Interval vector
def iv(pc_set):
    sort = sorted(pc_set)
    backwards = sort[::-1]
    intervals = []
    vector = [0,0,0,0,0,0]

    while len(backwards) > 1:
        n = len(backwards)
        x = 1
        for _ in range(n - 1):
            intervals.append(backwards[0] - backwards[x])
            x += 1
        backwards.pop(0)

    for i in intervals:
        if i == 1 or i == 11:
            vector[0] += 1
        elif i == 2 or i == 10:
            vector[1] += 1
        elif i == 3 or i == 9:
            vector[2] += 1
        elif i == 4 or i == 8:
            vector[3] += 1
        elif i == 5 or i == 7:
            vector[4] += 1
        elif i == 6:
            vector[5] += 1
        else:
            print("ERROR: NON MOD 12 VALUE")
    return vector


# Convert a given list of intervals to interval classes
def int_class(intervals):
    result = []
    for interval in intervals:
        if interval == 1 or interval == 11:
            result.append(1)
        elif interval == 2 or interval == 10:
            result.append(2)
        elif interval == 3 or interval == 9:
            result.append(3)
        elif interval == 4 or interval == 8:
            result.append(4)
        elif interval == 5 or interval == 7:
            result.append(5)
        elif interval == 6:
            result.append(6)
        else:
            print('ERROR: NON MOD 12 VALUE')
    return result


# Characteristic function:
# returns a 12-point vector indicating which of the twelve pitch classes are present in the given set
def char_func(pc_set):
    result = [1 if i in pc_set else 0 for i in range(12)]
    return result


# Degrees of symmetry:
# returns a two-point vector indicating the number of axes under which the given set maps to itself under transposition and inversion respectively
def deg_sym(pc_set):
    T = 0
    I = 0

    for i in range(12):
        if sorted(trans(pc_set, i)) == sorted(pc_set):
            T += 1

        if sorted(inv(pc_set, i)) == sorted(pc_set):
            I += 1
    return [T, I]


# Checks to see if two given sets are related by transposition, inversion, multiplication, or share the NA interval vector
def find_rel(pc_set1, pc_set2):
    result = {}
    T = []
    I = []

    for i in range(12):
        if sorted(trans(pc_set1, i)) == sorted(pc_set2):
            T.append(i)

        if sorted(inv(pc_set1, i)) == sorted(pc_set2):
            I.append(i)
    result['T'] = T
    result['I'] = I

    if sorted(mult(pc_set1, 7)) == sorted(pc_set2):
        result['M'] = 'YES'
    else:
        result['M'] = 'NO'

    if iv(pc_set1) == iv(pc_set2) and T == [] and I == []:
        result['Z'] = 'YES'
    else:
        result['Z'] = 'NO'

    if sc[find_forte(pc_set1)]['complement'] == find_forte(pc_set2):
        result['C'] = 'YES'
    else:
        result['C'] = 'NO'

    return result


# Pitch-class sum:
# Returns the mod-twelve summed value of all of the pitch classes in a given pitch-class set
def pc_sum(pc_set):
    total = 0
    for pc in pc_set:
        total += pc
    return (total % 12)


# Directed Voice-Leading Sum:
# As seen in Richard Cohn,
# "Square Dances with Cubes"
# Journal of Music Theory 42 no. 2 (1998): 285
def DVLS(x, y):
    if len(x) > len(y):
        n = len(x) - len(y)
        for _ in range(n):
            y.append(0)
    elif len(y) > len(x):
        n = len(y) - len(x)
        for _ in range(n):
            x.append(0)

    total = 0
    for a, b in zip(x, y):
        total += ((b - a) % 12)
    return (total % 12)


# Transposition invariance vector:
# Returns a twelve-point vector indicating the number of pitch classes held invariant under each of the twelve transposition values
def t_invar(pc_set):
    result = []
    for i in range(12):
        invariant = 0
        t_set = trans(pc_set, i)
        for j in t_set:
            if j in pc_set:
                invariant += 1
        result.append(invariant)
    return result


# Inversion invariance vector:
# Returns a twelve-point vector indicating the number of pitch classes held invariant under each of the twelve inversional axes
def i_invar(pc_set):
    result = []
    for i in range(12):
        invariant = 0
        i_set = inv(pc_set, i)
        for j in i_set:
            if j in pc_set:
                invariant += 1
        result.append(invariant)
    return result


# Interval string:
# Returns the interval between each adjacent pitch class in an ordered pitch-class set
def cint(pc_set):
    result = []
    cycle = pc_set[1:]
    cycle.append(pc_set[0])
    for a, b in zip(cycle, pc_set):
        if (a - b) < 0:
            result.append((a - b) + 12)
        else:
            result.append(a - b)
    return result


# Returns the consonance value of a given set as seen in David Huron,
# "Interval-Class Content in Equally-Tempered Pitch-Class Sets: Common Scales Exhibit Optimum Tonal Consonance."
# Music Perception, 11 no. 3 (1994): 289–305
def harm_cons(pc_set):
  vector = iv(pc_set)
  total = round((IC1_value * vector[0]) \
              + (IC2_value * vector[1]) \
              + (IC3_value * vector[2]) \
              + (IC4_value * vector[3]) \
              + (IC5_value * vector[4]) \
              + (IC6_value * vector[5]), 3)
  return total


# Returns a dictionary of all intervals found between pitch classes n steps apart in a given ordered pitch-class set
def inventory(pc_set):
    backwards = pc_set[::-1]
    result = {}
    for b in range(len(pc_set)):
        name = '%s' % (b)
        result[name] = []
        for a in backwards:
            result[name].append((a - backwards[b]) % 12)
            b = (b + 1) % len(backwards)
    return result


# Generates a random pitch-class set of random size
def rand_set():
    aggregate = [0,1,2,3,4,5,6,7,8,9,10,11]
    random_set = []
    n = r.randint(2,10)
    for a in range(n):
        r.shuffle(aggregate)
        random_set.append(aggregate.pop())
    return random_set


# Finds the relationship between a given pitch-class set and that set's prime form
def rel2prime(pc_set):
    given = pc_set
    if sc[find_forte(pc_set)]['forte'] == 'NA':
        prime = sc[find_forte(pc_set)]['prime']
        rel = find_rel(given, prime)
        if rel['T'] == []:
            result = []
            for i in rel['I']:
                result.append('I%s' % (i))
            return result
        elif rel['I'] == []:
            result = []
            for i in rel['T']:
                result.append('T%s' % (i))
            return result
        else:
            result = []
            for i in rel['T']:
                result.append('T%s' % (i))
            for j in rel['I']:
                result.append('I%s' % (j))
            return result
    else:
        rahn_prime = sc[find_forte(pc_set)]['prime']
        rahn_rel = find_rel(given, rahn_prime)
        if rahn_rel['T'] == []:
            rahn_result = []
            for i in rahn_rel['I']:
                rahn_result.append('I%s' % (i))
        elif rahn_rel['I'] == []:
            rahn_result = []
            for i in rahn_rel['T']:
                rahn_result.append('T%s' % (i))
        else:
            rahn_result = []
            for i in rahn_rel['T']:
                rahn_result.append('T%s' % (i))
            for j in rahn_rel['I']:
                rahn_result.append('I%s' % (j))

        forte_prime = sc[find_forte(pc_set)]['forte']
        forte_rel = find_rel(given, forte_prime)
        if forte_rel['T'] == []:
            forte_result = []
            for i in forte_rel['I']:
                forte_result.append('I%s' % (i))
            return "Rahn = %s, Forte = %s" % (rahn_result, forte_result)
        elif forte_rel['I'] == []:
            forte_result = []
            for i in forte_rel['T']:
                forte_result.append('T%s' % (i))
            return "Rahn = %s, Forte = %s" % (rahn_result, forte_result)
        else:
            forte_result = []
            for i in forte_rel['T']:
                forte_result.append('T%s' % (i))
            for j in forte_rel['I']:
                forte_result.append('I%s' % (j))
            return "Rahn = %s, Forte = %s" % (rahn_result, forte_result)


# Generates the literal complement of a given pitch-class set
def complement(pc_set):
    result = [i for i in aggregate if i not in pc_set]
    return result


## The following three functions are used to find the normal order of a given pitch-class sets

# Returns n rotations of the sorted ordering of a given n-sized set
def rotations(pc_set):
    rotations = []
    sorted_set = sorted(pc_set)
    for index in range(len(sorted_set)):
        rotations.append(sorted_set[index:] + sorted_set[:index])
    return rotations


# Returns all of the intervals from the first pitch class in each rotation to every other pitch class in the set
def all_intervals(rotations):
    all_intervals = []
    for rotation in rotations:
        intervals = []
        moving_index = 1
        for _ in range(len(rotation) - 1):
            interval = rotation[len(rotation) - moving_index] - rotation[0]
            if interval < 0:
                intervals.append(interval + 12)
            else:
                intervals.append(interval)
            moving_index += 1
        all_intervals.append([rotation, intervals])
    return all_intervals


# Returns the most left-packed rotation of a given set as in Rahn's normal-order algorithm
def best(intervals):
    counter = 0
    while len(intervals) > 1:
        intervals_to_check = sorted([intervals[i][1][0] for i in range(len(intervals))])
        smallest = intervals_to_check[0]
        to_remove = []
        for j in range(len(intervals)):
            if intervals[j][1][0] != smallest:
                to_remove.append(intervals[j]) # Removes rotations that aren't candidates for normal order
        if to_remove != []:
            for k in to_remove:
                intervals.remove(k)
        if len(intervals[0][1]) > 1: # Ensures all intervals aren't deleted
            for l in range(len(intervals)):
                del intervals[l][1][0]
        counter += 1
        if counter > 10: # This creates an exit condition for highly-symmetrical sets
            sorted_sets = sorted([intervals[m][0] for m in range(len(intervals))])
            return sorted_sets[0] # Chooses the set with the smallest first pc
    return intervals[0][0] # Returns the only remaining set after all ineligable
                           # rotations have been deleted


# Combines the above functions into a single function
def normal_order(pc_set):
    return best(all_intervals(rotations(pc_set)))


# Prime-form finder:
# Returns the Forte number of a given pitch-class set
def find_forte(pc_set):
    n = len(pc_set)
    transpose = sorted(list(set(pc_set)))
    invert = inv(transpose, 0)[::-1]
    trans_array = []
    inv_array = []
    for i in range(n):
        trans_rotated = transpose[i:] + transpose[:i]
        x = 12 - trans_rotated[0]
        trans_array.append(trans(trans_rotated, x))
        inv_rotated = invert[i:] + invert[:i]
        y = 12 - inv_rotated[0]
        inv_array.append(trans(inv_rotated, y))
    for z in sc:
        prime = sc[z]['prime']
        if prime in trans_array:
            return z
            break
        elif prime in inv_array:
            return z
            break


# Converts a string of pitch classes or intervals that uses no spaces and A, B, and C for 10, 11, and 12 into an array
def string2array(input_string):
    result = [10 if i == 'T' else 11 if i == 'E' else 12 if i == 'W' else int(i) for i in input_string]
    return result


# Converts an array of pitch classes or intervals to a string that has no spaces and uses A, B, and C for 10, 11, and 12
def array2string(input_array):
    result = ''.join(['T' if i == 10 else 'E' if i == 11 else 'W' if i == 12 else str(i) for i in input_array])
    return result

# Adds angled brackets to the beginning and end of a string of intervals or pitch classes
def string2vector(input_string):
    result = '<' + input_string + '>'
    return result

# Generates a random twelve-tone row
def rand_row():
    row = aggregate
    r.shuffle(row)
    return row

# Generates a twelve-tone matrix for a given row as a dictionary
def row_matrix(row):
    i_row = inv(row, (row[0] + row[0]) % 12)
    matrix = {}
    for i in range(12):
        p_form = trans(row, i)
        r_form = p_form[::-1]
        i_form = trans(i_row, i)
        ri_form = i_form[::-1]
        matrix['P%s' % (i)] = p_form
        matrix['R%s' % (i)] = r_form
        matrix['I%s' % (i)] = i_form
        matrix['RI%s' % (i)] = ri_form
    return matrix


# Prints a twelve-tone row matrix
def print_matrix(row):
    print('\n')
    i_row = inv(row, (row[0] + row[0]) % 12)
    print('\t     I' + '  I'.join(['T' if pc == 10 else 'E' if pc == 11 else str(pc) for pc in row]))
    print('\t    -----------------------------------------------')
    for i in i_row:
        if i < row[0]:
            diff = (i + 12) - row[0]
        else:
            diff = i - row[0]
        p = trans(row, diff)
        p_string = '   '.join(['T' if pc == 10 else 'E' if pc == 11 else str(pc) for pc in p])
        print("\tP%s | %s | R%s" % (p_string[0], p_string, p_string[0]))
    print('\t    -----------------------------------------------')
    print('\t    RI' + ' RI'.join(['T' if pc == 10 else 'E' if pc == 11 else str(pc) for pc in row]))
    print('\n')


# Gets the number of unique row forms for the given row
def uniq_forms(row):
    matrix = row_matrix(row)
    uniq_forms = len(Counter(str(i) for i in matrix.values()).values())
    return uniq_forms


# Gets the indexes under which a given row is P, I, and RI combinatorial
def comb(hexachord):
    result = {'P': [], 'I': [], 'RI': []}
    for i in range(12):
        if sorted(trans(hexachord, i)) == sorted(complement(hexachord)):
            result['P'].append(i)
        elif sorted(inv(hexachord, i)) == sorted(complement(hexachord)):
            result['I'].append(i)
        elif sorted(inv(hexachord, i)) == sorted(hexachord):
            result['RI'].append(i)
    return result
