# WireTextTools::findPlaceholders()

Source: `wire/core/WireTextTools.php`

Find and return all {placeholder} tags found in given string

@param string $str String that might contain field {tags}

@param array $options
 - `has` (bool): Specify true to only return true or false if it has tags (default=false).
	- `tagOpen` (string): The required opening tag character(s), default is '{'
	- `tagClose` (string): The required closing tag character(s), default is '}'

@return array|bool Always returns array unless you specify the `has` option as true.

@since 3.0.126
