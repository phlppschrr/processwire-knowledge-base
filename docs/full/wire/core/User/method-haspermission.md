# User::hasPermission()

Source: `wire/core/User.php`

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
