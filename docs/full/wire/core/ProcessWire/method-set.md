# $processWire->set($key, $value, $lock = false): $this

Source: `wire/core/ProcessWire.php`

Set a new API variable

Alias of $this->wire(), but for setting only, for syntactic convenience.
i.e. $this->wire()->set($key, $value);

## Arguments

- string $key API variable name to set
- Wire|mixed $value Value of API variable
- bool $lock Whether to lock the value from being overwritten

## Return value

$this
