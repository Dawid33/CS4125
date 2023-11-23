# pylint: disable=too-few-public-methods
# pylint: disable=import-error
# pylint: disable=no-name-in-module

from models.database_manager.db_manager import DBManager
from models.users.admin import Admin
from instance.db import Fine
import unittest
from unittest.mock import Mock

class TestAdmin(unittest.TestCase):

    def setUp(self):
        self.mock_db_manager = Mock(spec=DBManager)
        self.admin = Admin(db_manager=self.mock_db_manager)

    def waive_fine_success(self):
        # Initialise mock IDs
        user_id = 1
        fine_id = 50
        self.mock_db_manager.get_user_fines.return_value = [Fine(fine_id, user_id, 50)] # Returns a mock value

        # Act
        result = self.admin.waive_fine(user_id, fine_id)

        # Assert
        self.mock_db_manager.pay_fine.assert_called_with(fine_id, new_balance=0)
        self.assertEqual(result, "Fine Successfully Waived")


    def waive_fine_not_found(self):
        # Initialise mock IDs
        user_id = 2
        fine_id = 100
        self.mock_db_manager.get_user_fines.return_value = []

        # Act
        result = self.admin.waive_fine(user_id, fine_id)

        # Assert
        self.assertEqual(result, "Fine not found")

if __name__ == '__main__':
    unittest.main()
