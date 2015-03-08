import os, sublime, sublime_plugin, subprocess, re

class RubyEvalCommand(sublime_plugin.TextCommand):

  PACKAGE_PATH = os.path.dirname(os.path.abspath(__file__))

  ENCODING = 'utf-8'

  def ruby(self):
      try:
          return self.view.settings().get("ruby_eval").get("ruby")
      except AttributeError:
          return "ruby"

  def run(self, edit):
    view = self.view
    selection = view.sel()
    process = subprocess.Popen(
      [
        self.ruby(),
        os.path.join(self.PACKAGE_PATH,'bin','xmpfilter'),
        "--no-warnings"
      ],
      stdin=subprocess.PIPE,
      stdout=subprocess.PIPE,
      stderr=subprocess.PIPE)

    if len(selection) == 1 and selection[0].size() == 0:
      selection = [sublime.Region(0, view.size())]

    for region in selection:
      text = view.substr(region)

      if not self.has_trailing_eval_mark(text):
        text = self.add_trailing_eval_mark(text)

      (stdout, stderr) = process.communicate(text.encode(self.ENCODING))

      if process.returncode != None and process.returncode != 0:
        sublime.message_dialog("There was an error: " + str(stderr))
        return

      view_lines = view.lines(region)
      output_lines = stdout.decode(self.ENCODING).split('\n')
      region_length = len(view_lines)

      if len(output_lines) > region_length:
        output_lines[region_length - 1] = "\n".join(output_lines[region_length - 1:-1])
        output_lines = output_lines[0:region_length]

      view_lines.reverse()
      output_lines.reverse()

      for i in range(len(output_lines)):
        view.replace(edit, view_lines[i], output_lines[i])

  def has_trailing_eval_mark(self, text):
    return re.search(r'#\s?=>.*\Z', text.strip())

  def add_trailing_eval_mark(self, text):
    return text.strip() + "\n# => "
