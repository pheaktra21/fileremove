# encoding = utf-8

import os
import logging

import ckan.plugins as plugins
from ckan.common import config

log = logging.getLogger(__name__)
_storage_path = None

## get_storage_path in ckan/ckan/lib/uploader.py
def get_storage_path():
    '''Function to cache storage path'''
    global _storage_path

    # None means it has not been set. False means not in config.
    if _storage_path is None:
        storage_path = config.get('ckan.storage_path')
        ofs_impl = config.get('ofs.impl')
        ofs_storage_dir = config.get('ofs.storage_dir')
        if storage_path:
            _storage_path = storage_path
        elif ofs_impl == 'pairtree' and ofs_storage_dir:
            log.warn('''Please use config option ckan.storage_path instead of
                     ofs.storage_dir''')
            _storage_path = ofs_storage_dir
            return _storage_path
        elif ofs_impl:
            log.critical('''We only support local file storage form version 2.2
                         of ckan please specify ckan.storage_path in your
                         config for your uploads''')
            _storage_path = False
        else:
            log.critical('''Please specify a ckan.storage_path in your config
                         for your uploads''')
            _storage_path = False

    return _storage_path

def file_remove(id):
    storage_path = get_storage_path()
    directory = os.path.join(storage_path, 'resources', id[0:3], id[3:6])
    filepath = os.path.join(directory, id[6:])

    # remove file and its directory tree
    try:
        # remove file
        os.remove(filepath)
        # remove empty parent directories
        os.removedirs(directory)
	log.info(u'File %s is deleted.' % filepath)
    except OSError, e:
	log.debug(u'Error: %s - %s.' % (e.filename, e.strerror)) 
        pass

class FileremovePlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IResourceController, inherit=True)

    def before_delete(context, data_dict, resource, resources):
	file_remove(resource['id'])
