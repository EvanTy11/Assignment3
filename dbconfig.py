import yaml
import redis

class dbconfig:


    def __init__(self, configfile):
        self.configfile = configfile

    # Loads yaml config file
    def load_config():

        with open("config.yaml", "r") as file:
            return yaml.safe_load(file)

    config = load_config()

    #establishes redis db connection and returns a redis obj
    def get_redis_connection(self):

        return redis.Redis(
            host=self.config["redis"]["host"],
            port=self.config["redis"]["port"],
            username=self.config["redis"]["user"],
            password=self.config["redis"]["password"],
        )


