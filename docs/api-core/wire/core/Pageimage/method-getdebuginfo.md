# $pageimage->getDebugInfo($options = array(), $returnType = 'string'): array|object|string

Source: `wire/core/Pageimage.php`

Verbose debug info (via @horst)

Optionally with individual options array.

## Usage

~~~~~
// basic usage
$array = $pageimage->getDebugInfo();

// usage with all arguments
$array = $pageimage->getDebugInfo($options = array(), $returnType = 'string');
~~~~~

## Arguments

- `$options` (optional) `array` The individual options you also passes with your image variation creation
- `$returnType` (optional) `string` 'string'|'array'|'object', default is 'string' and returns markup or plain text

## Return value

- `array|object|string`

## Since

3.0.132
