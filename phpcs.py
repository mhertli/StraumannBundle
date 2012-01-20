import os
import sublime
import sublime_plugin

class PhpcsCommand(sublime_plugin.TextCommand):  
    def run(self, edit):  
    	self.view.window().run_command("save")
    	folder_name, file_name = os.path.split(self.view.file_name())
     	self.view.window().run_command("exec", {'cmd': ['/usr/local/php5-20111115-115202/bin//phpcs',file_name]})
     	sublime.status_message("CodeSniffer executed on " + file_name)