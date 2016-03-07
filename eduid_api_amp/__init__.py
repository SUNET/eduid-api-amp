from eduid_userdb.exceptions import UserDoesNotExist


def attribute_fetcher(db, _id):
    attributes = {}

    user = db.users.find_one({'_id': _id})
    if user is None:
        raise UserDoesNotExist("No user matching _id=%s in collection 'users'" % repr(_id))

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
