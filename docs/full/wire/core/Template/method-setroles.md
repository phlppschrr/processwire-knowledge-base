# $template->setRoles($value, $type = 'view')

Source: `wire/core/Template.php`

Set roles for this template

## Usage

~~~~~
// basic usage
$result = $template->setRoles($value);

// usage with all arguments
$result = $template->setRoles($value, $type = 'view');
~~~~~

## Arguments

- `$value` `array|PageArray` Role objects or array or Role IDs.
- `$type` (optional) `string` Specify one of the following: - `view` (default) - `edit` - `create` - `add` - Or a `Permission` object of `page-view` or `page-edit`
