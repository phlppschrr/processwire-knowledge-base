# $templates->rename(Template $template, $name)

Source: `wire/core/Templates.php`

Rename given template (and its fieldgroup, and file, when possible)

Given template must have its previous 'name' still present, and new name provided in $name
argument to this method.

## Arguments

- Template $template
- string $name New name to use

## Throws

- WireException if rename cannot be completed

## Meta

- @since 3.0.170
