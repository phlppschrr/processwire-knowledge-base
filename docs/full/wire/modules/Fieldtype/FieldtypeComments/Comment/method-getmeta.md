# Comment::getMeta()

Source: `wire/modules/Fieldtype/FieldtypeComments/Comment.php`

Get meta data property value (custom fields for comments)

Note: values returned are exactly as they were set and do not go through any runtime
formatting for HTML entities or anything like that. Be sure to provide your own formatting
where necessary.

@param null|string $key Name of property to get

@return string|array|int|float|mixed|null Returns value or null if not found

@since 3.0.203
