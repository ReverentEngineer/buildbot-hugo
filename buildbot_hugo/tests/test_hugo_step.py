#!/usr/bin/env python3
from twisted.trial import unittest

from buildbot.test.util.misc import TestReactorMixin
from buildbot.test.util.steps import BuildStepMixin

class TestHugo(BuildStepMixin, TestReactorMixin, unittest.TestCase):

    def setUp(self):
        self.setUpTestReactor()
        self.setUpBuildStep()

    def test_one(self):
        pass

    def tearDown(self):
        self.tearDownBuildStep()


if __name__ == '__main__':
    unittest.main()
