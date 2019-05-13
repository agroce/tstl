code = []

def init_keepsake():
    global code
    code = [1] * 5

def increment_number_0():
    code[0] = code[0] + 1
    code[4] = code[4] + 2
    fix_numbers();


def increment_number_1():
    code[1] = code[1] + 1
    code[3] = code[3] + 2
    fix_numbers();

def increment_number_2():
    code[2] = code[2] + 1
    code[0] = code[0] + 2
    fix_numbers();

def increment_number_3():
    code[3] = code[3] + 1
    code[2] = code[2] + 2
    fix_numbers()

def increment_number_4():
    code[4] = code[4] + 1
    code[1] = code[1] + 2
    fix_numbers()

def fix_numbers():
  for j in range(5):
    code[j] = (code[j] % 5) + 1
