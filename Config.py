import os

ENVIRONMENT = os.environ.get('ENVIRONMENT', False)

if ENVIRONMENT:
    try:
        API_ID = int(os.environ.get('API_ID', 21518327))
    except ValueError:
        raise Exception("Your API_ID is not a valid integer.")
    API_HASH = os.environ.get('API_HASH', e72f588b3e4763f01eecfc3c4aa7e8ac)
    BOT_TOKEN = os.environ.get('BOT_TOKEN', '6721031289:AAF2orQmnkkSCJC7Rp7-fSehRaezexSRNtE')
    DATABASE_URL = os.environ.get('DATABASE_URL', postgres://irnfieon:K-F9J_rI1BgfI9tsoVU_jZ1NvmfABWLF@berry.db.elephantsql.com/irnfieon)
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")  # Sqlalchemy dropped support for "postgres" name.
    # https://stackoverflow.com/questions/62688256/sqlalchemy-exc-nosuchmoduleerror-cant-load-plugin-sqlalchemy-dialectspostgre
    MUST_JOIN = os.environ.get('MUST_JOIN', None)
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN.replace("@", "")
else:
    # Fill the Values
    API_ID = 0
    API_HASH = ""
    BOT_TOKEN = ""
    DATABASE_URL = ""
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
    MUST_JOIN = ""
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN[1:]
