# $pagesRequest->setRedirectPath($redirectPath, $type = 301)

Source: `wire/core/PagesRequest.php`

Set the redirect path

## Usage

~~~~~
// basic usage
$result = $pagesRequest->setRedirectPath($redirectPath);

// usage with all arguments
$result = $pagesRequest->setRedirectPath($redirectPath, $type = 301);
~~~~~

## Arguments

- `$redirectPath` `string`
- `$type` (optional) `int` 301 or 302
