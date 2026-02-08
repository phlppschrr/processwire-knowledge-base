# NotificationArray::errors()

Source: `wire/modules/System/SystemNotifications/NotificationArray.php`

Return all error Notifications

@param string|array $options One or more of array elements or space separated string of:
	first: only first item will be returned (string)
	last: only last item will be returned (string)
	clear: clear out all items that are returned from this method (includes both local and global)

@return Notices|string Array of NoticeError error messages or string if last, first or str option was specified.
