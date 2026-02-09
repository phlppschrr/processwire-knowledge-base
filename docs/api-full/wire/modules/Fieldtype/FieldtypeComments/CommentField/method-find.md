# $commentField->find($selectorString, array $options = array()): CommentArray

Source: `wire/modules/Fieldtype/FieldtypeComments/CommentField.php`

Find comments matching given selector

## Usage

~~~~~
// basic usage
$commentArray = $commentField->find($selectorString);

// usage with all arguments
$commentArray = $commentField->find($selectorString, array $options = array());
~~~~~

## Arguments

- $selectorString
- `$options` (optional) `array`

## Return value

- `CommentArray`
