#!/usr/bin/env python3
"""This module contains unit tests for utils.py"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
import requests
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """Test class for `access_nested_map` function"""

    @parameterized.expand([
        ({'a': 1}, ('a',), 1),
        ({'a': {'b': 2}}, ('a',), {'b': 2}),
        ({'a': {'b': 2}}, ('a', 'b'), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test that `access_nested_map` function returns the expected result"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ('a',), 'a'),
        ({'a': 1}, ('a', 'b'), 'b')
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """Test that `access_nested_map` function raises a KeyError for the respective inputs"""
        with self.assertRaises(KeyError) as e:
            access_nested_map(nested_map, path)
        self.assertEqual(f"KeyError('{expected}')", repr(e.exception))


class TestGetJson(unittest.TestCase):
    """Test class for `get_json` function"""

    @parameterized.expand([
        ('http://example.com', {'payload': True}),
        ('http://holberton.io', {'payload': False})
    ])
    def test_get_json(self, test_url, test_payload):
        """Test that `get_json` function returns the expected result"""
        config = {'return_value.json.return_value': test_payload}
        with patch('requests.get', **config) as mock:
            self.assertEqual(get_json(test_url), test_payload)
            mock.assert_called_once()


class TestMemoize(unittest.TestCase):
    """Test class for `memoize` decorator"""

    def test_memoize(self):
        """Test that `a_property` is memoized"""
        class TestClass:
            """Test class to be memoized"""

            def a_method(self):
                """A method to be memoized"""
                return 42

            @memoize
            def a_property(self):
                """A property to be memoized"""
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock:
            test_class = TestClass()
            test_class.a_property()
            test_class.a_property()
            mock.assert_called_once()
