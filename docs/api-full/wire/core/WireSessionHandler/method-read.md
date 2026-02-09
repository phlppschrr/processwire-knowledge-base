# $wireSessionHandler->read($id): string|false

Source: `wire/core/WireSessionHandler.php`

Read and return data for session indicated by $id

## Usage

~~~~~
// basic usage
$string = $wireSessionHandler->read($id);
~~~~~

## Arguments

- `$id` `string` Session ID

## Return value

- `string|false` Serialized data string, blank string if none, or false on fail
