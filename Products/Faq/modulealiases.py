from Products.Faq.at.content import FaqFolder
from Products.Faq.at.content import FaqEntry

import sys
sys.modules['Products.Faq.FaqFolder'] = FaqFolder
sys.modules['Products.Faq.FaqEntry'] = FaqEntry

