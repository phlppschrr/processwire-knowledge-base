# Fields::findByTag()

Source: `wire/core/Fields.php`

Return all fields that have the given $tag

Returns an associative array of `['field_name' => 'field_name']` if `$getFieldNames` argument is true,
or `['field_name => Field instance]` if not (which is the default).

@param string $tag Tag to find fields for

@param bool $getFieldNames If true, returns array of field names rather than Field objects (default=false).

@return array Array of Field objects, or array of field names if requested. Array keys are always field names.

@since 3.0.106
