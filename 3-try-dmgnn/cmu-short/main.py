'''
Author: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
Date: 2023-09-06 20:39:56
LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
LastEditTime: 2023-09-06 21:34:04
FilePath: /zhangqq/josie-gnn-code/recomb/DMGNN-master/cmu-short/main.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import argparse
import sys
import torchlight
from torchlight import import_class


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Processor collection')

    processors = dict()
    processors['prediction'] = import_class('processor.recognition.REC_Processor')

    subparsers = parser.add_subparsers(dest='processor')
    for k, p in processors.items():
        subparsers.add_parser(k, parents=[p.get_parser()])

    arg = parser.parse_args()

    # start
    Processor = processors[arg.processor]
    p = Processor(sys.argv[2:])
    p.start()
