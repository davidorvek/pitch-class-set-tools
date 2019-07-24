import json

# JSON object containing the Forte numbers, prime forms (using Rahn's alogrith), interval vectors, Z partners, and Forte prime form for every pitch-class set
with open('/users/davidorvek/documents/python/music/pcs.json','r') as pcs_file:
    pcs = json.load(pcs_file)

# JSON object containing the sum-class system for every set class
with open('/users/davidorvek/documents/python/music/sum_class_system.json', 'r') as sum_class_file:
    sum_classes = json.load(sum_class_file)

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
    trans_result = []
    for pc in pc_set:
        new_pc = pc + n
        if new_pc >= 12:
            trans_result.append(new_pc % 12)
        else:
            trans_result.append(new_pc)
    return trans_result

# Inversion:
# inverts a given pitch-class set about pitch-class axis n
def inv(pc_set, n):
    inv_result = []
    for pc in pc_set:
        new_pc = n - pc
        if new_pc < 0:
            inv_result.append(new_pc + 12)
        else:
            inv_result.append(new_pc)
    return inv_result

# Multiplicative transformation:
# returns a new set by multiplying each pitch class in the set by n mod 12
def mult(pc_set, n):
	result = []
	for i in pc_set:
		result.append((i * n) % 12)
	return result

# Finds the inversional index that relates a set whose root is a given interval from a given root
def find_i(root, interval):
	index = (root + (root - (5 - distance))) % 12
	return index

# Interval vector
def int_vect(pc_set):
    sort = sorted(pc_set)
    backwards = sort[::-1]
    iv_result = []
    IC1 = 0
    IC2 = 0
    IC3 = 0
    IC4 = 0
    IC5 = 0
    IC6 = 0

    while len(backwards) > 1:
        n = len(backwards)
        x = 1
        for _ in range(n - 1):
            iv_result.append(backwards[0] - backwards[x])
            x += 1
        backwards.pop(0)

    for i in iv_result:
        if i == 1 or i == 11:
            IC1 += 1
        elif i == 2 or i == 10:
            IC2 += 1
        elif i == 3 or i == 9:
            IC3 += 1
        elif i == 4 or i == 8:
            IC4 += 1
        elif i == 5 or i == 7:
            IC5 += 1
        elif i == 6:
            IC6 += 1
        else:
            pass
    return "<%s%s%s%s%s%s>" % (IC1, IC2, IC3, IC4, IC5, IC6)

# Characteristic function:
# returns a 12-point vector indicating which of the twelve pitch classes are present in the given set
def char_func(pc_set):
    result = []
    for i in range(12):
        if i in pc_set:
            result.append(1)
        else:
            result.append(0)
    return result

# Degrees of symmetry:
# returns a two-point vector indicating the number of axes under which the given set maps to itself under transposition and inversion respectively
def deg_sym(pc_set):
    T = 0
    I = 0
    for i in range(12):
        if sorted(trans(pc_set, i)) == sorted(pc_set):
            T += 1
        else:
            T += 0
        if sorted(inv(pc_set, i)) == sorted(pc_set):
            I += 1
        else:
            I += 0
    return T, I

# Checks to see if two given sets are related by transposition, inversion, multiplication, or share the same interval vector
def find_rel(pc_set1, pc_set2):
    T = []
    I = []
    M = []
    Z = []

    for i in range(12):
        if sorted(trans(pc_set1, i)) == sorted(pc_set2):
            T.append(i)
        else:
            pass
        if sorted(inv(pc_set1, i)) == sorted(pc_set2):
            I.append(i)
        else:
            pass
        if sorted(mult(pc_set1, i)) == sorted(pc_set2):
            M.append(i)
        else:
            pass

    if int_vect(pc_set1) == int_vect(pc_set2) and T == [] and I == []:
        Z.append('YES')
    else:
        Z.append('NO')

    results = {'T': T, 'I': I, 'M': M, 'Z': Z}
    return results

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
        else:
                pass
        total = 0
        for a, b in zip(x, y):
                total += ((b - a) % 12)
        return (total % 12)

# Transposition invariance vector:
# Returns a twelve-point vector indicating the number of pitch classes held invariant under each of the twelve transposition values
def t_vect(pc_set):
    results = []
    for i in range(12):
        invariant = 0
        t_set = trans(pc_set, i)
        for j in t_set:
            if j in pc_set:
                invariant += 1
            else:
                pass
        results.append(invariant)
    return results

# Inversion invariance vector:
# Returns a twelve-point vector indicating the number of pitch classes held invariant under each of the twelve inversional axes
def i_vect(pc_set):
    results = []
    for i in range(12):
        invariant = 0
        i_set = inv(pc_set, i)
        for j in i_set:
            if j in pc_set:
                invariant += 1
            else:
                pass
        results.append(invariant)
    return results

# Interval string:
# Returns the interval between each adjacent pitch class in an ordered pitch-class set
def int_string(pc_set):
    result = []
    cycle = pc_set[1:]
    cycle.append(pc_set[0])
    for a, b in zip(cycle, pc_set):
        if (a - b) < 0:
            result.append(a - b + 12)
        else:
            result.append(a - b)
    return result

# Returns the consonance value of a given set as seen in David Huron,
# "Interval-Class Content in Equally-Tempered Pitch-Class Sets: Common Scales Exhibit Optimum Tonal Consonance."
# Music Perception, 11 no. 3 (1994): 289–305
def harm_cons(pc_set):
  sort = sorted(pc_set)
  backwards = sort[::-1]
  result = []
  vector_array = []
  IC1 = 0
  IC2 = 0
  IC3 = 0
  IC4 = 0
  IC5 = 0
  IC6 = 0
  while len(backwards) > 1:
    n = len(backwards)
    x = 1
    for _ in range(n - 1):
      result.append(backwards[0] - backwards[x])
      x += 1
    backwards.pop(0)
  for i in result:
    if i == 1 or i == 11:
      IC1 += 1
    elif i == 2 or i == 10:
      IC2 += 1
    elif i == 3  or i == 9:
      IC3 += 1
    elif i == 4 or i == 8:
      IC4 += 1
    elif i == 5 or i == 7:
      IC5 += 1
    elif i == 6:
      IC6 += 1
    else:
      pass
  vector_array.append(IC1)
  vector_array.append(IC2)
  vector_array.append(IC3)
  vector_array.append(IC4)
  vector_array.append(IC5)
  vector_array.append(IC6)
  total = round((IC1_value * vector_array[0]) \
              + (IC2_value * vector_array[1]) \
              + (IC3_value * vector_array[2]) \
              + (IC4_value * vector_array[3]) \
              + (IC5_value * vector_array[4]) \
              + (IC6_value * vector_array[5]), 3)
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
    import random as r
    aggregate = [0,1,2,3,4,5,6,7,8,9,10,11]
    random_set = []
    n = r.randint(2,10)
    for a in range(n):
        r.shuffle(aggregate)
        random_set.append(aggregate.pop())
    return random_set

# Finds the relationship between a given pitch-class set and that set's prime form
def rel_to_prime(pc_set):
    given = pc_set
    if pcs[find_prime(pc_set)][3]['FORTE'] == 'SAME':
        prime = pcs[find_prime(pc_set)][0]
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
        rahn_prime = pcs[find_prime(pc_set)][0]
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

        forte_prime = pcs[find_prime(pc_set)][3]['FORTE']
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
	aggregate = [0,1,2,3,4,5,6,7,8,9,10,11]
	for i in pc_set:
		if i in aggregate:
			aggregate.remove(i)
		else:
			pass
	return aggregate

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
                to_remove.append(intervals[j]) # Removes rotations that aren't
            else:                              # candidates for normal order
                pass
        if to_remove != []:
            for k in to_remove:
                intervals.remove(k)
        else:
            pass
        if len(intervals[0][1]) > 1: # Ensures all intervals aren't deleted
            for l in range(len(intervals)):
                del intervals[l][1][0]
        else:
            pass
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
def find_prime(pc_set):
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
    for z in pcs:
        prime = pcs[z][0]
        if prime in trans_array:
            return z
            break
        elif prime in inv_array:
            return z
            break
        else:
            pass

# Converts a pitch-class string that uses no spaces and t and e for 10 and 11 into an array
def string2array(pc_string):
    result = []
    for i in pc_string:
        if i == 't':
            result.append(10)
        elif i == 'e':
            result.append(11)
        else:
            result.append(int(i))
    return result


# Converts a pitch-class array to a string that has no spaces and uses t and e for 10 and 11
def array2string(pc_array):
    result = ''
    for i in pc_array:
        if i == 10:
            result = result + 't'
        elif i == 11:
            result = result + 'e'
        else:
            result = result + str(i)
    return result
