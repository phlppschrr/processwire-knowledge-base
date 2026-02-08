# Wire::warnings()

Source: `wire/core/Wire.php`

Return or manage warnings recorded by just this object or all Wire objects

This method returns and manages warnings that were previously set by `Wire::warning()`.

~~~~~
// Get warnings for one object
$warnings = $obj->warnings();

// Get first warning in object
$warning = $obj->warnings('first');

// Get warnings for all Wire objects
$warnings = $obj->warnings('all');

// Get and clear all warnings for all Wire objects
$warnings = $obj->warnings('clear all');
~~~~~


@param string|array $options One or more of array elements or space separated string of:
	- `first` - only first item will be returned
	- `last` - only last item will be returned
	- `all` - include all errors, including those beyond the scope of this object
	- `clear` - clear out all items that are returned from this method
	- `array` - return an array of strings rather than series of Notice objects.
	- `string` - return a newline separated string rather than array/Notice objects.

@return Notices|array|string Array of `NoticeWarning` warnings, or string if last, first or str option was specified.
