# $processWire->set($key, $value, $lock = false): $this

Source: `wire/core/ProcessWire.php`

Set a new API variable

Alias of $this->wire(), but for setting only, for syntactic convenience.
i.e. $this->wire()->set($key, $value);

## Usage

~~~~~
// basic usage
$result = $processWire->set($key, $value);

// usage with all arguments
$result = $processWire->set($key, $value, $lock = false);
~~~~~

## Arguments

- `$key` `string` API variable name to set
- `$value` `Wire|mixed` Value of API variable
- `$lock` (optional) `bool` Whether to lock the value from being overwritten

## Return value

- `$this`
