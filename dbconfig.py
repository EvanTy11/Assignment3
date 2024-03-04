import yaml
import redis


class dbconfig:
    '''Class used for db connection'''

    def __init__(self, configfile):
        '''init constructor for our dbconfig class'''
        self.configfile = configfile

    def load_config():
        '''Parses config file and returns python obj'''
        with open("config.yaml", "r") as file:
            return yaml.safe_load(file)
    # stores obj for later use
    config = load_config()

    def get_redis_connection(self):
        '''takes in self.config
        returns a redis obj'''
        return redis.Redis(
            host=self.config["redis"]["host"],
            port=self.config["redis"]["port"],
            username=self.config["redis"]["user"],
            password=self.config["redis"]["password"],
        )
