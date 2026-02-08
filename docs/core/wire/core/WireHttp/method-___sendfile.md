# WireHttp::___sendFile()

Source: `wire/core/WireHttp.php`

Send the contents of the given filename to the current http connection.

This function utilizes the `$config->fileContentTypes` to match file extension
to content type headers and force-download state.

This function throws a `WireException` if the file can't be sent for some reason.


@param string|bool $filename Filename to send (or boolean false if sending $options[data] rather than file)

@param array $options Options that you may pass in:
  - `exit` (bool): Halt program execution after file send (default=true).
  - `partial` (bool): Allow use of partial downloads via HTTP_RANGE requests? Since 3.0.131 (default=true)
  - `forceDownload` (bool|null): Whether file should force download (default=null, i.e. let content-type header decide).
  - `downloadFilename` (string): Filename you want the download to show on user's computer, or omit to use existing.
  - `headers` (array): The $headers argument to this method can also be provided as an option right here, since 3.0.131 (default=[])
  - `data` (string): String of data to send rather than contents of file, applicable only if $filename argument is false, Since 3.0.132.

@param array $headers Headers that are sent. These are the defaults:
  - `pragma`: public
  - `expires`: 0
  - `cache-control`: must-revalidate, post-check=0, pre-check=0
  - `content-type`: {content-type} (replaced with actual content type)
  - `content-transfer-encoding`: binary
  - `content-length`: {filesize} (replaced with actual filesize)
  - To remove a header completely, make its value NULL and it won't be sent.

@return int Returns value only if `exit` option is false (value is quantity of bytes sent)

@throws WireException
