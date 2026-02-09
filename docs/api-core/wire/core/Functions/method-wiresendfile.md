# $functions->wireSendFile($filename, array $options = array(), array $headers = array())

Source: `wire/core/Functions.php`

Send the contents of the given filename via http

This function utilizes the `$config->fileContentTypes` to match file extension
to content type headers and force-download state.

This function throws a WireException if the file can’t be sent for some reason.

This is procedural version of the `$files->send()` method. See that method for all options.

## Usage

~~~~~
// basic usage
$result = $functions->wireSendFile($filename);

// usage with all arguments
$result = $functions->wireSendFile($filename, array $options = array(), array $headers = array());
~~~~~

## Arguments

- `$filename` `string` Full path and filename to send
- `$options` (optional) `array` Optional options that you may pass in (see `WireHttp::sendFile()` for details)
- `$headers` (optional) `array` Optional headers that are sent (see `WireHttp::sendFile()` for details)

## Exceptions

- `WireException`

## See Also

- [WireHttp::sendFile()](../WireHttp/method-___sendfile.md)
- [WireFileTools::send()](../WireFileTools/method-send.md)
