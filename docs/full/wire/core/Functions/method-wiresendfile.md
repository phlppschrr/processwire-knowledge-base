# $functions->wireSendFile($filename, array $options = array(), array $headers = array())

Source: `wire/core/Functions.php`

Send the contents of the given filename via http

This function utilizes the `$config->fileContentTypes` to match file extension
to content type headers and force-download state.

This function throws a WireException if the file can’t be sent for some reason.

This is procedural version of the `$files->send()` method. See that method for all options.

## Arguments

- string $filename Full path and filename to send
- array $options Optional options that you may pass in (see `WireHttp::sendFile()` for details)
- array $headers Optional headers that are sent (see `WireHttp::sendFile()` for details)

## Throws

- WireException

## See also

- [WireHttp::sendFile()](../WireHttp/method-___sendfile.md)
- [WireFileTools::send()](../WireFileTools/method-send.md)
