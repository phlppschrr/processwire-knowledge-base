# Notice

Source: `wire/core/Notice.php`

ProcessWire Notice

Notice
Manages notifications in the ProcessWire admin, primarily for internal use.
Base class that holds a message, source class, and timestamp.
Contains individual notices/messages used by the application to display to the user.
Notice items come in three different classes: NoticeMessage, NoticeWarning and NoticeError.
They are all identical in terms of API, with the only difference being that they render as
informational messages, warnings, or errors.

ProcessWire 3.x, Copyright 2025 by Ryan Cramer
https://processwire.com

## other

@property string|object|array $text Text or value of notice

@property string $class Class of notice

@property int $timestamp Unix timestamp of when the notice was generated

@property int $flags Bitmask using any of the Notice::constants

@property-read $flagsArray Current flags as an array where indexes are int flags and values are flag names (since 3.0.149)

@property-read $flagsStr Current flags as string of flag names (since 3.0.149)

@property string $icon Name of icon to use with Notice

@property string $idStr Unique ID string for Notice

@property int $qty Number of times this Notice was added.

## prepend

Flag indicates notice should prepend (rather than append) to any existing notices

@since 3.0.135

## debug

Flag indicates the notice is for when debug mode is on only

## log

Flag indicates the notice will also be sent to the messages or errors log

## logOnly

Flag indicates the notice will be logged, but not shown

## allowMarkup

Flag indicates the notice is allowed to contain markup and won’t be automatically entity encoded

Note: entity encoding is done by the admin theme at output time, which should detect this flag.

## markup

Alias of allowMarkup flag

@since 3.0.208

## anonymous

Make notice anonymous (not tied to a particular class)

@since 3.0.135

## noGroup

Indicate notice should not group/collapse with others of the same type (when supported by admin theme)

@since 3.0.146

## separate

Alias of noGroup flag

@since 3.0.208

## login

Ignore notice unless it will be seen by a logged-in user

@since 3.0.149

## admin

Ignore notice unless user is somewhere in the admin (login page included)

@since 3.0.149

## superuser

Ignore notice unless current user is a superuser

@since 3.0.149

## allowMarkdown

Allow parsing of basic/inline markdown and bracket markup per $sanitizer->entitiesMarkdown()

@since 3.0.165

## markdown

Alias of allowMarkdown flag

@since 3.0.208

## allowDuplicate

Present duplicate notices separately rather than collapsing them to one

String name can be referred to as 'allowDuplicate' or just 'duplicate'

@since 3.0.208

## duplicate

Alias of allowDuplicate flag

@since 3.0.208

## __construct()

Create the Notice

As of version 3.0.149 the $flags argument can also be specified as a space separated
string or array of flag names. Previous versions only accepted flags integer.

@param string $text Notification text

@param int|string|array $flags Flags Flags for Notice

## set()

Set property

@param string $key

@param mixed $value

@return $this|WireData

## get()

Get property

@param string $key

@return mixed

## flags()

Get or set flags

@param string|int|array|null $value Accepts flags integer, or array of flag names, or space-separated string of flag names

@return int

@since 3.0.149

## flag()

Given flag name or int, return flag int

@param string|int $name

@return int

## flagNames()

Get string of names for given flags integer

@param null|int $flags Specify flags integer or omit to return all flag names (default=null)

@param bool $getString Get a space separated string rather than an array (default=false)

@return array|string

@since 3.0.149

## addFlag()

Add a flag

@param int|string $flag

@since 3.0.149

## removeFlag()

Remove a flag

@param int|string $flag

@since 3.0.149

## hasFlag()

Does this Notice have given flag?

@param int|string $flag

@return bool

@since 3.0.149

## getName()

Get the name for this type of Notice

This name is used for notice logs when Notice::log or Notice::logOnly flag is used.

@return string Name of log (basename)

## viewable()

Is this notice viewable at runtime?

@return bool

@since 3.0.254
