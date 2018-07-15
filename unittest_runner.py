#!/usr/bin/env python3
import unittest


# Tests
class TestAggregation(unittest.TestCase):

    def setUp(self):
        print("Set-up")

    def tearDown(self):
        print("Tear-down")

    def test_to_logging(self):
        message = 'Hello World!'
        print(message)


if __name__ == '__main__':
    unittest.main()

