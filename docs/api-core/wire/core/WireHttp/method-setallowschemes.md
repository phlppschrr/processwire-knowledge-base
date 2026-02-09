# $wireHttp->setAllowSchemes($schemes, $replace = false): $this

Source: `wire/core/WireHttp.php`

Set schemes WireHttp is allowed to access (default=[http, https])

## Usage

~~~~~
// basic usage
$result = $wireHttp->setAllowSchemes($schemes);

// usage with all arguments
$result = $wireHttp->setAllowSchemes($schemes, $replace = false);
~~~~~

## Arguments

- `$schemes` `array|string` Array of schemes or space-separated string of schemes
- `$replace` (optional) `bool` Specify true to replace any existing schemes already allowed (default=false)

## Return value

- `$this`
