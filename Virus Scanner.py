#!/usr/bin/python3

'''
 ' Virus Scanner in Python 3
 ' Author: Sanjan Geet Singh <>
'''

import hashlib
import sys
import os
import datetime

def now():
    return datetime.datetime.now()

def error(msg, code=-1):
    print("Error:", msg)
    exit(code)

def verifySignatures(hashes):
    for hash in hashes:
        if len(hash) != 64:
            error("Wrong Syntax in Virus Signatures Database.")

def readFile(filename, mode, error_msg):
    try:
        file = open(filename, mode)
        c = file.read()
        file.close()
        return c
    except:
        error(error_msg)

def sha256(data):
    return hashlib.sha256(data).hexdigest().lower()

def readSignatures():
    return readFile("signatures.bin", 'r', "Virus Signatures Database not found in the current directory.").lower().split('\n')

def usage():
    print('Usage: python3 "Virus Scanner.py" [file to scan]')
    exit(0)

def scan(file_to_scan):
    virus_signatures = readSignatures()
    verifySignatures(virus_signatures)
    
    file_hash = sha256(readFile(file_to_scan, 'rb', ''))

    if file_hash in virus_signatures:
        print("[+] It is a Virus.")
        return

    print("[-] It is Safe.")

if __name__ == '__main__':
    start_time = now()
    if len(sys.argv) == 2:
        file_to_scan = sys.argv[1]
        if os.path.isfile(file_to_scan):
            print("Starting Scan...")
            scan(file_to_scan)
            stop_time = now()
            print("Scan Finished")
            print("Time Elapsed:", stop_time-start_time)
        else:
            error("File {} not Found.".format(file_to_scan))
    else:
        usage()
