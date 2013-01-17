import os, sublime, sublime_plugin, subprocess

class RubyEvalCommand(sublime_plugin.TextCommand):

  PACKAGE_PATH = os.path.dirname(os.path.abspath(__file__))

  def run(self, edit):
    view = self.view
    region = sublime.Region(0, view.size())
    text = view.substr(region)

    settings = self.view.settings().get('ruby_eval')
    gem_home = os.system('echo $GEM_HOME')
    rcodetools = os.system('ls $GEM_HOME/gems | grep rcodetools')

    s = subprocess.Popen(      
      [
        '/usr/bin/env',
        'ruby',
        os.path.join(self.PACKAGE_PATH,'bin','xmpfilter')
      ],
      stdin=subprocess.PIPE,
      stdout=subprocess.PIPE,
      stderr=subprocess.PIPE)

    out = s.communicate(text)

    if s.returncode != None and s.returncode != 0:
      sublime.message_dialog("There was an error: " + out[1])
      return

    viewlines = view.lines(region)
    viewlines.reverse()
    outlines = out[0].split('\n')
    outlines.reverse()
    max_range = len(viewlines)

    for i in range(0, max_range):
      view.replace(edit, viewlines[i], outlines[i+1])