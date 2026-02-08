# NotificationArray

Source: `wire/modules/System/SystemNotifications/NotificationArray.php`

Contains multiple Event objects for a single page

@class NotificationArray

## __construct()

Create a new NotificationArray

@param Page|User $page User (or page) that these notifications are for

## isValidItem()

Template method from WireArray

@param Notification $item

@return bool

## add()

Add a Notification instance to this NotificationArray

@param Notification $item

@return self|NotificationArray|WireArray

## get()

Retrieve a Notification by index or by id

@param int|string $key

@return Notification|null

## getBy()

Get a notification that contains the given value for $property

@param string $property

@param mixed $value

@return null|Notification

## save()

Save any changes or additions that were made to these Notifications

@return bool

## __toString()

Get string value of this NotificationArray

@return string

## getNew()

Get a new Notification

@param string $flag Specify any flag, flag name or space-separated combination of flag names

@param bool $addNow Add it to this NotificationArray now?

@return Notification

## message()

***********************************************************************************
The following methods are based on those in the base Wire class, but they override
them to replace Notices functionality with Notifications

## message()

Record an informational or 'success' message

@param string $text

@param int|bool $flags See Notification flags

@return Notification

## warning()

Record a warning notification

@param string $text

@param int|bool $flags See Notification flags

@return Notification

## error()

Record an error notification

@param string $text

@param int|bool $flags See Notification flags

@return Notification

## errors()

Return all error Notifications

@param string|array $options One or more of array elements or space separated string of:
	first: only first item will be returned (string)
	last: only last item will be returned (string)
	clear: clear out all items that are returned from this method (includes both local and global)

@return Notices|string Array of NoticeError error messages or string if last, first or str option was specified.

## warnings()

Return warnings recorded by this object

@param string|array $options One or more of array elements or space separated string of:
	first: only first item will be returned (string)
	last: only last item will be returned (string)
	clear: clear out all items that are returned from this method (includes both local and global)

@return Notices|string Array of NoticeError error messages or string if last, first or str option was specified.

## messages()

Return messages recorded by this object

@param string|array $options One or more of array elements or space separated string of:
	first: only first item will be returned (string)
	last: only last item will be returned (string)
	clear: clear out all items that are returned from this method (includes both local and global)
	errors: returns errors rather than messages.
	warnings: returns warnings rather than messages.

@return Notices|string Array of NoticeError error messages or string if last, first or str option was specified.
