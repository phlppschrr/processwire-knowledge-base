# $fields->findByTag($tag, $getFieldNames = false): array

Source: `wire/core/Fields.php`

Return all fields that have the given $tag

Returns an associative array of `['field_name' => 'field_name']` if `$getFieldNames` argument is true,
or `['field_name => Field instance]` if not (which is the default).

## Arguments

- `$tag` `string` Tag to find fields for
- `$getFieldNames` (optional) `bool` If true, returns array of field names rather than Field objects (default=false).

## Return value

array Array of Field objects, or array of field names if requested. Array keys are always field names.

## Since

3.0.106
