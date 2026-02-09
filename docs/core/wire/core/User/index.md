# User

Source: `wire/core/User.php`

Inherits: `Page`


Groups:
Group: [access](group-access.md)
Group: [common](group-common.md)
Group: [languages](group-languages.md)
Group: [other](group-other.md)

ProcessWire UserPage

A type of Page used for storing an individual User


The $user API variable is a type of page representing the current user, and the User class is Page type used for all users.

@link http://processwire.com/api/variables/user/ Offical $user API variable Documentation



Additional notes regarding the $user->pass property:
Note that when getting, this returns a hashed version of the password, so it is not typically useful to get this property.
However, it is useful to set this property if you want to change the password. When you change a password, it is assumed
to be the non-hashed/non-encrypted version. ProcessWire will hash it automatically when the user is saved.

Methods:
Method: [__construct()](method-__construct.md)
Method: [hasRole()](method-hasrole.md)
Method: [addRole()](method-addrole.md)
Method: [removeRole()](method-removerole.md)
Method: [hasPermission()](method-haspermission.md)
Method: [hasPagePermission()](method-___haspagepermission.md) (hookable)
Method: [hasTemplatePermission()](method-___hastemplatepermission.md) (hookable)
Method: [getPermissions()](method-getpermissions.md)
Method: [isSuperuser()](method-issuperuser.md)
Method: [isGuest()](method-isguest.md)
Method: [isLoggedin()](method-isloggedin.md)
Method: [setLanguage()](method-setlanguage.md)
Method: [get()](method-get.md)
Method: [hasTfa()](method-hastfa.md)
