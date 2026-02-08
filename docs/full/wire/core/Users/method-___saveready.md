# $users->___saveReady(Page $page): array

Source: `wire/core/Users.php`

Hook called just before a user is saved

## Usage

~~~~~
// basic usage
$array = $users->___saveReady($page);

// usage with all arguments
$array = $users->___saveReady(Page $page);
~~~~~

## Arguments

- `$page` `Page` The user about to be saved

## Return value

- `array` Optional extra data to add to pages save query.
