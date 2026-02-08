# $pagefile->setDescription($value, ?Page $language = null): $this

Source: `wire/core/Pagefile.php`

Set a description, optionally parsing JSON language-specific descriptions to separate properties

## Usage

~~~~~
// basic usage
$result = $pagefile->setDescription($value);

// usage with all arguments
$result = $pagefile->setDescription($value, ?Page $language = null);
~~~~~

## Arguments

- `$value` `string|array`
- Language|null Langage to set it for. Omit to determine automatically.

## Return value

- `$this`
