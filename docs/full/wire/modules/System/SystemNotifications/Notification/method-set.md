# Notification::set()

Source: `wire/modules/System/SystemNotifications/Notification.php`

Set a value to the Notification

Note: setting the 'expires' value accepts either a future date, or a quantity of seconds
in the future relative to now.

@param string $key

@param mixed $value

@return self|Notification|WireData
