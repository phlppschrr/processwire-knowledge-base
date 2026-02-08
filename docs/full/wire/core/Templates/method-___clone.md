# Templates::___clone()

Source: `wire/core/Templates.php`

Clone the given Template

Note that this also clones the Fieldgroup if the template being cloned has its own named fieldgroup.

@todo: clone the fieldgroup context settings too.

@param Template|Saveable $item Template to clone

@param string $name Name of new template that will be created, or omit to auto-assign.

@return bool|Template $item Returns the new Template on success, or false on failure
