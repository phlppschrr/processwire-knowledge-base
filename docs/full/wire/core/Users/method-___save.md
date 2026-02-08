# $users->save(Page $page): bool

Source: `wire/core/Users.php`

Save a User

- This is the same as calling $user->save()
- If the user is new, it will be inserted. If existing, it will be updated.
- If you want to just save a particular field for the user, use `$user->save($fieldName)` instead.

**Hook note:**
If you want to hook this method, please hook the `Users::saveReady`, `Users::saved`, or any one of
the `Pages::save*` hook methods instead, as this method will not capture users saved directly
through `$pages->save($user)`.

## Example

~~~~~
// Example of hooking $pages->save() on User objects only
$wire->addHookBefore('Pages::save(<User>)', function(HookEvent $e) {
  $user = $event->arguments(0);
});
~~~~~

## Usage

~~~~~
// basic usage
$bool = $users->save($page);

// usage with all arguments
$bool = $users->save(Page $page);
~~~~~

## Hookable

- Hookable method name: `save`
- Implementation: `___save`
- Hook with: `$users->save()`

## Arguments

- `$page` `Page`

## Return value

- `bool` True on success

## Exceptions

- `WireException`
