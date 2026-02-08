# Wire::errors()

Source: `wire/core/Wire.php`

Return or manage errors recorded by just this object or all Wire objects

This method returns and manages errors that were previously set by `Wire::error()`.

~~~~~
// Get errors for one object
$errors = $obj->errors();

// Get first error in object
$error = $obj->errors('first');

// Get errors for all Wire objects
$errors = $obj->errors('all');

// Get and clear all errors for all Wire objects
$errors = $obj->errors('clear all');
~~~~~


@param string|array $options One or more of array elements or space separated string of:
	- `first` - only first item will be returned
	- `last` - only last item will be returned
	- `all` - include all errors, including those beyond the scope of this object
	- `clear` - clear out all items that are returned from this method
	- `array` - return an array of strings rather than series of Notice objects.
	- `string` - return a newline separated string rather than array/Notice objects.

@return Notices|array|string Array of `NoticeError` errors, or string if last, first or str option was specified.
