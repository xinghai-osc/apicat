import os

def getDir(plugin_name):
  dir = os.getCwd()+"plugins\"+plugin_name
  return dir
