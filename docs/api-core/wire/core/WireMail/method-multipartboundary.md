# $wireMail->multipartBoundary($prefix = ''): string

Source: `wire/core/WireMail.php`

Get the multipart boundary string for this email

## Usage

~~~~~
// basic usage
$string = $wireMail->multipartBoundary();

// usage with all arguments
$string = $wireMail->multipartBoundary($prefix = '');
~~~~~

## Arguments

- `$prefix` (optional) `string|bool` Specify optional boundary prefix or boolean true to clear any existing stored boundary

## Return value

- `string`
