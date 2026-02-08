# WireInputData: other

Source: `wire/core/WireInputData.php`

@method string name($varName) Sanitize to ProcessWire name format

@method string varName($varName) Sanitize to PHP variable name format

@method string fieldName($varName) Sanitize to ProcessWire Field name format

@method string templateName($varName) Sanitize to ProcessWire Template name format

@method string pageName($varName) Sanitize to ProcessWire Page name format

@method string pageNameTranslate($varName) Sanitize to ProcessWire Page name format with translation of non-ASCII characters to ASCII equivalents

@method string filename($varName) Sanitize to valid file basename as used by filenames in ProcessWire

@method string pagePathName($varName) Sanitize to what could be a valid page path in ProcessWire

@method string email($varName) Sanitize email address, converting to blank if invalid

@method string emailHeader($varName) Sanitize string for use in an email header

@method string text($varName, $options = array()) Sanitize to single line of text up to 255 characters (1024 bytes max), HTML markup is removed

@method string textarea($varName) Sanitize to multi-line text up to 16k characters (48k bytes), HTML markup is removed

@method string url($varName) Sanitize to a valid URL, or convert to blank if it can't be sanitized

@method string selectorField($varName) Sanitize a field name for use in a selector string

@method string selectorValue($varName) Sanitize a value for use in a selector string

@method string entities($varName) Return an entity encoded version of the value

@method string purify($varName) Return a value run through HTML Purifier (value assumed to contain HTML)

@method string string($varName) Return a value guaranteed to be a string, regardless of what type $varName is. Does not sanitize.

@method string date($varName, $dateFormat) Validate and return $varName in the given PHP date() or strftime() format.

@method int int($varName, $min = 0, $max = null) Sanitize value to integer with optional min and max. Unsigned if max >= 0, signed if max < 0.

@method int intUnsigned($varName, $min = null, $max = null) Sanitize value to unsigned integer with optional min and max.

@method int intSigned($varName, $min = null, $max = null) Sanitize value to signed integer with optional min and max.

@method float float($varName, $min = null, $max = null, $precision = null) Sanitize value to float with optional min and max values.

@method array array($varName, $sanitizer = null) Sanitize array or CSV String to an array, optionally running elements through specified $sanitizer.

@method array intArray($varName, $min = 0, $max = null) Sanitize array or CSV string to an array of integers with optional min and max values.

@method string|null option($varName, array $allowedValues) Return value of $varName only if it exists in $allowedValues.

@method array options($varName, array $allowedValues) Return all values in array $varName that also exist in $allowedValues.

@method bool bool($varName) Sanitize value to boolean (true or false)
