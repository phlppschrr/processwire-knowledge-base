# Fields::isNative()

Source: `wire/core/Fields.php`

Is the given field name native/permanent to the database?

Such fields are disallowed from being used for custom field names.

@param string $name Field name you want to check

@return bool True if field is native (and thus should not be used) or false if it's okay to use
