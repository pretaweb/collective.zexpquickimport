.. contents ::

Introduction
==============

The package is monkey patch zexp import without triggering the object events.

To Solve
==============

During import zexp file, we faced a lots of errors related to event notify from object. One of the examples as below::

  2014-04-02T08:57:35 ERROR Zope.SiteErrorLog 1396393055.010.604317940455 http://localhost:8080/manage_importObject
  Traceback (innermost last):
    Module ZPublisher.Publish, line 60, in publish
    Module ZPublisher.mapply, line 77, in mapply
    Module ZPublisher.Publish, line 46, in call_object
    Module OFS.ObjectManager, line 620, in manage_importObject
    Module OFS.ObjectManager, line 642, in _importObjectFromFile
    Module OFS.ObjectManager, line 358, in _setObject
    Module zope.event, line 31, in notify
    Module zope.component.event, line 24, in dispatch
    Module zope.component._api, line 136, in subscribers
    Module zope.component.registry, line 321, in subscribers
    Module zope.interface.adapter, line 585, in subscribers
    Module zope.component.event, line 32, in objectEventNotify
    Module zope.component._api, line 136, in subscribers
    Module zope.component.registry, line 321, in subscribers
    Module zope.interface.adapter, line 585, in subscribers
    Module OFS.subscribers, line 113, in dispatchObjectMovedEvent
    Module zope.container.contained, line 153, in dispatchToSublocations
    Module zope.component._api, line 136, in subscribers
    Module zope.component.registry, line 321, in subscribers
    Module zope.interface.adapter, line 585, in subscribers
    Module Products.CMFCore.CMFCatalogAware, line 262, in handleContentishEvent
    Module Products.CMFCore.CMFCatalogAware, line 188, in notifyWorkflowCreated
    Module Products.CMFCore.WorkflowTool, line 289, in notifyCreated
    Module Products.CMFCore.WorkflowTool, line 635, in _reindexWorkflowVariables
    Module Products.Archetypes.CatalogMultiplex, line 122, in reindexObject
    Module Products.CMFPlone.CatalogTool, line 388, in catalog_object
    Module Products.ZCatalog.ZCatalog, line 476, in catalog_object
    Module Products.ZCatalog.Catalog, line 326, in catalogObject
    Module Products.ZCatalog.Catalog, line 270, in updateMetadata
    Module Products.ZCatalog.Catalog, line 394, in recordify
    Module plone.indexer.wrapper, line 59, in __getattr__
    Module plone.indexer.delegate, line 16, in __call__
    Module pretaweb.agls.browser.agls, line 155, in agls_type
    Module Products.Archetypes.Schema, line 235, in __getitem__
  KeyError: 'AGLSType'

Solution
==============

For now, we set `suppress_events` argument to `False` when calling `_setObject` function inside `_importObjectFromFile` function. 

Note
==============

This package is not fully tested. Use it at your own risk. We believe it only applicable when you want to import a whole Plone site and not part of the site.

Todo
==============

* Make the `suppress_events` optional. We are not sure setting `suppress_events` argument to `False` will have any other effects on other things. This is the next thing we are going to do.
