import unittest
from unittest import TestCase
from .kafkaClass import KafkaTopic
from pprint import pprint


class TestKafkaTopic(TestCase):
    def test_get(self):
        c = KafkaTopic('kafka').get('my-topic')
        self.assertIsNotNone(c)
        pprint(c)
    def test_delete(self):
        c = KafkaTopic('kafka').delete('my-topic')
        print('herere')
        pprint(c)
    def test_create(self):
        c = KafkaTopic('kafka').createOrUpdate()
        pprint(c)

if __name__ == '__main__':
    unittest.main()
