import json


class MyIterator:

    def __init__(self, from_data_file, to_data_file):
        self.from_data_file = from_data_file
        self.to_data_file = to_data_file
        self.country_list = []
        self.new_line = ''
        self.count = 0
        with open(self.from_data_file, 'r') as data_file:
            data = json.load(data_file)
        for i in data:
            self.country_list.append(i['name']['common'])
        self.country = self.country_list.__iter__()

    def __iter__(self):
        return self

    def __next__(self):
        if self.count == len(self.country_list):
            raise StopIteration
        else:
            self.count += 1
            country = self.country.__next__()
            country_wiki = country.replace(' ', '_')
            country_link = f'https://en.wikipedia.org/wiki/{country_wiki}'
            self.new_line = f'{country} - {country_link}\n'
            return self.new_line

    def save_data(self):
        with open(self.to_data_file, mode='a', encoding='utf-8') as links_file:
            links_file.write(self.new_line)
