# SectionBox
### Helps to structure your code and makes it clearer

---

This Sublime Text 3 Plugin helps you to sturcture complex code by creating eye-catching section heading with just one click. e.g.:

	########  #############  ##########
	# DATA #  # VARIABLES #  # IMPORT #
	########, #############, ##########
At the moment the package just works for languages whichs comment character is a `#` like for example Python. Support for further languages will be added in future versions.

---

## Installation:
1. In your Sublime Text 3 click `Preferences > Browse Packages`
2. Download the package and copy the CommenBox project folder into the previously opened `Packages`folder
3. Restart Sublime Text 3


## Usage:
1. Write the name of the section, e.g. `Test`
2. Place the cursor somewhere in this line and press the default shortcut <kbd>cmd</kbd>+<kbd>ctrl</kbd>+<kbd>s</kbd> (for Windows use the windows key instead)
`Edit > SectionBox` can be used instead
3. A section box as follows will be created:

``` ```

    ########
    # TEST #
    ########

## TODO:
* Support language dependant comment character 
* Add sectionBoxes with a indentation