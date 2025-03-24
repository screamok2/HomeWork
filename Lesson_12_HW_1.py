import codecs
import re

def delete_html_tags(html_file, result_file='cleaned.txt'):
      with codecs.open(html_file, 'r', 'utf-8') as file:
           html = file.read()
           html1 = re.sub(r" *<.*?>","", html)
           html2 = re.sub( r" *<.+", "", html1)
           html3 = re.sub(r" ?[a-z]+", "", html2)
           html4 = re.sub(r" *=.+>", "", html3)
           html5 = re.sub(r" *=.*", "", html4)
           html6 = re.sub( r" +-", "", html5)
           html7 = re.sub(r"", "", html6)

      with codecs.open(result_file, "w", 'utf-8') as cleaned_file:
          cleaned_file.write(html7)





delete_html_tags(r"draft.html" , r"cleaned.txt" )