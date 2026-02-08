# $fileLog->save($str, array $options = array()): bool

Source: `wire/core/FileLog.php`

Save the given log entry string

## Usage

~~~~~
// basic usage
$bool = $fileLog->save($str);

// usage with all arguments
$bool = $fileLog->save($str, array $options = array());
~~~~~

## Arguments

- `$str` `string`
- `$options` (optional) `array` options to modify behavior (Added 3.0.143) - `allowDups` (bool): Allow duplicating same log entry in same runtime/request? (default=true) - `mergeDups` (int): Merge previous duplicate entries that also appear near end of file? To enable, specify int for quantity of bytes to consider from EOF, value of 1024 or higher (default=0, disabled) - `maxTries` (int): If log entry fails to save, maximum times to re-try (default=20) - `maxTriesDelay` (int): Micro seconds (millionths of a second) to delay between re-tries (default=2000)

## Return value

- `bool` Success state: true if log written, false if not.
