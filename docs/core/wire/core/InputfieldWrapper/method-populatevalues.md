# InputfieldWrapper::populateValues()

Source: `wire/core/InputfieldWrapper.php`

Populate values for all Inputfields in this wrapper from the given $data object or array.

This iterates through every field in this InputfieldWrapper and looks for field names
that are also present in the given object or array. If present, it uses them to populate
the associated Inputfield.

If given an array, it should be an associative with the field 'name' as the keys and
the field 'value' as the array value, i.e. `['field_name' => 'field_value']`.


@param WireData|Wire|ConfigurableModule|array $data

@return array Returns array of field names that were populated
