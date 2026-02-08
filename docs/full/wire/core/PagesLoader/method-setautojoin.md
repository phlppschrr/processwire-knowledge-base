# $pagesLoader->setAutojoin($autojoin = true)

Source: `wire/core/PagesLoader.php`

Enable or disable use of autojoin for all queries

Default should always be true, and you may use this to turn it off temporarily, but
you should remember to turn it back on

## Usage

~~~~~
// basic usage
$result = $pagesLoader->setAutojoin();

// usage with all arguments
$result = $pagesLoader->setAutojoin($autojoin = true);
~~~~~

## Arguments

- `$autojoin` (optional) `bool`
