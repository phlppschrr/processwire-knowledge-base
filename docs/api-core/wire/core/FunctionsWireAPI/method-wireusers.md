# $functionsWireAPI->wireUsers($selector = ''): Users|PageArray|User|NullPage|mixed

Source: `wire/core/FunctionsWireAPI.php`

Access the $users API variable as a function

See the pages() function for full usage details.

## Usage

~~~~~
// basic usage
$users = $functionsWireAPI->wireUsers();

// usage with all arguments
$users = $functionsWireAPI->wireUsers($selector = '');
~~~~~

## Arguments

- `$selector` (optional) `string|array` Optional selector to send to find() or get()

## Return value

- `Users|PageArray|User|NullPage|mixed`

## See Also

- pages()
