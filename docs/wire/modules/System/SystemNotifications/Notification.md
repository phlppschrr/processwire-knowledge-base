# Notification

Source: `wire/modules/System/SystemNotifications/Notification.php`

An individual notification item to be part of a NotificationArray for a Page

@class Notification


data encoded vars, all optional
===============================

@property int $id  unique ID (among others the user may have)

@property string $text  extended text

@property string $html  extended text as HTML markup

@property string $from  "from" text where applicable, like a class name

@property string $icon  fa-icon when applicable

@property string $href  clicking notification goes to this URL

@property int $progress  progress percent 0-100

@property int $expires  datetime after which will automatically be deleted

## other

@property int $pages_id  page ID notification is for (likely a User page)

@property int $sort  sort value, as required by Fieldtype

@property int $src_id  page ID when notification was generated

@property string $title  title/headline

@property int $flags  flags: see flag constants

@property int $created  datetime created (unix timestamp)

@property int $modified  datetime created (unix timestamp)

@property int $qty  quantity of times this notification has been repeated

@property array $flagNames Notification flag names

## flagDebug

Flag constants for Notification objects

Note that flags 2-32 line up with the same flags from Notice objects

## __construct()

Construct a new Notification

## is()

Does this Notification match the given flag name(s)?

@param string $name

@return bool

## flagNameToFlag()

Given a flag name, return the corresponding flag value

@param string $name

@return int mixed

@throws WireException if given unknown flag

## flagNamesToFlags()

Given multiple space separated flag names, return array of flag values

@param string $names space separted, will also accept CSV

@return array of flag name => flag value

## setFlag()

Set a named flag

@param string|int $name Flag to set

@param bool $add True to add flag, false to remove

@return self

## addFlag()

Add the given flag name(s) (shortcut for setFlag)

@param string $name One or more space-separated flag names

@return self

## removeFlag()

Remove the given flag name(s) (shortcut for setFlag)

@param string $name One or more space-separated flag names

@return self

## setFlags()

Set multiple flags

@param string $names space separated string of flag names

@param bool $add True to add, false to remove

@return self

## set()

Set a value to the Notification

Note: setting the 'expires' value accepts either a future date, or a quantity of seconds
in the future relative to now.

@param string $key

@param mixed $value

@return self|Notification|WireData

## getID()

Return an ID string/hash unique to this Notification within the page that its on

The text/html, modified date, expires date, and icon may change without affecting the id.

@return mixed|null|string

## getHash()

Return an string hash for comparing other notifications to see if they contain the same content

Hash specifically excludes consideration of dates (created, modified, expires)

@return string

## get()

Retrieve a value from the Notification

@param string $key

@return mixed

## isExpired()

Is this Notification expired?

@return bool

## __toString()

String value of a Notification

@return string
