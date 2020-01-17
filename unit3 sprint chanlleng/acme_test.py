import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""

    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)
        self.assertEqual(prod.weight, 20)
        self.assertEqual(prod.stealability(), 'Kinda stealable.')


class AcmeReportTests(unittest.TestCase):
    def test_default_num_products(self):
        products = generate_products()
        self.assertEqual(len(products), 30)

    def test_legal_names(self):
        products = generate_products()
        for x in products:
            name = x.name

        self.assertIn(x.name, ADJECTIVES, NOUNS)


if __name__ == '__main__':
    unittest.main()
