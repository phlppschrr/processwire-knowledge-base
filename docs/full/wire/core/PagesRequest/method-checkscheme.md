# $pagesRequest->checkScheme(Page $page)

Source: `wire/core/PagesRequest.php`

If the template requires a different scheme/protocol than what is here, then redirect to it.

This method just silently sets the $this->redirectUrl var if a redirect is needed.
Note this does not work if GET vars are present in the URL -- they will be lost in the redirect.

## Usage

~~~~~
// basic usage
$result = $pagesRequest->checkScheme($page);

// usage with all arguments
$result = $pagesRequest->checkScheme(Page $page);
~~~~~

## Arguments

- `$page` `Page`
