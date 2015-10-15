__author__ = 'HB_Y'
import sys
# import external python file in order to call _word_count
import utility

# the source file name and destination file name
# the source contain plain text
# the destination file contain the result of _word_count
_file_source_path = "demo_source.txt"
_file_des_path = "demo_des.txt"

try:
    # open the input file and pass it to a file object called inputFile
    inputFile = open(_file_source_path, "r+")
    # open the destination file to which the output will be going
    outputFile = open(_file_des_path,"w+");

    str = inputFile.read()
    dict={}
    dict = utility.word_frequecy_count(str)
    for k,v in dict.items():
        outputFile.write(k+ " " + v.__str__()+"\n")

except IOError as e:
    print("I/O error({0}): {1}".format(e.errno, e.strerror))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise

