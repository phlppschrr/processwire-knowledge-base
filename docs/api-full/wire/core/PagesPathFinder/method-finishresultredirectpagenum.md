# $pagesPathFinder->finishResultRedirectPageNum($response, &$result): int

Source: `wire/core/PagesPathFinder.php`

Update result for cases where a redirect was determined that involved pagination

Most of the logic here allows for the special case of admin URLs, which work with either
a custom pageNumUrlPrefix or the original/default one. This is a helper for the
finishResult() method.

## Usage

~~~~~
// basic usage
$int = $pagesPathFinder->finishResultRedirectPageNum($response, $result);

// usage with all arguments
$int = $pagesPathFinder->finishResultRedirectPageNum($response, &$result);
~~~~~

## Arguments

- `$response` `int`

## Return value

- `int`

## Since

3.0.198

## Details

- @var array $result
