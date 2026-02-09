# $notification->setFlags($names, $add = true): self

Source: `wire/modules/System/SystemNotifications/Notification.php`

Set multiple flags

## Usage

~~~~~
// basic usage
$result = $notification->setFlags($names);

// usage with all arguments
$result = $notification->setFlags($names, $add = true);
~~~~~

## Arguments

- `$names` `string` space separated string of flag names
- `$add` (optional) `bool` True to add, false to remove

## Return value

- `self`
