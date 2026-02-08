# Functions::wireIconMarkupFile()

Source: `wire/core/Functions.php`

Get the markup or class name for an icon that can represent the given filename

~~~~~
// Outputs: "<i class='fa fa-pdf-o'></i>"
echo wireIconMarkupFile('file.pdf');
~~~~~


@param string $filename Can be any type of filename (with or without path).

@param string|bool $class Additional class attributes, i.e. "fw" for fixed-width (optional).
	Or specify boolean TRUE to get just the icon class name (no markup).

@return string
