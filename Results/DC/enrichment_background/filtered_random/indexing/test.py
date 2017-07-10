import os
import sys
from pysam import Fastafile
from random import randint
from math import ceil
from whoosh.index import create_in, open_dir
from whoosh.fields import Schema, NUMERIC, TEXT
from whoosh.qparser import QueryParser
from whoosh.query import Every, Term, And
from whoosh.analysis import StandardAnalyzer


schema=Schema(cpg=NUMERIC(int,32,stored=True),map=NUMERIC(int,32,stored=True),blk=NUMERIC(int,32,stored=True),region=TEXT(stored=True))
index = open_dir("mm9_map_index")

with index.searcher() as searcher:
  for i in range(0,101):
    for j in range(0,101):
      query = And([Term("map",i), Term("cpg", j)])
      results = searcher.search(query, limit=None, scored=False, sortedby=None)
      print results

