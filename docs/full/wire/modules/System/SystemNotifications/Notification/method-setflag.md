# $notification->setFlag($name, $add = true): self

Source: `wire/modules/System/SystemNotifications/Notification.php`

Set a named flag

## Usage

~~~~~
// basic usage
$result = $notification->setFlag($name);

// usage with all arguments
$result = $notification->setFlag($name, $add = true);
~~~~~

## Arguments

- `$name` `string|int` Flag to set
- `$add` (optional) `bool` True to add flag, false to remove

## Return value

- `self`
