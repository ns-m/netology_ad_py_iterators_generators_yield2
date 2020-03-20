from classes.iterator_class import MyIterator
from classes.generator import md5


if __name__ == '__main__':
    myiterator = MyIterator
    start = myiterator('data/countries.json', 'data/links.txt')
    for _ in start:
        start.save_data()
    print('Data written to file links.txt ')

    for _ in md5('data/links.txt'):
        print(_)
