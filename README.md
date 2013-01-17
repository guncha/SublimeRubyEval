RubyEval
========

Evaluate the current file in Ruby and replace each instance of `# =>` with that lines resulting output.

## Installation

```
$ cd ~/Library/Application\ Support/Sublime\ Text\ 2/Packages
$ git clone https://github.com/kevinthompson/SublimeRubyEval.git RubyEval
```

## Usage

RubyEval will evaluate either your entire file, or the selected region, and will replace any instance of `# =>` with its evaluated result. Simply add `# =>` to the end of each line that you'd like to display the evaluated result of, then optionally select the region to parse, and execute the `ruby_eval` command using your assigned hotkey, or through Sublime Text 2's command pallette.

By default, the `ruby_eval` command is bound to `super+k, super +e`.

## Sources
This version of RubyEval was originally forked from [jugyo/SublimeRubyEval](https://github.com/jugyo/SublimeRubyEval), but the code is primarily based off of examples privided in [this superuser.com post](http://superuser.com/questions/472413/is-there-a-way-to-execute-and-update-markers-in-sublime-text-2).