# $user->___hasTemplatePermission($name, $template): bool

Source: `wire/core/User.php`

Does this user have the given permission on the given template?

## Usage

~~~~~
// basic usage
$bool = $user->___hasTemplatePermission($name, $template);
~~~~~

## Arguments

- `$name` `string|Permission` Permission name
- `$template` `Template|int|string` Template object, name or ID

## Return value

- `bool`

## Exceptions

- `WireException`
