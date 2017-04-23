import sqlparse
import codecs
import os
import collections
from sqlparse.filters import StripWhitespace, Tokens2Unicode
from sqlparse.lexer import tokenize
from sqlparse import tokens as T
from sqlparse import keywords
from collections import *


MY_KEYWORDS_COMMON = {
    'WHERE': T.Keyword,
    'FROM': T.Keyword,
    'INNER': T.Keyword,
    'JOIN': T.Keyword,
    'STRAIGHT_JOIN': T.Keyword,
    'AND': T.Keyword,
    'OR': T.Keyword,
    'LIKE': T.Keyword,
    'ON': T.Keyword,
    'IN': T.Keyword,
    'BY': T.Keyword,
    'GROUP': T.Keyword,
    'ORDER': T.Keyword,
    'LEFT': T.Keyword,
    'LEFT JOIN':T.Keyword,
    'RIGHT JOIN':T.Keyword,
    'LEFT OUTER JOIN':T.Keyword,
    'RIGHT OUTER JOIN':T.Keyword,
    'OUTER': T.Keyword,
    'FULL': T.Keyword,
    'FULL JOIN':T.Keyword,
    'DISTINCT': T.Keyword,
}

DIR_PATH = os.path.abspath(os.path.dirname(__file__))
PARENT_DIR = os.path.dirname(DIR_PATH)
FILES_DIR = os.path.join(DIR_PATH, 'files')

def load_file(filename, encoding='utf-8'):
    """Opens filename with encoding and return it's contents."""
    f = codecs.open(os.path.join(FILES_DIR, filename), 'r', encoding)
    data = f.read()
    f.close()
    return data

sql="""select s.appkey, 
    (s.nums - COALESCE(r.nums,0L)), 
    s.platform cnt from (select appkey,nums,platform from t where status=\'success\') s 
    left join (select appkey, nums from t where status=\'response\') r 
    on s.appkey = r.appkey;
    select * from dual group by a;
    ALTER TABLE mpns_report ADD IF NOT EXISTS 
    PARTITION (year=\'2015\', month=\'03\', day=\'30\')
    LOCATION \'/user/log/msgRecv/2015/03/30\';"""
text_sql=load_file('parse.sql')
sql_strip_whitespace=Tokens2Unicode(StripWhitespace(tokenize(text_sql)))

parsed=sqlparse.parse(sql)
keywords_counter=Counter()
def find_key_word(tokens):
    for token in tokens:
        if(token.is_group()):
            sub_tokens=token.tokens
            find_key_word(sub_tokens)
        elif(token.ttype == T.Keyword and token.value.upper() in MY_KEYWORDS_COMMON):
            keywords_counter[str(token.value.upper())] +=1
        else:
            pass

for stmt in parsed:
    find_key_word(stmt.tokens)



