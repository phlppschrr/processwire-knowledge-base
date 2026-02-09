# WireInputData: other

Source: `wire/core/WireInputData.php`

- [name($varName): string](method-name.md) Sanitize to ProcessWire name format
- [varName($varName): string](method-varname.md) Sanitize to PHP variable name format
- [fieldName($varName): string](method-fieldname.md) Sanitize to ProcessWire Field name format
- [templateName($varName): string](method-templatename.md) Sanitize to ProcessWire Template name format
- [pageName($varName): string](method-pagename.md) Sanitize to ProcessWire Page name format
- [pageNameTranslate($varName): string](method-pagenametranslate.md) Sanitize to ProcessWire Page name format with translation of non-ASCII characters to ASCII equivalents
- [filename($varName): string](method-filename.md) Sanitize to valid file basename as used by filenames in ProcessWire
- [pagePathName($varName): string](method-pagepathname.md) Sanitize to what could be a valid page path in ProcessWire
- [email($varName): string](method-email.md) Sanitize email address, converting to blank if invalid
- [emailHeader($varName): string](method-emailheader.md) Sanitize string for use in an email header
- [text($varName, $options = array()): string](method-text.md) Sanitize to single line of text up to 255 characters (1024 bytes max), HTML markup is removed
- [textarea($varName): string](method-textarea.md) Sanitize to multi-line text up to 16k characters (48k bytes), HTML markup is removed
- [url($varName): string](method-url.md) Sanitize to a valid URL, or convert to blank if it can't be sanitized
- [selectorField($varName): string](method-selectorfield.md) Sanitize a field name for use in a selector string
- [selectorValue($varName): string](method-selectorvalue.md) Sanitize a value for use in a selector string
- [entities($varName): string](method-entities.md) Return an entity encoded version of the value
- [purify($varName): string](method-purify.md) Return a value run through HTML Purifier (value assumed to contain HTML)
- [string($varName): string](method-string.md) Return a value guaranteed to be a string, regardless of what type $varName is. Does not sanitize.
- [date($varName, $dateFormat): string](method-date.md) Validate and return $varName in the given PHP date() or strftime() format.
- [int($varName, $min = 0, $max = null): int](method-int.md) Sanitize value to integer with optional min and max. Unsigned if max >= 0, signed if max < 0.
- [intUnsigned($varName, $min = null, $max = null): int](method-intunsigned.md) Sanitize value to unsigned integer with optional min and max.
- [intSigned($varName, $min = null, $max = null): int](method-intsigned.md) Sanitize value to signed integer with optional min and max.
- [float($varName, $min = null, $max = null, $precision = null): float](method-float.md) Sanitize value to float with optional min and max values.
- [array($varName, $sanitizer = null): array](method-array.md) Sanitize array or CSV String to an array, optionally running elements through specified $sanitizer.
- [intArray($varName, $min = 0, $max = null): array](method-intarray.md) Sanitize array or CSV string to an array of integers with optional min and max values.
- [option($varName, array $allowedValues): string|null](method-option.md) Return value of $varName only if it exists in $allowedValues.
- [options($varName, array $allowedValues): array](method-options.md) Return all values in array $varName that also exist in $allowedValues.
- [bool($varName): bool](method-bool.md) Sanitize value to boolean (true or false)
