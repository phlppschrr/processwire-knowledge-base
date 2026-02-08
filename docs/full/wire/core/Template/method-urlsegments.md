# Template::urlSegments()

Source: `wire/core/Template.php`

Get or set allowed URL segments


@param array|int|bool|string $value Omit to return current value, or to set value:
 - Specify array of allowed URL segments, may include 'segment', 'segment/path' or 'regex:your-regex'.
	- Or specify boolean true or 1 to enable all URL segments.
	- Or specify integer 0, boolean false, or blank array to disable all URL segments.

@return array|int Returns array of allowed URL segments, or 0 if disabled, or 1 if any allowed.
