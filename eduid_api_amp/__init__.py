from eduid_am.exceptions import UserDoesNotExist


def attribute_fetcher(db, user_id):
    attributes = {}

    user = db.users.find_one({'_id': user_id})
    if user is None:
        raise UserDoesNotExist("No user matching _id='%s' in collection 'users'" % user_id)

    # white list of valid attributes for security reasons
    for attr in ['c',
                 'displayName',
                 'eduID,private,credential_id',
                 'eduID,private,salt',
                 'eduPersonPrincipalName',
                 'eduPersonTargetedID',
                 'email',
                 'givenName',
                 'norEduPersonNIN',
                 'ou',
                 'sn',
                 'uid',
                 ]:
        value = user.get(attr, None)
        if value is not None:
            attributes[attr] = value

    return attributes
