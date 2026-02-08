# $markupQA->debug($set = null): bool

Source: `wire/core/MarkupQA.php`

Get or set debug status

Applies only if current user is a superuser

## Usage

~~~~~
// basic usage
$bool = $markupQA->debug();

// usage with all arguments
$bool = $markupQA->debug($set = null);
~~~~~

## Arguments

- `$set` (optional) `bool|null` Omit this argument to get or specify bool to set

## Return value

- `bool`
