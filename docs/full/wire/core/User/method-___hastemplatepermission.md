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

## Hooking Before

~~~~~
$this->addHookBefore('User::hasTemplatePermission', function(HookEvent $event) {
  $user = $event->object;

  // Get arguments
  $name = $event->arguments(0);
  $template = $event->arguments(1);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $name);
  $event->arguments(1, $template);
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('User::hasTemplatePermission', function(HookEvent $event) {
  $user = $event->object;

  // Get arguments
  $name = $event->arguments(0);
  $template = $event->arguments(1);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Arguments

- `$name` `string|Permission` Permission name
- `$template` `Template|int|string` Template object, name or ID

## Return value

- `bool`

## Exceptions

- `WireException`
