"""
    Monkey patch zexp import without triggering the object events
"""
import logging
from OFS.ObjectManager import customImporters


logger = logging.getLogger('collective.zexpquickimport')


def import_object_from_file(self, filepath, verify=1, set_owner=1):
    # locate a valid connection
    logger.info("+++ start patching _importObjectFromFile")
    connection = self._p_jar
    obj = self

    while connection is None:
        obj = obj.aq_parent
        connection = obj._p_jar
    ob = connection.importFile(
        filepath, customImporters=customImporters)
    if verify:
        self._verifyObjectPaste(ob, validate_src=0)
    id = ob.id
    if hasattr(id, 'im_func'):
        id = id()
    self._setObject(id, ob, set_owner=set_owner, suppress_events=True)

    # try to make ownership implicit if possible in the context
    # that the object was imported into.
    ob = self._getOb(id)
    ob.manage_changeOwnershipType(explicit=0)
    logger.info("+++ end patching _importObjectFromFile")
