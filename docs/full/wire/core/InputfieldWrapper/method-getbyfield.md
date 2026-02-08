# InputfieldWrapper::getByField()

Source: `wire/core/InputfieldWrapper.php`

Get Inputfield by Field (hasField)

This is useful in cases where the input name may differ from the Field name
that it represents, and you only know the field name. Applies only to
Inputfields connected with a Page and Field (i.e. used for page editing).


@param Field|string|int $field

@return Inputfield|InputfieldWrapper|null

@since 3.0.239
