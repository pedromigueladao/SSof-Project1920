#!/usr/bin/env python3

import os
import json
from pprint import pprint
import time
from termcolor import colored


'''
T14 - João Miguel Campos, Vasco Morganho, Gonçalo Santos

This script will run all tests inside the public test repo, available @ https://github.com/pedromigueladao/SSof-Project1920.

NOTE: This may not yield perfect results, as some outputs may be correct only for that group, based on group choices on how to tackle the problem. For example, you may have duplicate vulnerabilities reported, or you may have an output where two sources are in the same reported vulnerability.

You should clone the repo, on the same directory of this script. It will then run all tests, leaving the diff and each test log (our program had a log) on this directory. The output your program gave will be stored inside the folder of each test, so do not commit.

You should probably add the SSof-Project1920 and *.diff.out to your gitignore, so the files won't bother you.

If you are having problems running the script due to termcolor, you can just pip install termcolor.

If you don't want to install it, just remove the import.
'''


TESTS_PASSED = 0;
TESTS_FAILED = 0;
TESTS_TOTAL = 0;

TEST_DIRECTORY = "SSof-Project1920/"

def ordered(obj):
    ''' Function used to compare json, since they will probably be out of order'''
    if isinstance(obj, dict):
        return sorted((k, ordered(v)) for k, v in obj.items())
    if isinstance(obj, list):
        return sorted(ordered(x) for x in obj)
    else:
        return obj

os.system("rm -f *.diff.out")

for root, dirs, files in os.walk("."):
    for direct in dirs:
        if direct.startswith("T") or direct.startswith("A"):
            print("=== RUNNING TEST " + direct + " ===\n")
            os.system("python ../tool.py " + TEST_DIRECTORY + direct + "/input.json " +  TEST_DIRECTORY + direct + "/patterns.json")


            file1 = TEST_DIRECTORY + direct + "/output.json"
            file2 = TEST_DIRECTORY + direct + "/input.output.json"

            try:
                with open(file1) as f1:
                    data_gud = json.load(f1)

                with open(file2) as f2:
                    data_maybe_gud = json.load(f2)

                if (ordered(data_gud) == ordered(data_maybe_gud)):
                    TESTS_PASSED += 1;
                    print(colored("== !! TEST SUCCESSFUL !! ==\n", "green"))
                    TESTS_TOTAL += 1;
                    print("=== ENDED TEST " + direct + " ===\n\n")

                elif (ordered(data_gud) != ordered(data_maybe_gud)):
                    print(colored("TEST " + direct + " FAILED! Open file " + direct + ".diff.out to see output.\n", "red"))

                    filename_diff = direct + ".diff.out"

                    file3 = open(filename_diff,"w+")
                    file3.write("=== OUR OUTPUT ===\n")
                    file3.write(json.dumps(ordered(data_maybe_gud), indent = 4))
                    file3.write("=== THE SUPPOSED OUTPUT ===\n")
                    file3.write(json.dumps(ordered(data_gud), indent = 4))
                    file3.close()

                    TESTS_FAILED += 1;
                    TESTS_TOTAL += 1;
                    print("=== ENDED TEST " + direct + " ===\n\n")
            except:
                continue;




print("\n=== TEST RESULTS ===\n")
print("TOTAL TESTS EXECUTED = %d" % TESTS_TOTAL)
print(colored("TESTS PASSED = %d" % TESTS_PASSED, "green"))
print(colored("TESTS FAILED = %d" % TESTS_FAILED, "red"))
