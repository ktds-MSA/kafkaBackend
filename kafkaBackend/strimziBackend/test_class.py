import unittest
from unittest import TestCase
from .kafkaClass import KafkaTopic
from pprint import pprint


class TestKafkaTopic(TestCase):
    def test_create(self):
        c = KafkaTopic('docker-for-desktop','kafka').create('my-topic')
        pprint(c)

    def test_get(self):
        c = KafkaTopic('docker-for-desktop','kafka').get('my-topic')
        self.assertIsNotNone(c)
        pprint(c)

    def test_delete(self):
        c = KafkaTopic('docker-for-desktop','kafka').delete('my-topic')
        pprint(c)

if __name__ == '__main__':
    unittest.main()
