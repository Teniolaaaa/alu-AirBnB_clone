#!/usr/bin/python3
"""
Unit tests for Review class.
"""
import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Test cases for Review class"""

    def test_review_inherits_from_base_model(self):
        """Test that Review inherits from BaseModel"""
        review = Review()
        self.assertIsInstance(review, BaseModel)

    def test_review_has_place_id_attribute(self):
        """Test Review has place_id attribute"""
        review = Review()
        self.assertTrue(hasattr(review, 'place_id'))
        self.assertEqual(review.place_id, "")

    def test_review_has_user_id_attribute(self):
        """Test Review has user_id attribute"""
        review = Review()
        self.assertTrue(hasattr(review, 'user_id'))
        self.assertEqual(review.user_id, "")

    def test_review_has_text_attribute(self):
        """Test Review has text attribute"""
        review = Review()
        self.assertTrue(hasattr(review, 'text'))
        self.assertEqual(review.text, "")

    def test_review_attributes_are_strings(self):
        """Test that Review attributes are strings"""
        review = Review()
        self.assertIsInstance(review.place_id, str)
        self.assertIsInstance(review.user_id, str)
        self.assertIsInstance(review.text, str)

    def test_review_to_dict(self):
        """Test Review to_dict method"""
        review = Review()
        review.place_id = "12345"
        review.user_id = "67890"
        review.text = "Great place!"

        review_dict = review.to_dict()

        self.assertEqual(review_dict['__class__'], 'Review')
        self.assertEqual(review_dict['place_id'], "12345")
        self.assertEqual(review_dict['user_id'], "67890")
        self.assertEqual(review_dict['text'], "Great place!")


if __name__ == '__main__':
    unittest.main()
