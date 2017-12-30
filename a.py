# ---------------------------------------------------------------------------
# This sample code contains some very basic items needed to get one converted
# from being a shell programmer to python programmer. It focusses on
# following items which are important for shell scripts type of programming :
#
# 1. How to process command line arguments.
# 2. How to deal with regular expressions.
# 3. How to handle files reading and writing.
# 4. How to handle invoking other commands and their ouput and return values.
# 4. Basic types and lists/tuples.
#
# Enjoy converting from shell to python
# ---------------------------------------------------------------------------

# Needed for handling command line arguments
import sys

# Needed for handlig regular expressions
import re

# Need to import subprocess to get the regular expressions
import subprocess


# How to process the command line arguments
# ---------------------------------------------------------------------------
print sys.argv  # All the arguments
print "First argument is : ", sys.argv[1]
print "Second argument is : ", sys.argv[2]
print "0th argument is (Path of command executed) : ", sys.argv[0]
print "Number of arguments (Includes the command itself) :  ", len(sys.argv)


# How to do regular expressions
# ---------------------------------------------------------------------------
for a in sys.argv:
    m = re.match('a.*[24]', a)
    if m:
        print "MATCH :", a
        print "Group : ", m.group()


# How to do files
# ---------------------------------------------------------------------------
fo = open("./testfile.txt", "r")
# Go through all the lines.
for line in fo:
    print "Line is : ", line
# Seek to start of file
fo.seek(0)
# Read the first line again
ln = fo.readline()
print "First line : ", ln
# other function of interest could be
#fo.close()
#fo.write()


# How to invoke other command and deal with their output and return values
# ---------------------------------------------------------------------------
# Simpler version. Outout of called program goes on stdout.
# Waits until command finishes
subprocess.call(["ls", "-al"])

# Flexible version. Connects with a pipe so calling program does not need
# wait.
p=subprocess.Popen(["/usr/sbin/netstat -p tcp -f inet"], stdout=subprocess.PIPE, shell=True)
while True:
    line=p.stdout.readline()
    if line == '' and p.poll() != None:
        break
    print "Reading from pipe :", line



# How to print something formatted
# ---------------------------------------------------------------------------
# Not formatted clutter
print "abc", 1, 2, "deffgg"
print "d", 88, 333, "kk"

# Same thing formatted
print("%5s %3d %4d %-10s" % ("abc", 1, 2, "deffgg"))
print("%5s %3d %4d %-10s" % ("d", 88, 333, "kk"))


# Basic data types
# ---------------------------------------------------------------------------
k = 9 # Integer
l = "junk" # Strings


# ---------------------------------------------------------------------------
# List can have mix and match of types
# List can grow
list1 = ["aa", "bb", 3, 4]
print list1
print list1[2]
print list1[-1]
k = len(list1)
list1 = list1+["aaaa", "bbbb"]
print list1
list1.extend([44, 55, "xyz"])
print list1

# Tuples are like list but can not grow
#
tuple1=("aa", "bb", 3, 4)
print tuple1
print tuple1[2]
print tuple1[-1]
tuple1=tuple1+("aaaa","bbbb")
print tuple1




