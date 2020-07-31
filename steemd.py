#!/usr/bin/python3 -u
#encoding:UTF-8
import json, os, sys, time
from contextlib import suppress

def init():
    env_dist = os.environ
    base_steem_path = env_dist.get('BASE_STEEM_PATH')
    if base_steem_path == None or base_steem_path == "":
        print("-------Has not config BASE_STEEM_PATH.-------")
        return
    print('BASE_STEEM_PATH is %s' % base_steem_path)
    # load config.ini file
    with open(base_steem_path + '/witness_node_data_dir/config.ini', 'r') as f:
        line = f.readlines()
        print('config.ini content: %s' % line)

def run():
    init()
    i = 1
    while True:
        print("block %i" % i)
        i = i + 1
        time.sleep(3)

if __name__ == '__main__':
    with suppress(KeyboardInterrupt):
        run()
