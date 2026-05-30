from urllib import parse
import os

f = open('C:/Users/011024/Downloads/72c81a85-7938-4771-8d65-4907a17e6d12/access.log', 'r')
s = open('C:/Users/011024/Downloads/72c81a85-7938-4771-8d65-4907a17e6d12/access.res', 'w')

tmp = parse.unquote(f.read())
s.write(tmp)