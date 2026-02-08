# $template->save(): Template|bool

Source: `wire/core/Template.php`

Save the template to database

This is the same as calling `$templates->save($template)`.

## Usage

~~~~~
// basic usage
$template = $template->save();
~~~~~

## Return value

- `Template|bool` Returns Template if successful, or false if not
