class Config:
    @staticmethod
    def init_app(app):
        pass

class ProdConfig(Config):

    pass

class DevConfig(Config):

    DEBUG = True

config_options = {
'development' : DevConfig,
'production' : ProdConfig

}
