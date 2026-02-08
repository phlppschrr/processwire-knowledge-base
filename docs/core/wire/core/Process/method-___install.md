# $process->___install()

Source: `wire/core/Process.php`

Per the Module interface, Install the module

By default a permission equal to the name of the class is installed, unless overridden with
the 'permission' property in your module information array.

See the `Module` interface and the `install` method there for more details.

## Usage

~~~~~
// basic usage
$result = $process->___install();
~~~~~
