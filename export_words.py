#!/usr/bin/env python
import sqlite3
import sys
     
def print_words(path):
    conn = sqlite3.connect(path)
    c = conn.cursor()

    for row in c.execute('SELECT stem FROM words'):
        print row[0].lower()
        
    c.close()
    conn.close()
        
if __name__ == '__main__':
    file = sys.argv[1] if len(sys.argv) > 1 else 'vocab.db'
    
    print_words(file)