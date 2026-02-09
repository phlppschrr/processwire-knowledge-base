# FileValidatorModule::getModuleInfo(): array

Source: `wire/core/FileValidatorModule.php`

Get module information

FileValidator modules should provide their own getModuleInfo() with the
key part being the 'validates' property (see below).

## Usage

~~~~~
// basic usage
$array = FileValidatorModule::getModuleInfo();
~~~~~

## Return value

- `array`
