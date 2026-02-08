# $templates->___clone(Saveable $item, $name = ''): bool|Template

Source: `wire/core/Templates.php`

Clone the given Template

Note that this also clones the Fieldgroup if the template being cloned has its own named fieldgroup.

## Arguments

- Template|Saveable $item Template to clone
- string $name Name of new template that will be created, or omit to auto-assign.

## Return value

bool|Template $item Returns the new Template on success, or false on failure

## Meta

- @todo: clone the fieldgroup context settings too.
