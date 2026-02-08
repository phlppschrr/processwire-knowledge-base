# $users->loaded(Page $page)

Source: `wire/core/Users.php`

Ensure that every user loaded has at least the 'guest' role

## Usage

~~~~~
// basic usage
$result = $users->loaded($page);

// usage with all arguments
$result = $users->loaded(Page $page);
~~~~~

## Arguments

- `$page` `Page`
