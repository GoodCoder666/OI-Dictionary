from difflib import SequenceMatcher
from os.path import join

from yaml import CSafeLoader

__all__ = ['load_database', 'search']

def _read_yml(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        loader = CSafeLoader(file)
        data = loader.get_single_data()
        loader.dispose()
        return data

def load_database(data_path='./data', info_file='dict_info.yml'):
    return [(db['name'], db['description'], _read_yml(join(data_path, db['path']))) for db in _read_yml(join(data_path, info_file))]

def search(word, dictionary, n=20, cutoff=0.6):
    # Modified from difflib.get_close_matches()
    result = []
    s = SequenceMatcher()
    s.set_seq2(word.lower())
    for x in dictionary:
        s.set_seq1(x['name'].lower())
        if s.real_quick_ratio() >= cutoff and s.quick_ratio() >= cutoff and s.ratio() >= cutoff:
            result.append((s.ratio(), x))
    return [x for _, x in sorted(result, key=lambda x: x[0], reverse=True)[:n]]