# $notificationArray->warning($text, $flags = 0): Notification

Source: `wire/modules/System/SystemNotifications/NotificationArray.php`

Record a warning notification

## Usage

~~~~~
// basic usage
$notification = $notificationArray->warning($text);

// usage with all arguments
$notification = $notificationArray->warning($text, $flags = 0);
~~~~~

## Arguments

- `$text` `string`
- `$flags` (optional) `int|bool` See Notification flags

## Return value

- `Notification`
