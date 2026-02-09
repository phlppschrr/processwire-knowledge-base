# Process::getAfterLoginUrl(Page $page): bool|string

Source: `wire/core/Process.php`

URL to redirect to after non-authenticated user is logged-in, or false if module does not support

When supported, module should gather any input GET vars and URL segments that it recognizes,
sanitize them, and return a URL for that request. ProcessLogin will redirect to the returned URL
after user has successfully authenticated.

If module does not support this, or only needs to support an integer 'id' GET var, then this
method can return false.

## Usage

~~~~~
// basic usage
$bool = Process::getAfterLoginUrl($page);

// usage with all arguments
$bool = Process::getAfterLoginUrl(Page $page);
~~~~~

## Arguments

- `$page` `Page` Requested page

## Return value

- `bool|string`

## Details

- @sine 3.0.167
