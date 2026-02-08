# $user->__construct(?Template $tpl = null)

Source: `wire/core/User.php`

Create a new User page in memory.

## Usage

~~~~~
// basic usage
$result = $user->__construct();

// usage with all arguments
$result = $user->__construct(?Template $tpl = null);
~~~~~

## Arguments

- `$tpl` (optional) `Template|null` Template object this page should use.
