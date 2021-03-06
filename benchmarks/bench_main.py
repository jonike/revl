#!/usr/bin/env mayapy

import os
import sys
import unittest

import maya.standalone
from maya import OpenMaya

_HERE = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(_HERE, os.pardir)))

import revl

maya.standalone.initialize()


class MainBench(unittest.TestCase):

    def setUp(self):
        OpenMaya.MFileIO.newFile(True)

    def benchCreatePrimitive1(self):
        count = 5000
        commands = [
            (1.0, revl.createPrimitive,)
        ]
        revl.run(commands, count)

    def benchCreatePrimitive2(self):
        count = 5000
        commands = [
            (1.0, revl.createPrimitive, (), {'type': revl.PrimitiveType.POLY_CUBE})
        ]
        revl.run(commands, count)

    def benchCreatePrimitive3(self):
        count = 5000
        commands = [
            (1.0, revl.createPrimitive, (), {'name': 'primitive'})
        ]
        revl.run(commands, count)

    def benchCreatePrimitive4(self):
        count = 5000
        commands = [
            (1.0, revl.createPrimitive, (), {'parent': True})
        ]
        revl.run(commands, count)

    def benchCreatePrimitive5(self):
        count = 5000
        commands = [
            (1.0, revl.createPrimitive, (), {'parent': True, 'forceTransformCreation': False})
        ]
        revl.run(commands, count)

    def benchCreateTransform1(self):
        count = 5000
        commands = [
            (1.0, revl.createTransform,)
        ]
        revl.run(commands, count)

    def benchCreateTransform2(self):
        count = 5000
        commands = [
            (1.0, revl.createTransform, (), {'name': 'xform'})
        ]
        revl.run(commands, count)

    def benchCreateTransform3(self):
        count = 5000
        commands = [
            (1.0, revl.createTransform, (), {'parent': True})
        ]
        revl.run(commands, count)


if __name__ == '__main__':
    from benchmarks.run import run
    run('__main__')
