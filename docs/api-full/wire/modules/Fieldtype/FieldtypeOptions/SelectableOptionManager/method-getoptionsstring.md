# $selectableOptionManager->getOptionsString(SelectableOptionArray $options, $language = ''): string

Source: `wire/modules/Fieldtype/FieldtypeOptions/SelectableOptionManager.php`

Get the options input string used for

## Usage

~~~~~
// basic usage
$string = $selectableOptionManager->getOptionsString($options);

// usage with all arguments
$string = $selectableOptionManager->getOptionsString(SelectableOptionArray $options, $language = '');
~~~~~

## Arguments

- `$options` `SelectableOptionArray`
- `$language` (optional) `int|string|Language` Language id, object, or name, if applicable

## Return value

- `string`

## Exceptions

- `WireException` if given invalid language
