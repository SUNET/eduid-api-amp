import bson

from eduid_userdb.exceptions import UserDoesNotExist
from eduid_userdb.testing import MongoTestCase
from eduid_api_amp import attribute_fetcher
from eduid_am.celery import celery, get_attribute_manager


TEST_DB_NAME = 'eduid_api_test'


class AttributeFetcherTests(MongoTestCase):

    def setUp(self, settings={}, skip_on_fail=False, std_user='johnsmith@example.com'):

        super(AttributeFetcherTests, self).setUp(celery, get_attribute_manager, userdb_use_old_format=True)

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
