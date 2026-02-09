# $selectableOptionArray->hasID($id): SelectableOption|bool

Source: `wire/modules/Fieldtype/FieldtypeOptions/SelectableOptionArray.php`

Is the given id present in these selectable options?

## Usage

~~~~~
// basic usage
$selectableOption = $selectableOptionArray->hasID($id);
~~~~~

## Arguments

- `$id` `int`

## Return value

- `SelectableOption|bool` Returns SelectableOption if found, or boolean false if not
