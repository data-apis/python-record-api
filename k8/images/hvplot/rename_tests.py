import glob
import shutil
import os.path as osp
all_tests = glob.glob('hvplot/tests/test*')
for test_file in all_tests:
    print(test_file)
    print(test_file.split('test'))
    *_, rest = test_file.split('test')
    new_path = osp.join('hvplot/tests', f'test_{rest}')
    print(rest)
    shutil.move(test_file, new_path)