# Wire::___trackException()

Source: `wire/core/Wire.php`

Hookable method called when an Exception (or Error) occurs

- It will log Exception to `exceptions.txt` log if 'exceptions' is in `$config->logs`.
- It will log Error to `errors.txt` log if 'errors' is in `$config->logs`.
- It will re-throw Exception or Error if `$config->allowExceptions` is true.
- If additional `$text` is provided, it will be sent to notice method call.

Please note that if your root /index.php version is less than 302 it will only receive
Exception (and not Error) objects.


@param \Throwable $e Exception or Error object that was thrown.

@param bool|int $severe Whether or not it should be considered severe (default=true).

@param string|array|object|true $text Additional details (optional):
	- When provided, it will be sent to `$this->error($text)` if $severe is true, or `$this->warning($text)` if $severe is false.
	- Specify boolean `true` to just send the `$e->getMessage()` to `$this->error()` or `$this->warning()`.

@return $this

@throws \Exception|\Error If `$severe==true` and `$config->allowExceptions==true`
