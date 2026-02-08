# $fieldtypeRepeaterVersions->getRepeaterPageArray(Page $page, Field $field, $value): PageArray

Source: `wire/modules/Fieldtype/FieldtypeRepeater/FieldtypeRepeaterVersions.php`

Normalize a value to a RepeaterPageArray

## Usage

~~~~~
// basic usage
$items = $fieldtypeRepeaterVersions->getRepeaterPageArray($page, $field, $value);

// usage with all arguments
$items = $fieldtypeRepeaterVersions->getRepeaterPageArray(Page $page, Field $field, $value);
~~~~~

## Arguments

- `$page` `Page`
- `$field` `Field`
- `$value` `RepeaterPage|RepeaterPageArray`

## Return value

- `PageArray`
