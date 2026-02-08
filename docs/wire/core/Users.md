# Users

Source: `wire/core/Users.php`

The Users class serves as the $users API variable.

Manages all users (User objects) in ProcessWire.

## other

@method PageArray find($selector) Return the User(s) matching the the given selector query.

@method User add($name) Add new User with the given name and return it.

@method bool save($user) Save given User.

@method bool delete($user) Delete the given User.

@method array saveReady($user) Hook called just before a User is saved

@method void saved($user, array $changes) Hook called after a User has been saved

@method void added($user) Hook called just after a User is added

@method void deleteReady($user) Hook called before a User is deleted

@method void deleted($user) Hook called after a User is deleted

@method User new($options = []) Create new User instance in memory (3.0.249+)

## __construct()

Construct

@param ProcessWire $wire

@param array $templates

@param array $parents

## get()

Get the user by name, ID or selector string

@param string $selectorString

@return User|NullPage|null

## setCurrentUser()

Set the current system user (the $user API variable)

@param User $user

## loaded()

Ensure that every user loaded has at least the 'guest' role

@param Page $page

## checkGuestRole()

Check that given user has guest role and add it if not

@param User $user

@since 3.0.198

## getCurrentUser()

Returns the current user object

@return User

## getGuestUser()

Get the 'guest' user account

@return User

## setAdminThemeByRole()

Set admin theme for all users having role

@param AdminTheme|string $adminTheme Admin theme instance or class/module name

@param Role $role

@return int Number of users set for admin theme

@throws WireException

@since 3.0.176

## ___save()

Save a User

- This is the same as calling $user->save()
- If the user is new, it will be inserted. If existing, it will be updated.
- If you want to just save a particular field for the user, use `$user->save($fieldName)` instead.

**Hook note:**
If you want to hook this method, please hook the `Users::saveReady`, `Users::saved`, or any one of
the `Pages::save*` hook methods instead, as this method will not capture users saved directly
through `$pages->save($user)`.
~~~~~
// Example of hooking $pages->save() on User objects only
$wire->addHookBefore('Pages::save(<User>)', function(HookEvent $e) {
  $user = $event->arguments(0);
});
~~~~~

@param Page $page

@return bool True on success

@throws WireException

## ___saveReady()

Hook called just before a user is saved


@param Page $page The user about to be saved

@return array Optional extra data to add to pages save query.
