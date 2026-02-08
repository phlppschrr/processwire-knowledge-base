# $user->hasTemplatePermission($name, $template): bool

Source: `wire/core/User.php`

Does this user have the given permission on the given template?

## Usage

~~~~~
// basic usage
$bool = $user->hasTemplatePermission($name, $template);
~~~~~

## Hookable

- Hookable method name: `hasTemplatePermission`
- Implementation: `___hasTemplatePermission`
- Hook with: `$user->hasTemplatePermission()`

## Arguments

- `$name` `string|Permission` Permission name
- `$template` `Template|int|string` Template object, name or ID

## Return value

- `bool`

## Exceptions

- `WireException`
