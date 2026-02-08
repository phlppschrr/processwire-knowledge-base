# Templates::rename()

Source: `wire/core/Templates.php`

Rename given template (and its fieldgroup, and file, when possible)

Given template must have its previous 'name' still present, and new name provided in $name
argument to this method.

@param Template $template

@param string $name New name to use

@since 3.0.170

@throws WireException if rename cannot be completed
