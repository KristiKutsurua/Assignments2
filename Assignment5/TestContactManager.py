import unittest
from contact_manager1 import ContactManager

class TestContactManager(unittest.TestCase):
    def setUp(self):
        self.contact_manager = ContactManager()
        self.contact_manager.add_contact("John", "1234567890")

    def test_add_contact(self):
        self.assertEqual(self.contact_manager.add_contact("Alice", "9876543210"), "Contact 'Alice' added successfully.")
        self.assertEqual(self.contact_manager.add_contact("John", "1111111111"), "Contact 'John' already exists.")

    def test_remove_contact(self):
        self.assertEqual(self.contact_manager.remove_contact("John"), "Contact 'John' removed successfully.")
        self.assertEqual(self.contact_manager.remove_contact("Alice"), "Contact 'Alice' not found.")

    def test_search_contact(self):
        self.assertEqual(self.contact_manager.search_contact("John"), "Name: John, Phone Number: 1234567890")
        self.assertEqual(self.contact_manager.search_contact("Alice"), "Contact 'Alice' not found.")

    def test_display_contacts(self):
        expected_output = "Name: John, Phone Number: 1234567890"
        self.assertEqual(self.contact_manager.display_contacts(), expected_output)
        empty_contact_manager = ContactManager()
        self.assertEqual(empty_contact_manager.display_contacts(), "No contacts found.")

if __name__ == "__main__":
    unittest.main()
