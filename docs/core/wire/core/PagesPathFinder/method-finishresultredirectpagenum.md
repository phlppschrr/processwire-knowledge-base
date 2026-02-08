# $pagesPathFinder->finishResultRedirectPageNum($response, &$result): int

Source: `wire/core/PagesPathFinder.php`

Update result for cases where a redirect was determined that involved pagination

Most of the logic here allows for the special case of admin URLs, which work with either
a custom pageNumUrlPrefix or the original/default one. This is a helper for the
finishResult() method.

## Arguments

- int $response

## Return value

int

## Meta

- @var array $result
- @since 3.0.198
