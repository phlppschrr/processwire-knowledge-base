# $fieldtype->___getConfigAdvancedInputfields(Field $field): InputfieldWrapper

Source: `wire/core/Fieldtype.php`

Get Inputfields for advanced settings of the Field and Fieldtype

Inputfields returned from this appear under the "Advanced" tab rather than the "Details" tab,
in the Field editor.

In most cases, you will want to implement the getConfigInputfields() or getConfigArray() rather than this method.

NOTE: Inputfields with a name that starts with an underscore, i.e. "_myname" are assumed to be for runtime
use and are NOT stored in the database.

## Usage

~~~~~
// basic usage
$inputfieldWrapper = $fieldtype->___getConfigAdvancedInputfields($field);

// usage with all arguments
$inputfieldWrapper = $fieldtype->___getConfigAdvancedInputfields(Field $field);
~~~~~

## Arguments

- `$field` `Field`

## Return value

- `InputfieldWrapper`
