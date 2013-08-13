# -*- coding: utf-8 -*- 
from five import grok
from zope import schema
from zope.interface import implements
from plone.directives import form
from plone.dexterity.content import Item

from plone.app.textfield import RichText

from Products.Faq import faqMessageFactory as _

class IFaqEntryDx(form.Schema):
    """A Dexterity Faq entry
    """
    
    title = schema.TextLine(
        title=_(u'label_question', default=u'Question'),
        description=_(u"desc_folder", default=u"The description of the FAQ category."),
        required=True,
    )

    description = schema.Text(
        title=_(u'label_detailed_question', default=u'Detailed Question'),
        description=_(u'desc_detailed_question', default=u'More details on the question, if not evident from the title.'),
        required=False,
    )

    answer = RichText(
        title=_(u'label_answer', default=u'Answer'),
        description=_(u"desc_answer", default=u"Meaningful sentences that explains the answer."),
        allowed_mime_types=('text/html', 'text/plain',),
        default_mime_type='text/html',
        output_mime_type='text/x-html-safe',
        required=True,
    )
    
class FaqEntryDx(Item):
    """FaqEntryDx class
    """

    implements(IFaqEntryDx)

grok.context(IFaqEntryDx)
grok.templatedir('browser/templates')

class View(grok.View):
    """IFaqEntryDx View
    """
    
    grok.require('zope2.View')
    grok.name('view')
    grok.template('faq-entry')