# Sanitizer::match()

Source: `wire/core/Sanitizer.php`

Validate that given value matches regex pattern.

If given value matches, value is returned. If not, blank is returned.


@param string $value Value to match

@param string $regex PCRE regex pattern (same as you would provide to PHP's `preg_match()`)

@return string Value you supplied if it matches, or blank string if it doesn't
