# $fieldtypeMulti->___loadPageField(Page $page, Field $field): array|null

Source: `wire/core/FieldtypeMulti.php`

Load the given page field from the database table and return the value.

- Return NULL if the value is not available, or array when it is.
- Return the value as it exists in the database (as an array), without further processing.
- This is intended only to be called by Page objects on an as-needed basis.
- Typically this is only called for fields that don't have 'autojoin' turned on.
- Any actual conversion of the value should be handled by the `Fieldtype::wakeupValue()` method.

If pagination is active, the following extra properties are populated to the returned array value:

- `_pagination_limit` (int): The specified limit of items per pagination.
- `_pagination_start` (int): The starting index of the pagination.
- `_pagination_total` (int): The total number of items across all paginations.

## Usage

~~~~~
// basic usage
$array = $fieldtypeMulti->___loadPageField($page, $field);

// usage with all arguments
$array = $fieldtypeMulti->___loadPageField(Page $page, Field $field);
~~~~~

## Arguments

- `$page` `Page` Page object to save.
- `$field` `Field` Field to retrieve from the page.

## Return value

- `array|null`
