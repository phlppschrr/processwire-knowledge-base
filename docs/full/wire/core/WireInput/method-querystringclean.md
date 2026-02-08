# WireInput::queryStringClean()

Source: `wire/core/WireInput.php`

Return a cleaned query string that was part of this request, or blank if none

Note: it is recommended that you always specify $options with this method as the defaults
may or may not be consistent with your needs.


@param array $options
 - `values` (array): Optional associative array of [name=value] to use in query string rather than current GET vars. (default=[])
 - `overrides` (array): Array of values to override or add to current request values. (default=[])
 - `validNames` (array): Only include query string variables with these names, and omit any others. (default=[])
 - `maxItems` (int): Maximum number of variables/items to include in the query string or 0 for no max. (default=20)
 - `maxLength` (int): Max overall length of returned query string or 0 for no max. (default=1024)
 - `maxNameLength` (int): Max length of any “name” in the “name=value” portion of a query string or 0 for no max. (default=50)
 - `maxValueLength` (int): Max length of any “value” in the “name=value” portion of a query string or 0 for no max. (default=255)
 - `maxArrayDepth` (int): Maximum depth for arrays, or 0 to disallow arrays. (default=0)
 - `maxArrayItems` (int): Maximum number of items allowed in arrays or 0 for no max. (default=20)
 - `associative` (bool): Allow associative arrays? (default=false)
 - `sanitizeName` (string): Sanitize query string variable names with this sanitizer method or blank to ignore. (default='fieldName')
 - `sanitizeValue` (string): Sanitize query string variable values with this sanitizer method or blank to ignore. (default='line')
 - `sanitizeRemove` (bool): Remove any variables from query string that are changed as the result of sanitization? (default=true)
 - `entityEncode` (bool): Should returned query string be entity encoded for HTML output? (default=true)
 - `encType` (int): Use PHP_QUERY_RFC3986 for spaces encoded to '%20' or PHP_QUERY_RFC1738 for spaces as '+'. (default=PHP_QUERY_RFC3986)
 - `separator` (string): Character(s) that separate each “name=value” in query string. (default='&')

@return string

@since 3.0.167
