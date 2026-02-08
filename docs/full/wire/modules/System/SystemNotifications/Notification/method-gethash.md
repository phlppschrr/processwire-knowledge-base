# $notification->getHash(): string

Source: `wire/modules/System/SystemNotifications/Notification.php`

Return an string hash for comparing other notifications to see if they contain the same content

Hash specifically excludes consideration of dates (created, modified, expires)

## Return value

string
