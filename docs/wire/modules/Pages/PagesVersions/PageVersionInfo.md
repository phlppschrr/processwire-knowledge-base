# PageVersionInfo

Source: `wire/modules/Pages/PagesVersions/PageVersionInfo.php`

Page Version Info

For pages that are a version, this class represents the `_version`
property of the page. It is also used as the return value for some
methods in the PagesVersions class to return version information.


ProcessWire 3.x, Copyright 2023 by Ryan Cramer
https://processwire.com

## other

@property int $version Version number

@property string $description Version description (not entity encoded)

@property-read string $descriptionHtml Version description entity encoded for output in HTML

@property int $created Date/time created (unix timestamp)

@property-read string $createdStr Date/time created (YYYY-MM-DD HH:MM:SS)

@property int $modified Date/time last modified (unix timestamp)

@property-read string $modifiedStr Date/time last modified (YYYY-MM-DD HH:MM:SS)

@property int $pages_id ID of page this version is for

@property Page $page Page this version is for

@property int $created_users_id ID of user that created this version

@property-read User|NullPage $createdUser User that created this version

@property int $modified_users_id ID of user that last modified this version

@property-read User|NullPage $modifiedUser User that last modified this version

@property array $properties Native page properties array in format [ property => value ]

@property-read array $fieldNames Names of fields in this version

@property string $action Populated with action name if info is being used for an action

## actionRestore

Value for $action property when restoring a page

## __construct()

@param array $data

## set()

Set property

@param string $key

@param string|int|Page $value

@return self

## get()

Get property

@param string $key

@return mixed|NullPage|Page|User|null

## getPage()

Get page that this version is for

@return NullPage|Page

## setPage()

Set page that this version is for

@param Page $page

## getCreatedUser()

Get user that created this version

@return NullPage|User

## getModifiedUser()

Get user that last modified this version

@return NullPage|User

## __toString()

String value is version number as a string

@return string
