##########
# IMPORT #
##########

import sublime
import sublime_plugin


########
# DATA #
########

class SectionboxCommand(sublime_plugin.TextCommand):
	"""
		Converts a simple section text into a nice looking secion box which make complex code way more clear
		- supports multi cursor selection
	"""
	def run(self, edit):
		for region in self.view.sel():
			if region.empty():			# Make sure that no region is selected
				line = self.view.line(region)
				lineText = (self.view.substr(line)).upper().strip(' \t\n\r')

				if lineText:			# Only add the box if there is a title
					self.view.replace(edit, line, self.commentBox(lineText))


	def commentBox(self, s):
		"""
			Packs the given string s into a box
		"""

		def wholeLine(length):
			return length * "#" + "\n"

		def innerLine():
			return "# " + s + " #\n"

		sLength = len(innerLine()) - 1

		return wholeLine(sLength) + innerLine() + wholeLine(sLength)