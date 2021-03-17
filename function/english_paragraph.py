def EnglishParagraph(para):
    data = str(para, encoding='utf-8')
    data = data.replace('-\r\n', '').replace('\r\n', ' ')\
               .replace('-\r', '').replace('\r', ' ')\
               .replace('-\n', '').replace('\n', ' ')
    return data


# class EnglishParagraph():
#     def __init__(self, string):
#         self.string = str(string)
#         self.parse()

#     def parse(self):
#         self.string = self.string.replace('-\r\n', '').replace('\r\n', ' ')
#         self.string = self.string.replace('-\r', '').replace('\r', ' ')
#         self.string = self.string.replace('-\n', '').replace('\n', ' ')

#     def get(self):
#         return self.string
