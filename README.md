RubyEval
========

Evaluate the selection in Ruby and print the result.

## Installation

```
$ cd ~/Library/Application\ Support/Sublime\ Text\ 2/Packages
$ git clone https://github.com/kevinthompson/SublimeRubyEval.git RubyEval
```

## Usage

The `ruby_eval` command is binded to `super+k, super+e`.

## Customize

In your Preferences.sublime-settings:

``` json
{
  // ...
  "ruby_eval": {
    "ruby": "~/.rbenv/versions/2.0.0-dev/bin/ruby"
  }
  // ...
}
```

The Default is `ruby`.
