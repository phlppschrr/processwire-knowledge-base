# WireInputData: other

Source: `wire/core/WireInputData.php`

- name($varName): string Sanitize to ProcessWire name format

- varName($varName): string Sanitize to PHP variable name format

- fieldName($varName): string Sanitize to ProcessWire Field name format

- templateName($varName): string Sanitize to ProcessWire Template name format

- pageName($varName): string Sanitize to ProcessWire Page name format

- pageNameTranslate($varName): string Sanitize to ProcessWire Page name format with translation of non-ASCII characters to ASCII equivalents

- filename($varName): string Sanitize to valid file basename as used by filenames in ProcessWire

- pagePathName($varName): string Sanitize to what could be a valid page path in ProcessWire

- email($varName): string Sanitize email address, converting to blank if invalid

- emailHeader($varName): string Sanitize string for use in an email header

- text($varName, $options = array(): string ) Sanitize to single line of text up to 255 characters (1024 bytes max), HTML markup is removed

- textarea($varName): string Sanitize to multi-line text up to 16k characters (48k bytes), HTML markup is removed

- url($varName): string Sanitize to a valid URL, or convert to blank if it can't be sanitized

- selectorField($varName): string Sanitize a field name for use in a selector string

- selectorValue($varName): string Sanitize a value for use in a selector string

- entities($varName): string Return an entity encoded version of the value

- purify($varName): string Return a value run through HTML Purifier (value assumed to contain HTML)

- string($varName): string Return a value guaranteed to be a string, regardless of what type $varName is. Does not sanitize.

- date($varName, $dateFormat): string Validate and return $varName in the given PHP date() or strftime() format.

- int($varName, $min = 0, $max = null): int Sanitize value to integer with optional min and max. Unsigned if max >= 0, signed if max < 0.

- intUnsigned($varName, $min = null, $max = null): int Sanitize value to unsigned integer with optional min and max.

- intSigned($varName, $min = null, $max = null): int Sanitize value to signed integer with optional min and max.

- float($varName, $min = null, $max = null, $precision = null): float Sanitize value to float with optional min and max values.

- array($varName, $sanitizer = null): array Sanitize array or CSV String to an array, optionally running elements through specified $sanitizer.

- intArray($varName, $min = 0, $max = null): array Sanitize array or CSV string to an array of integers with optional min and max values.

- option($varName, array $allowedValues): string|null Return value of $varName only if it exists in $allowedValues.

- options($varName, array $allowedValues): array Return all values in array $varName that also exist in $allowedValues.

- bool($varName): bool Sanitize value to boolean (true or false)
