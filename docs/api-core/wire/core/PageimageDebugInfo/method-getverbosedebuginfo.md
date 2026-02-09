# $pageimageDebugInfo->getVerboseDebugInfo($options = array(), $returnType = 'string'): array|object|string

Source: `wire/core/PageimageDebugInfo.php`

Get verbose DebugInfo, optionally with individual options array, @horst

(without invoking the magic debug)

## Usage

~~~~~
// basic usage
$array = $pageimageDebugInfo->getVerboseDebugInfo();

// usage with all arguments
$array = $pageimageDebugInfo->getVerboseDebugInfo($options = array(), $returnType = 'string');
~~~~~

## Arguments

- `$options` (optional) `array` The individual options you also passes with your image variation creation
- `$returnType` (optional) `string` 'string'|'array'|'object', default is 'string' and returns markup or plain text

## Return value

- `array|object|string`
