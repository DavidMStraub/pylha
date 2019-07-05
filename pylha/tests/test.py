import unittest
import tempfile
import pylha
import yaml
import json
import pkgutil

test_in = ['isasusy.spc',
'sdecay.bin',
'slha.txt',
'softsusy.spc',
'SPheno.spc',
'sps1a.spc',
'isajet.txt',
'SPheno-2.spc.MSSM',
'SPheno.spc.MSSM',
]

class TestLHA(unittest.TestCase):
    def test_read(self):
        for test_file in test_in:
            s = pkgutil.get_data('pylha', 'tests/data/{}'.format(test_file))
            d = pylha.load(s.decode('utf-8'))
            self.assertTrue(d) # not empty
            for k in d:
                self.assertIn(k, ['BLOCK', 'DECAY']) # no unknown blocks

    def test_exc(self):
        # this should work
        d = pylha.load(r"""BLOCK name
        1 2.0
        """)
        self.assertDictEqual(d, {'BLOCK': {'name': {'values': [[1, 2.0]]}}})
        # missing block name
        with self.assertRaises(pylha.parse.ParseError):
            pylha.load("""BLOCK
            1 2.0
            """)
        # missing block name but comment
        with self.assertRaises(pylha.parse.ParseError):
            pylha.load("""BLOCK # bla
            1 2.0
            """)
        # no block
        with self.assertRaises(pylha.parse.ParseError):
            pylha.load("""
            1 2.0
            """)

    def test_format(self):
        # various checks with differently formatted numbers and spaces
        self.assertDictEqual(pylha.load("BLOCK name\n1\t2.0 #comment"),
                             {'BLOCK': {'name': {'values': [[1, 2.0]]}}})
        self.assertDictEqual(pylha.load("BLOCK name\n  \t 1 2."),
                             {'BLOCK': {'name': {'values': [[1, 2.]]}}})
        self.assertDictEqual(pylha.load("BLOCK name\n  \t 1 2.#comment"),
                             {'BLOCK': {'name': {'values': [[1, 2.0]]}}})
        self.assertDictEqual(pylha.load("BLOCK name\n  \t 11325325 .2#comment"),
                             {'BLOCK': {'name': {'values': [[11325325, 0.2]]}}})
        self.assertDictEqual(pylha.load("BLOCK name\n1\t2.#2.0comment"),
                             {'BLOCK': {'name': {'values': [[1, 2.0]]}}})
        self.assertDictEqual(pylha.load("BLOCK name\n  \t 1 .#2.0comment"),
                             {'BLOCK': {'name': {'values': [[1, '.']]}}})
    def test_format_comments(self):
        # various checks with differently formatted numbers and spaces
        self.assertDictEqual(pylha.load("BLOCK name\n1\t2.0 #comment", comments=True),
                             {'BLOCK': {'name': {'values': [[1, 2.0, '#comment']]}}})
        self.assertDictEqual(pylha.load("BLOCK name\n  \t 1 2."),
                             {'BLOCK': {'name': {'values': [[1, 2.]]}}})
        self.assertDictEqual(pylha.load("BLOCK name\n  \t 1 2.#comment", comments=True),
                             {'BLOCK': {'name': {'values': [[1, 2.0, '#comment']]}}})
        self.assertDictEqual(pylha.load("BLOCK name\n  \t 11325325 .2#comment", comments=True),
                             {'BLOCK': {'name': {'values': [[11325325, 0.2, '#comment']]}}})
        self.assertDictEqual(pylha.load("BLOCK name\n1\t2.#2.0comment", comments=True),
                             {'BLOCK': {'name': {'values': [[1, 2.0, '#2.0comment']]}}})
        self.assertDictEqual(pylha.load("BLOCK name\n  \t 1 .#2.0comment", comments=True),
                             {'BLOCK': {'name': {'values': [[1, '.', '#2.0comment']]}}})

    def test_write(self):
        # read
        s = pkgutil.get_data('pylha', 'tests/data/SPheno.spc')
        d = pylha.load(s.decode('utf-8'))

        # export json
        s = pylha.dump(d, 'json')
        self.assertIsInstance(s, str)
        d = json.loads(s)
        self.assertIsInstance(d, dict)
        f = tempfile.TemporaryFile(mode='w+')
        pylha.dump(d, 'json', f)

        # export yaml
        s = pylha.dump(d, 'yaml')
        self.assertIsInstance(s, str)
        d = yaml.load(s)
        self.assertIsInstance(d, dict)
        f = tempfile.TemporaryFile(mode='w+')
        pylha.dump(d, 'yaml', f)

        # export lha
        s = pylha.dump(d, 'lha')
        self.assertIsInstance(s, str)
        d = pylha.load(s)
        self.assertIsInstance(d, dict)
        f = tempfile.TemporaryFile(mode='w+')
        pylha.dump(d, 'lha', f)
        pylha.load(f)
