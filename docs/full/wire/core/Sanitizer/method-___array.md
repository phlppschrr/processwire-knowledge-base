# Sanitizer::___array()

Source: `wire/core/Sanitizer.php`

Sanitize array or CSV string to array of values, optionally sanitized by given method

If given a string, delimiter may be pipe ("|"), or comma (","), unless overridden with the `delimiter`
or `delimiters` options.


@param array|string|mixed $value Accepts an array or CSV string.
  If given something else, it becomes first item in array.

@param string|array $sanitizer Sanitizer method to apply to items in the array or omit/null for none,
  or in 3.0.165+ optionally substitute the $options argument here instead (default=null).

@param array $options Optional modifications to default behavior:
	- `maxItems` (int): Maximum items allowed in each array (default=0, which means no limit)
 - `maxDepth` (int): Max nested array depth (default=0, which means no nesting allowed) Since 3.0.160
 - `trim` (bool): Trim whitespace from front/back of each string item in array? (default=true) Since 3.0.190
	- `sanitizer` (string): Optionally specify sanitizer for array values as option rather than argument (default='') Since 3.0.165
	- `keySanitizer` (string): Optionally sanitize associative array keys with this method (default='') Since 3.0.167
	- The following options are only used if the provided $value is a string:
 - `csv` (bool): Allow conversion of delimited string to array? (default=true) Since 3.0.165
	- `delimiter` (string): Single delimiter to use to identify CSV strings. Overrides the 'delimiters' option when specified (default=null)
	- `delimiters` (array): Delimiters to identify CSV strings. First found delimiter will be used, default=array("|", ",")
	- `enclosure` (string): Enclosure to use for CSV strings (default=double quote, i.e. `"`)
	- `escape` (string): Escape to use for CSV strings (default=backslash, i.e. "\\")

@return array

@throws WireException if an unknown $sanitizer method is given
