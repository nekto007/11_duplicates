import os
import sys

dublicates = []


def get_full_filenames(path):
    for root, dirnames, filenames in os.walk(path):
        for filename in filenames:
            yield os.path.join(root, filename)


def compare_files(filename1, filename2):
    if filename1 != filename2:
        if filename1[(filename1.rfind('/')+1):] == filename2[(filename2.rfind('/')+1):]:
            if os.path.getsize(filename1) == os.path.getsize(filename2):
                dublicates.append(filename1)


def find_duplicates(path):
    if os.path.exists(path):
        for filename1 in get_full_filenames(path):
            for filename2 in get_full_filenames(path):
                compare_files(filename1, filename2)
    else:
        '%s is wrong path' % path
if __name__ == '__main__':
    pass

    path = sys.argv[1]
    print('Searching for duplicates in %s' % path)
    print('Please, wait...')
    find_duplicates(path)
    print("Найденные дубликаты: ", dublicates)
    print('--- Job done ---')