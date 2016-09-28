from django.apps import AppConfig
# from beta.index import StartupIndex
# from beta.models import Startup
# 
# class BetaConfig(AppConfig):
#     name = 'beta'
# 
# from django.apps import AppConfig
# from django.contrib import algoliasearch
# 
# class apps(AppConfig):
#     name = 'beta'
# 
#     def ready(self):
#         Startup = self.get_model('startup')
#         algoliasearch.register(Startup, StartupIndex)
#         
# from django.contrib.algoliasearch import raw_search
# 
# params = { "hitsPerPage": 5 }
# raw_search(Startup, "startup", params)
# 
