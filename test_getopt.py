import sys
import test_getopt

if __name__ == '__main__':
    for item in sys.argv:
        print item


longargs = ['directory-prefix=', 'format=', '--f_long=']
try:
    opts,args =test_getopt.test_getopt( sys.argv[1:], 'f:t:', longargs)
except test_getopt.GetoptError:
    pass
print opts,args
for a,b in opts:
    if a in ('--directory-prefix',''):
        print b
    if a in ('--format',''):
        print b