import sublime, sublime_plugin
import os

class JasmineCoffeeScriptDetectFileTypeCommand(sublime_plugin.EventListener):
  """ Detects current file type if the file's extension isn't conclusive """
  """ Original pastie here: http://pastie.org/private/kz8gtts0cjcvkec0d4quqa """

  def on_load(self, view):
    filename = view.file_name()
    if not filename: # buffer has never been saved
      return

    name = os.path.basename(filename.lower())
    if name[-15:] == "_spec.js.coffee":
      set_syntax(view, "Jasmine CoffeeScript", "JasmineCoffeeScript")
    elif name[-12:] == "_spec.coffee":
      set_syntax(view, "Jasmine CoffeeScript", "JasmineCoffeeScript")

def set_syntax(view, syntax, path=None):
  if path is None:
    path = syntax
  view.settings().set('syntax', 'Packages/'+ path + '/Syntaxes/' + syntax + '.tmLanguage')
  print "Switched syntax to: " + syntax
