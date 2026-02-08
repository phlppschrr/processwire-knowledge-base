# Functions::wireSendFile()

Source: `wire/core/Functions.php`

Send the contents of the given filename via http

This function utilizes the `$config->fileContentTypes` to match file extension
to content type headers and force-download state.

This function throws a WireException if the file can’t be sent for some reason.

This is procedural version of the `$files->send()` method. See that method for all options.


@param string $filename Full path and filename to send

@param array $options Optional options that you may pass in (see `WireHttp::sendFile()` for details)

@param array $headers Optional headers that are sent (see `WireHttp::sendFile()` for details)

@throws WireException

@see WireHttp::sendFile(), WireFileTools::send()
