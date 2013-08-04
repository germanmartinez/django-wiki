from django import forms
from django.forms.util import flatatt
from django.utils.encoding import force_unicode
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe
from wysihtml5.widgets import Wysihtml5TextareaWidget

from wiki.editors.base import BaseEditor

class WysiHtml5(BaseEditor):
    editor_id = 'WysiHtml5'
    
    def get_admin_widget(self, instance=None):
        return Wysihtml5TextareaWidget()
    
    def get_widget(self, instance=None):
        return Wysihtml5TextareaWidget()

    class AdminMedia:
        css = {
            'all': ("wysihtml5/css/stylesheet.css",
                    "wysihtml5/css/toolbar.css",)
        }
        js = ("wysihtml5/js/advanced.js",
              "wysihtml5/js/simple.js",
              "wysihtml5/js/wysihtml5-0.4.0pre.min.js",
              )

    class Media:
        css = {
            'all': ("wysihtml5/css/stylesheet.css",
                    "wysihtml5/css/toolbar.css",)
        }
        js = ("wysihtml5/js/advanced.js",
              "wysihtml5/js/simple.js",
              "wysihtml5/js/wysihtml5-0.4.0pre.min.js",
              )


