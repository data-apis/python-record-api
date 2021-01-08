#!/usr/bin/env python
# This file was taken and modified from
# https://github.com/data-apis/dataframe-tools/
import argparse
import json
import pathlib
import os


def notebook_to_python(content):
    """
    Convert a notebook to a Python script, removing
    all markdown.

    `content` is the parsed notebook JSON.
    """
    result = []
    for cell in content['cells']:
        if cell['cell_type'] == 'code':
            if isinstance(cell['source'], str):
                cell['source'] = [cell['source']]
            for line in cell['source']:
                result += line.split('\n')

    result = [line for line in result if not line.startswith('!') and not line.startswith('%')]

    return '\n'.join(result)


def process_notebook(path):
    """
    Process the notebook in the given path to convert it into a python file.
    """
    script_id = os.path.splitext(os.path.basename(path))[0]
    with open(path, 'rb') as f:
        script_content = f.read()
        try:
            nb_content = json.loads(script_content)
        except json.JSONDecodeError:
            # not a notebook, we assume it's already a Python file
            script_as_python = script_content.decode('utf-8')
        else:
            script_as_python = notebook_to_python(nb_content)

        script_dir = pathlib.Path('scripts')
        script_dir.mkdir(parents=True, exist_ok=True)

        with open(script_dir / f'{script_id}.py', 'w') as f:
            f.write(script_as_python)


def main(directory):
    """
    Take notebooks under the given directory, convert them to python files, and
    create a directory structure ready to be executed.
    """
    for root, dirs, files in os.walk(directory):
        for f in files:
            print(f)
            if f.endswith('ipynb'):
                print('*****')
                process_notebook(os.path.join(root, f))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='notebook loader')
    parser.add_argument('dir', type=str,
                        help='Directory of the notebooks')
    args = parser.parse_args()
    main(args.dir)