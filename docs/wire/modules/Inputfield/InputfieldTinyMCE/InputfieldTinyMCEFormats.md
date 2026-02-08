# InputfieldTinyMCEFormats

Source: `wire/modules/Inputfield/InputfieldTinyMCE/InputfieldTinyMCEFormats.php`

InputfieldTinyMCEFormats

Helper for managing TinyMCE style_formats and related settings

ProcessWire 3.x, Copyright 2023 by Ryan Cramer
https://processwire.com

## getBlockFormats()

Get block_formats

@return string

## getStyleFormats()

Get style_formats

@param array $defaults

@return array|mixed

## mergeStyleFormats()

Merge the given style formats

@param array $styleFormats

@param array $addFormats

@return array

## applyStyleFormatsCSS()

Add CSS that converts to style_formats and content_style

Easier-to-use alternative to the importcss plugin

@param string $css From the styleFormatsCSS setting

@param array $settings

@param array $defaults

## applyRemoveStyleFormats()

Remove style formats that have a 'remove=true' property

@param array $styleFormats

@return array

## getInvalidStyles()

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

## invalidStylesStrToArray()

Convert invalid_styles string to array

@param string $value i.e. "line-height color a=background|background-color td=height"

@param array $a Optionally merge with these styles

@return array

## invalidStylesArrayToStr()

Convert invalid_styles array to string

@param array $a

@return string
