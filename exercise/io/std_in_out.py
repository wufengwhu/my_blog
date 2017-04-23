#coding=utf-8
import sys
import optparse
if len(sys.argv )!= 3:
    sys.stderr.write("usage: python %s inputfile outputfile\n" % sys.argv[0])
    #raise SystemExit(1)

p = optparse.OptionParser()
p.add_option("-o", action="store",dest="outfile")
p.add_option("--output", action="store", dest="outfile")

p.set_defaults(debug=False)

#解析命令行
opts, args = p.parse_args()

outfile=opts.outfile