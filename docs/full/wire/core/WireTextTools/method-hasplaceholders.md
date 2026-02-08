# WireTextTools::hasPlaceholders()

Source: `wire/core/WireTextTools.php`

Does the string have any {placeholder} tags in it?

@param string $str

@param array $options
	- `tagOpen` (string): The required opening tag character(s), default is '{'
	- `tagClose` (string): The required closing tag character(s), default is '}'

@return bool

@since 3.0.126
