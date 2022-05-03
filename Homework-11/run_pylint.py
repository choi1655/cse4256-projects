import os
import sys

def run_before_pylint():
    files = os.listdir('./')

    for file in files:
        if file.endswith('.py'):
            filename = file.split('.')[0]
            os.system(f'pylint {file} > before_{filename}.txt')

def run_after_pylint():
    files = os.listdir('./')

    for file in files:
        if file.endswith('.py'):
            filename = file.split('.')[0]
            os.system(f'pylint {file} > after_{filename}.txt')

def main(is_before=False, filename=None):

    dir_name = './';
    folder_names = ['Homework-01', 'Homework-03', 'Homework-05', 'Homework-07', 'Homework-09']
    if filename:
        folder_names = [filename]
    os.chdir(dir_name)
    for folder in folder_names:
        path = dir_name + folder + '/'
        os.chdir(path)
        run_before_pylint() if is_before else run_after_pylint()
        os.chdir('../')


if __name__ == '__main__':

    def usage():
        print('usage: python run_pylint.py [before|after|FolderName]')
        sys.exit(-1)

    if len(sys.argv) != 2:
        usage()
    if sys.argv[1] == 'before' or sys.argv[1] == 'after':
        main(sys.argv[1] == 'before')
    else:
        main(filename=sys.argv[1])