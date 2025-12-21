'''
Docstring for advanced-python-env.week 2.hackerrank.tuple
If u are getting negative or wrong solution just change your current language to python 2. The reason is -
Python 2: hash() for strings was generally deterministic across runs.
Python 3 (3.3+): hash() for strings and some other types is randomized between interpreter runs for security reasons, while remaining consistent within a single run.
Both versions: Differences in string encoding and representation can also lead to different hash values for seemingly identical content.
'''

if __name__ == '__main__':
  n = int(input())
  integer_list = map(int, input().split())
  print(hash(tuple(integer_list)))