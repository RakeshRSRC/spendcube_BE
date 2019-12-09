import os


os.environ['POSTGRES_URL']='127.0.0.1:5432'  # Remove this line on PRODUCTION
os.environ['POSTGRES_USER']='postgres'  # Remove this line on PRODUCTION
os.environ['POSTGRES_PW']='postgres'  # Remove this line on PRODUCTION
os.environ['POSTGRES_DB']='spendcube'  # Remove this line on PRODUCTION


def get_env_variable(name):
    try:
        return os.environ[name]
    except KeyError:
        message = "Expected environment variable '{}' not set.".format(name)
        raise Exception(message)


# the values of those depend on your setup
POSTGRES_URL = get_env_variable("POSTGRES_URL")
POSTGRES_USER = get_env_variable("POSTGRES_USER")
POSTGRES_PW = get_env_variable("POSTGRES_PW")
POSTGRES_DB = get_env_variable("POSTGRES_DB")