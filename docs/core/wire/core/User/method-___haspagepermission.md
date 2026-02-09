# $user->hasPagePermission($name, ?Page $page = null): bool

Source: `wire/core/User.php`

Does this user have named permission for the given Page?

This is a basic permission check and it is recommended that you use those from the PagePermissions module instead.
You use the PagePermissions module by calling the editable(), addable(), etc., functions on a page object.
The PagePermissions does use this function for some of it's checking.

## Usage

~~~~~
// basic usage
$bool = $user->hasPagePermission($name);

// usage with all arguments
$bool = $user->hasPagePermission($name, ?Page $page = null);
~~~~~

## Hookable

- Hookable method name: `hasPagePermission`
- Implementation: `___hasPagePermission`
- Hook with: `$user->hasPagePermission()`

## Hooking Before

~~~~~
$this->addHookBefore('User::hasPagePermission', function(HookEvent $event) {
  $user = $event->object;

  // Get arguments
  $name = $event->arguments(0);
  $page = $event->arguments(1);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $name);
  $event->arguments(1, $page);
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('User::hasPagePermission', function(HookEvent $event) {
  $user = $event->object;

  // Get arguments
  $name = $event->arguments(0);
  $page = $event->arguments(1);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Arguments

- string|Permission
- `$page` (optional) `Page|null` Optional page to check against

## Return value

- `bool`
