# User

Source: `wire/core/User.php`

ProcessWire UserPage

A type of Page used for storing an individual User

ProcessWire 3.x, Copyright 2022 by Ryan Cramer
https://processwire.com

The $user API variable is a type of page representing the current user, and the User class is Page type used for all users.

@link http://processwire.com/api/variables/user/ Offical $user API variable Documentation



Additional notes regarding the $user->pass property:
Note that when getting, this returns a hashed version of the password, so it is not typically useful to get this property.
However, it is useful to set this property if you want to change the password. When you change a password, it is assumed
to be the non-hashed/non-encrypted version. ProcessWire will hash it automatically when the user is saved.

## common

@property PageArray $roles Get the roles this user has.

## languages

@property Language $language User language, applicable only if LanguageSupport installed.

## other

@property string $email Get or set email address for this user.

@property string|Password $pass Set the user’s password.

@property string $admin_theme Admin theme class name (when applicable).

## __construct()

Create a new User page in memory.

@param Template|null $tpl Template object this page should use.

## hasRole()

Does this user have the given Role?


~~~~~
if($user->hasRole('editor')) {
  // user has the editor role
}
~~~~~

@param string|Role|int $role May be Role name, object or ID.

@return bool

## addRole()

Add Role to this user

This is the same as `$user->roles->add($role)` except this one will also accept ID or name.

~~~~~
// Add the "editor" role to the $user
$user->addRole('editor');
$user->save();
~~~~~


@param string|int|Role $role May be Role name, object, or ID.

@return bool Returns false if role not recognized, true otherwise

## removeRole()

Remove Role from this user

This is the same as `$user->roles->remove($role)` except this one will accept ID or name.

~~~~~
// Remove the "editor" role from the $user
$user->removeRole('editor');
$user->save();
~~~~~


@param string|int|Role $role May be Role name, object or ID.

@return bool false if role not recognized, true otherwise

## hasPermission()

Does the user have the given permission?

- Optionally accepts a `Page` or `Template` context for the permission.
- This method accounts for the user's permissions across all their roles.

~~~~~
if($user->hasPermission('page-publish')) {
  // user has the page-publish permission in one of their roles
}
if($user->hasPermission('page-publish', $page)) {
  // user has page-publish permission for $page
}
~~~~~


@param string|Permission $name Permission name, object or id.

@param Page|Template|bool|string $context Page or Template...
 - or specify boolean true to return if user has permission OR if it was added at any template
 - or specify string "templates" to return array of Template objects where user has permission

@return bool|array

## ___hasPagePermission()

Does this user have named permission for the given Page?

This is a basic permission check and it is recommended that you use those from the PagePermissions module instead.
You use the PagePermissions module by calling the editable(), addable(), etc., functions on a page object.
The PagePermissions does use this function for some of it's checking.


@param string|Permission

@param Page|null $page Optional page to check against

@return bool

## ___hasTemplatePermission()

Does this user have the given permission on the given template?


@param string|Permission $name Permission name

@param Template|int|string $template Template object, name or ID

@return bool

@throws WireException

## getPermissions()

Get this user’s permissions, optionally within the context of a Page.

~~~~~
// Get all permissions the user has across their roles
$permissions = $user->getPermissions();

// Get all permissions the user has for $page
$permissions = $user->getPermissions($page);
~~~~~


@param Page|null $page Optional page to check against

@return PageArray of Permission objects

## isSuperuser()

Does this user have the superuser role?

Same as calling `$user->roles->has('name=superuser');` but potentially faster.


@return bool

## isGuest()

Is this the non-logged in guest user?


@return bool

## isLoggedin()

Is the current $user logged in and the same as this user?

When this method returns true, it means the current $user (API variable) is
this user and that they are logged in.


@return bool

## setLanguage()

Set language for user (quietly)

- Sets the language without tracking it as a change to the user.
- If language support is not installed this method silently does nothing.


@param Language|string|int $language Language object, name, or ID

@return self

@throws WireException if language support is installed and given an invalid/unknown language

@since 3.0.186

## get()

Get value

@param string $key

@return null|mixed

## hasTfa()

Does user have two-factor authentication (Tfa) enabled? (and what type?)

- Returns boolean false if not enabled.
- Returns string with Tfa module name (string) if enabled.
- When `$getInstance` argument is true, returns Tfa module instance rather than module name.

The benefit of using this method is that it can identify if Tfa is enabled without fully
initializing a Tfa module that would attach hooks, etc. So when you only need to know if
Tfa is enabled for a user, this method is more efficient than accessing `$user->tfa_type`.

When using `$getInstance` to return module instance, note that the module instance might not
be initialized (hooks not added, etc.). To retrieve an initialized instance, you can get it
from `$user->tfa_type` rather than calling this method.


@param bool $getInstance Get Tfa module instance when available? (default=false)

@return bool|string|Tfa

@since 3.0.162
