import collections
import json
from pprint import pprint


max_len_word = 6
top_words = 10
def read_json(file_path):
    with open(file_path, encoding='utf-8') as new_fale:
        news = json.load(new_fale)
        pprint(news)
        description_words = []
        for item in news['rss']['channel']['items']:
            description = [word for word in item['description'].split(' ') if len(word) > max_len_word]
            description_words.extend(description)
            counrer_words = collections.Counter(description_words)
        pprint(counrer_words.most_common(top_words))

if __name__ =='__main__':
    read_json('newsafr.json')

print('@' * 50)

# import xml.etree.ElementTree as ET
#
# parser = ET.XMLParser(encoding='utf-8')
# xml_data = ET.parse('newsafr.xml', parser)
# xml_root = xml_data.getroot()
#
# def read_xml():
#     descriptions = xml_root.findall('channel/item/description')
#     descriptions_word = []
#     for descrip in descriptions:
#         for word in descrip:
#             if len(word) > max_len_word:
#                 descriptions_word.extend(word)
#         print(descriptions_word)
        # for word in descrip
    #     description = [word for word in i if len(word) > max_len_word]
    #     descriptions_word.extend(description)
    #     counter_word = collections.Counter(descriptions_word)
    # pprint(counter_word.most_common(top_words))

#read_xml()