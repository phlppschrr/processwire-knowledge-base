# $field->getInputfield(Page $page, $contextStr = ''): Inputfield|null

Source: `wire/core/Field.php`

Get the Inputfield module used to collect input for this field.

## Usage

~~~~~
// basic usage
$inputfield = $field->getInputfield($page);

// usage with all arguments
$inputfield = $field->getInputfield(Page $page, $contextStr = '');
~~~~~

## Hookable

- Hookable method name: `getInputfield`
- Implementation: `___getInputfield`
- Hook with: `$field->getInputfield()`

## Arguments

- `$page` `Page` Page that the Inputfield is for.
- `$contextStr` (optional) `string` Optional context string to append to the Inputfield's name/id (for repeaters and such).

## Return value

- `Inputfield|null`
