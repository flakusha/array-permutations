from itertools import *
from typing import List, Dict

# more_itertools
def powerset(iter):
    seq = list(iter)
    return chain.from_iterable(combinations(seq, r) for r in\
    range(len(seq) + 1))

# more_itertools
def partitions(iter):
    seq = list(iter)
    len_seq = len(seq)
    for item in powerset(range(1, len_seq)):
        yield [seq[item:j] for item, j in zip((0,) + item, item + (len_seq,))]

def sums_and_subs(variants, target, solutions):
    result = None
    valid_variants = []
    for variant_unwrap in variants:
        # print()
        print(variant_unwrap)
        res_sum = 0
        for variant in variant_unwrap:
            # list of str to str
            var_j = "".join(variant)
            res_sum += int(var_j)
        print(res_sum)
        if res_sum < target:
            # print("Sum is less")
            signs = []
            continue
        elif res_sum == target:
            signs = []
            variant_num = variant_unwrap
            print("Found solution (1)")
        else:
            variant_num = []
            signs = []
            for variant in variant_unwrap:
                # list of str to str
                var_j = "".join(variant)
                variant_num.append(variant)
                # str to int
                var_i = int(var_j)

                double_var = var_i * 2
                if res_sum - double_var == target:
                    print("Found solution (2)")
                    # res_sum -= double_var
                    signs.append("-")
                    # TODO
                    res_sum = target
                elif res_sum - double_var > target:
                    signs.append("-")
                    res_sum -= double_var
                else:
                    signs.append("+")
                    pass

        if res_sum == target and len(signs) == 0:
            print("Solution (1)")
            solution = ""
            for variant in variant_num:
                var_j = "".join(variant)
                "+".join(solution, var_j)
            solutions.append(solution)
        elif res_sum == target:
            print("Solution (2)")
            solution = ""
            for variant, sign in zip_longest(variant_num, signs,\
            fillvalue= "+"):
                var_j = "".join(variant)
                print(var_j, sign)
                solution = "{}{}{}".format(solution, sign, var_j)
            solutions.append(solution)

seq = partitions("9876543210")
# print(len(list(seq)))
target = 200
solutions:List[str] = list()

sums_and_subs(seq, target, solutions)

print(solutions)

# variants = partitions(seq)
# print(len(list(variants)))

