# WireInput::queryString()

Source: `wire/core/WireInput.php`

Return the unsanitized query string that was part of this request, or blank if none

Note that the returned query string is not sanitized, so if you use it in any output
be sure to run it through `$sanitizer->entities()` first. An optional assoc array
param can be used to add new GET params or override existing ones.


@param array $overrides Optional assoc array for overriding or adding GET params

@return string Returns the unsanitized query string

@see WireInput::queryStringClean()
