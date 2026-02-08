# $wireFileTools->send($filename, array $options = array(), array $headers = array()): int

Source: `wire/core/WireFileTools.php`

Send the contents of the given filename to the current http connection

This function utilizes the `$config->fileContentTypes` to match file extension to content type headers
and force-download state.

This function throws a `WireException` if the file can’t be sent for some reason. Set the `throw` option to
false if you want it to instead return integer 0 when errors occur.

## Arguments

- string|bool $filename Full path and filename to send or boolean false if provided in `$options[data]`.
- array $options Optional options to modify default behavior: - `exit` (bool): Halt program execution after file send (default=true). - `partial` (bool): Allow use of partial downloads via HTTP_RANGE requests? Since 3.0.131 (default=true) - `forceDownload` (bool|null): Whether file should force download, or null to let content-type header decide (default=null). - `downloadFilename` (string): Filename you want the download to show on user’s computer, or omit to use existing (default=''). - `headers` (array): The $headers argument to this method can also be provided as an option right here (default=[]). Since 3.0.131. - `data` (string): String of data to send rather than file, $filename argument must be false (default=''). Since 3.0.132. - `limitPath` (string|bool): Prefix disk path $filename must be within, false to disable, true for site/assets (default=false). Since 3.0.169. - `throw` (bool): Throw exceptions on error? When false, it will instead return integer 0 on errors (default=true). Since 3.0.169.
- array $headers Optional headers that are sent, below are the defaults: - `pragma`: public - `expires`: 0 - `cache-control`: must-revalidate, post-check=0, pre-check=0 - `content-type`: {content-type} (replaced with actual content type) - `content-transfer-encoding`: binary - `content-length`: {filesize} (replaced with actual filesize) - To remove a header completely, make its value NULL. - If preferred, the above headers can be specified in `$options[headers]` instead.

## Return value

int Returns bytes sent, only if `exit` option is false (since 3.0.169)

## Throws

- WireException

## See also

- [WireHttp::sendFile()](../WireHttp/method-___sendfile.md)
