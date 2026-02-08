# AdminTheme::getClass()

Source: `wire/core/AdminTheme.php`

Return class for a given named item or blank if none available

Omit the first argument to return all classes in an array.

@param string $name Tag or item name, i.e. “input”, or omit to return all defined [tags=classes]

@param bool $getArray Specify true to return array of class name(s) rather than string (default=false). $name argument required.

@return string|array Returns string or array of class names, or array of all [tags=classes] or $tagName argument is empty.
