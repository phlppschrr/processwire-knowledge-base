# $page->getUser($userType): User|NullPage

Source: `wire/core/Page.php`

Get page’s created or modified user

## Usage

~~~~~
// basic usage
$user = $page->getUser($userType);
~~~~~

## Arguments

- `$userType` `string` One of 'created' or 'modified'

## Return value

- `User|NullPage`
