# encoding = utf-8

import os
import logging

import ckan.plugins as plugins
import ckan.lib.uploader as uploader
from ckan.common import config

log = logging.getLogger(__name__)

def file_remove(id):
    storage_path = uploader.get_storage_path()
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
