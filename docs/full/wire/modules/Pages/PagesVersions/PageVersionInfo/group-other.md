# PageVersionInfo: other

Source: `wire/modules/Pages/PagesVersions/PageVersionInfo.php`

- $version: int Version number

- $description: string Version description (not entity encoded)

- $descriptionHtml: string Version description entity encoded for output in HTML

- $created: int Date/time created (unix timestamp)

- $createdStr: string Date/time created (YYYY-MM-DD HH:MM:SS)

- $modified: int Date/time last modified (unix timestamp)

- $modifiedStr: string Date/time last modified (YYYY-MM-DD HH:MM:SS)

- $pages_id: int ID of page this version is for

- $page: Page Page this version is for

- $created_users_id: int ID of user that created this version

- $createdUser: User|NullPage User that created this version

- $modified_users_id: int ID of user that last modified this version

- $modifiedUser: User|NullPage User that last modified this version

- $properties: array Native page properties array in format [ property => value ]

- $fieldNames: array Names of fields in this version

- $action: string Populated with action name if info is being used for an action
