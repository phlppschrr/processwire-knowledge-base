# $admin->_checkForTwoFactorAuth(Session $session)

Source: `wire/core/admin.php`

Check if two factor authentication is being required and display warning with link to configure

## Usage

~~~~~
// basic usage
$result = $admin->_checkForTwoFactorAuth($session);

// usage with all arguments
$result = $admin->_checkForTwoFactorAuth(Session $session);
~~~~~

## Arguments

- `$session` `Session`
