#!/usr/bin/python
# coding: utf-8


class WordsFinder():
    def __init__(self, *file_names):
        self.file_names = file_names


    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file=file_name, mode="r", encoding="utf-8") as file:
                result_str = file.read()
                for str_ in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    result_str = result_str.replace(str_, " ")
                all_words.update({file_name: result_str.split()}) 
        return all_words        

    def find(self, word):
        result_dict = {}
        for i, j in self.get_all_words().items():
            for value in j:
                if value.lower() == word.lower():
                    result_dict.update({i: j.index(value )+1})
                    continue
        return result_dict
    
    def count(self, word):
        result_dict = {}
        for i, j in self.get_all_words().items():
            count = 0
            for value in j:
                if value.lower() == word.lower():
                    count += 1
            result_dict.update({i: count})
        return result_dict

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
