# $selectableOptionArray->hasTitle($title): SelectableOption|bool

Source: `wire/modules/Fieldtype/FieldtypeOptions/SelectableOptionArray.php`

Is the given title present in these selectable options?

## Usage

~~~~~
// basic usage
$selectableOption = $selectableOptionArray->hasTitle($title);
~~~~~

## Arguments

- `$title` `string`

## Return value

- `SelectableOption|bool` Returns SelectableOption if found, or boolean false if not
