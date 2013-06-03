import datetime

import bson

from eduid_am.exceptions import UserDoesNotExist
from eduid_am.tests import MongoTestCase
from eduid_api_amp import attribute_fetcher


TEST_DB_NAME = 'eduid_api_test'


class AttributeFetcherTests(MongoTestCase):

    def test_invalid_user(self):
        self.assertRaises(UserDoesNotExist, attribute_fetcher, self.conn['test'],
                          bson.ObjectId('000000000000000000000000'))

    def test_existing_user(self):
        user_id = self.conn['test'].users.insert({
            'email': 'john@example.com',
            'givenName': 'John',
        })
        self.assertEqual(
            attribute_fetcher(self.conn['test'], user_id),
            {'email': 'john@example.com',
            'givenName': 'John',
             }
            )

    def test_malicious_attributes(self):
        user_id = self.conn['test'].users.insert({
            'email': 'john@example.com',
            'givenName': 'John',
            'malicious': 'hacker',
        })
        # Malicious attributes are not returned
        self.assertEqual(
            attribute_fetcher(self.conn['test'], user_id),
            {'email': 'john@example.com',
             'givenName': 'John',
             }
        )
