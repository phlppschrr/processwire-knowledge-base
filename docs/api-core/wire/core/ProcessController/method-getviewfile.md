# $processController->getViewFile(Process $process, $method = ''): string

Source: `wire/core/ProcessController.php`

Given a process and method name, return the first matching valid view file for it

## Usage

~~~~~
// basic usage
$string = $processController->getViewFile($process);

// usage with all arguments
$string = $processController->getViewFile(Process $process, $method = '');
~~~~~

## Arguments

- `$process` `Process`
- `$method` (optional) `string` If omitted, 'execute' is assumed

## Return value

- `string`
