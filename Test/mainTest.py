import unittest
from PyAnvil import Space,Body
class TestMovingBodyVariable(unittest.TestCase):
	def setUp(self):
		self.space=Space()
	def test_basic(self):
		print(self.space)


if __name__ == '__main__':
	unittest.main()