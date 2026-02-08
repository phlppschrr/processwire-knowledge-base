# ProcessWire::set()

Source: `wire/core/ProcessWire.php`

Set a new API variable

Alias of $this->wire(), but for setting only, for syntactic convenience.
i.e. $this->wire()->set($key, $value);

@param string $key API variable name to set

@param Wire|mixed $value Value of API variable

@param bool $lock Whether to lock the value from being overwritten

@return $this
