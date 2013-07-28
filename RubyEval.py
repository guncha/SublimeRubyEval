import os, sublime, sublime_plugin, subprocess

class RubyEvalCommand(sublime_plugin.TextCommand):

  PACKAGE_PATH = os.path.dirname(os.path.abspath(__file__))

  def run(self, edit):
    self.settings = sublime.load_settings('RubyEval.sublime-settings')
    view = self.view
    selection = view.sel()
    process = subprocess.Popen(
      [
        self.settings.get("ruby"),
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
      output = process.communicate(text)

      if process.returncode != None and process.returncode != 0:
        sublime.message_dialog("There was an error: " + output[1])
        return

      view_lines = view.lines(region)
      output_lines = output[0].split('\n')
      region_length = len(view_lines)

      if len(output_lines) > region_length:
        output_lines[region_length - 1] = "\n".join(output_lines[region_length - 1:-1])
        output_lines = output_lines[0:region_length]

      view_lines.reverse()
      output_lines.reverse()

      for i in range(len(output_lines)):
        view.replace(edit, view_lines[i], output_lines[i])
