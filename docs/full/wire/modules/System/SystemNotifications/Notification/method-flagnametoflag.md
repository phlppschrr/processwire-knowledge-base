# $notification->flagNameToFlag($name): int

Source: `wire/modules/System/SystemNotifications/Notification.php`

Given a flag name, return the corresponding flag value

## Usage

~~~~~
// basic usage
$int = $notification->flagNameToFlag($name);
~~~~~

## Arguments

- `$name` `string`

## Return value

- `int` mixed

## Exceptions

- `WireException` if given unknown flag
