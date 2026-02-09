# $processController->getProcessMethodName(Process $process): string

Source: `wire/core/ProcessController.php`

Get the name of the method to execute with the Process

## Usage

~~~~~
// basic usage
$string = $processController->getProcessMethodName($process);

// usage with all arguments
$string = $processController->getProcessMethodName(Process $process);
~~~~~

## Arguments

- Process @process

## Return value

- `string`

## Exceptions

- `ProcessControllerPermissionException`
