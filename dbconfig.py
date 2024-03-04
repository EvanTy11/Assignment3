import yaml
import redis


class dbconfig:

    def __init__(self, configfile):
        self.configfile = configfile

    def load_config():
        '''returns yaml config instance'''
        with open("config.yaml", "r") as file:
            return yaml.safe_load(file)

    config = load_config()

    def get_redis_connection(self):
        '''takes in seld.config
        returns a redis obj'''
        return redis.Redis(
            host=self.config["redis"]["host"],
            port=self.config["redis"]["port"],
            username=self.config["redis"]["user"],
            password=self.config["redis"]["password"],
        )
