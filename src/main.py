from itertools import *
from typing import List

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
        res_sum = 0
        for variant in variant_unwrap:
            # list of str to str
            var_j = "".join(variant)
            res_sum += int(var_j)
        if res_sum < target:
            signs = []
            continue
        elif res_sum == target:
            signs = []
            variant_num = variant_unwrap
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
                    # res_sum -= double_var
                    signs.append("-")
                    res_sum = target
                elif res_sum - double_var > target:
                    signs.append("-")
                    res_sum -= double_var
                else:
                    signs.append("+")
                    pass

        if res_sum == target and len(signs) == 0:
            solution = ""
            for variant in variant_num:
                var_j = "".join(variant)
                " + ".join(solution, var_j)
            solutions.append(solution)
        elif res_sum == target:
            solution = ""
            for variant, sign in zip_longest(variant_num, signs,\
            fillvalue= "+"):
                var_j = "".join(variant)
                solution = "{} {} {}".format(solution, sign, var_j)
            solutions.append(solution)

seq = partitions("9876543210")
target = 200
solutions:List[str] = list()

sums_and_subs(seq, target, solutions)

print("Решения задачи:")
for solution in solutions:
    if solution.strip().startswith("+"):
        print(solution.replace(" + ", "", 1), end = " = {}\n".format(str(target)))
    else:
        print(solution.strip(), end = " = {}\n".format(str(target)))