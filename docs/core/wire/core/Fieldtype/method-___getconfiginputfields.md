# $fieldtype->getConfigInputfields(Field $field): InputfieldWrapper

Source: `wire/core/Fieldtype.php`

Get any Inputfields used for configuration of this Fieldtype.

This is in addition to any configuration fields supplied by the Inputfield.

Classes implementing this method should call upon this parent method to obtain the InputfieldWrapper, and then
append their own Inputfields to that.

NOTE: Inputfields with a name that starts with an underscore, i.e. "_myname" are assumed to be for runtime
use and are NOT stored in the database.

## Usage

~~~~~
// basic usage
$inputfieldWrapper = $fieldtype->getConfigInputfields($field);

// usage with all arguments
$inputfieldWrapper = $fieldtype->getConfigInputfields(Field $field);
~~~~~

## Hookable

- Hookable method name: `getConfigInputfields`
- Implementation: `___getConfigInputfields`
- Hook with: `$fieldtype->getConfigInputfields()`

## Arguments

- `$field` `Field`

## Return value

- `InputfieldWrapper`
