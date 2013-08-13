# -*- coding: utf-8 -*- 
from zope import schema
from five import grok
from zope.interface import implements
from plone.directives import form
from plone.dexterity.content import Container

from Products.Faq import faqMessageFactory as _

class IFaqFolderDx(form.Schema):
    """A Dexterity folder that can contain Faq
    """
    
    title = schema.TextLine(
        title=_(u"Title"),
        required=True,
    )

    description = schema.Text(
        title= _(u"label_folder", default=u"Description"),
        description=_(u"desc_folder", default=u"The description of the FAQ category."),
        required=False,
    )
    
    delay = schema.Int(
        title=_(u"label_delay", default=u"Delay"),
        description=_(u"desc_delay", default=u"Delay for a new item."),
        required=True,
        default=7,
        min=0,
        max=99999,
    )

class FaqFolderDx(Container):
    """FaqFolderDx class
    """

    implements(IFaqFolderDx)
    
grok.context(IFaqFolderDx)
grok.templatedir('browser/templates')

class View(grok.View):
    """IFaqEntryDx View
    """
    
    grok.context(IFaqFolderDx)
    grok.require('zope2.View')
    grok.name('view')
    grok.template('faq-folder')