import os
import sys

if len(sys.argv) > 2:
    raise Exception('Only one argument is supported')
elif len(sys.argv) == 1:
    raise Exception('What u tryna generate fella ? Give me a name')


folder_name = sys.argv[1]
cur_dir = os.getcwd()
path = os.path.join(cur_dir, folder_name)

try:
    os.mkdir(path)
except OSError as error:
    print(error)
    exit(1)

parent = os.path.basename(os.path.normpath(path))

with open(os.path.join(path, 'code.py'), 'w') as f:
    f.writelines([
        'import sys\n',
        f'sys.stdout = open(\'{parent}/output.txt\', \'w\')\n'
        f'sys.stdin = open(\'{parent}/input.txt\', \'r\')\n'
    ])

    f.close()

input_f = open(os.path.join(path, 'input.txt'), 'x')
output_f = open(os.path.join(path, 'output.txt'), 'x')
