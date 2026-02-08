# PageVersionInfo: other

Source: `wire/modules/Pages/PagesVersions/PageVersionInfo.php`

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
