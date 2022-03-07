import re

import lxml
from lxml.html.clean import Cleaner
from lxml.html import document_fromstring

# def clean_html(content):
#     doc = document_fromstring(content)
#     cleaner = Cleaner(remove_unknown_tags=False, allow_tags=['p', 'br', 'b'],
#         page_structure=True)
#     return cleaner.clean_html(doc).text_content()

def clean_html(content):
    article_cleaner = lxml.html.clean.Cleaner()
    article_cleaner.javascript = True
    article_cleaner.style = True
    article_cleaner.allow_tags = [
        'a', 'span', 'p', 'br', 'strong', 'b',
        'em', 'i', 'tt', 'code', 'pre', 'blockquote', 'img', 'h1',
        'h2', 'h3', 'h4', 'h5', 'h6',
        'ul', 'ol', 'li', 'dl', 'dt', 'dd']
    article_cleaner.remove_unknown_tags = False
    content = re.sub(r'</div></body></html>\n$', '', article_cleaner.clean_html(content))
    return content