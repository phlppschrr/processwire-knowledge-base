# InputfieldTinyMCEFormats::getInvalidStyles()

Source: `wire/modules/Inputfield/InputfieldTinyMCE/InputfieldTinyMCEFormats.php`

Get TinyMCE "invalid_styles" setting and prepare as array value

Parses value in space-separated string format (commas optional):
~~~~~
line-height, color, a=background|background-color, td=height
~~~~~
In the above, line-height and color are disabled for all elements,
background and background color are disabled for "a" elements,
and height is disabled for "td" elements.

@param string|array $value

@param array|string $defaultValue

@param bool $merge Merge with given defaultValue?

@return array|string
