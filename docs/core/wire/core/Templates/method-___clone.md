# $templates->___clone(Saveable $item, $name = ''): bool|Template

Source: `wire/core/Templates.php`

Clone the given Template

Note that this also clones the Fieldgroup if the template being cloned has its own named fieldgroup.

## Usage

~~~~~
// basic usage
$bool = $templates->___clone($item);

// usage with all arguments
$bool = $templates->___clone(Saveable $item, $name = '');
~~~~~

## Arguments

- `$item` `Template|Saveable` Template to clone
- `$name` (optional) `string` Name of new template that will be created, or omit to auto-assign.

## Return value

- `bool|Template` $item Returns the new Template on success, or false on failure

## Details

- @todo: clone the fieldgroup context settings too.
