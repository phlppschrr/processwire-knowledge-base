# FileValidatorModule

Source: `wire/core/FileValidatorModule.php`

Inherits: `WireData`
Implements: `Module`

Base class for FileValidator modules

Base class for FileValidator modules, which validate uploaded files.
To create a FileValidator module:

1. Create a class that extends this and follow the naming convention: `FileValidator[Something]`.
2. Place in file: /site/modules/FileValidator[Something].module (or in module-specific directory).
3. Copy the `getModuleInfo()` method out of this class and update as appropriate.
4. Implement an `isValidFile($filename)` method, and you are done.

Example: /site/modules/FileValidatorHTML.module
~~~~~~
class FileValidatorHTML extends FileValidatorModule {
    public static function getModuleInfo() {
      return array(
        'title' => 'Validate HTML files',
        'version' => 1,
        'validates' => array('html', 'htm'),
      );
    }
    protected function isValidFile($filename) {
        $valid = false;
        // some code to validate $filename and set $valid
        return $valid;
    }
}
~~~~~~

This file is licensed under the MIT license
https://processwire.com/about/license/mit/

Methods:
- [`getModuleInfo(): array`](method-getmoduleinfo.md) Get module information
- [`isValidFile(string $filename): bool|int`](method-isvalidfile.md) Is the given file valid? (this is the method modules should implement)
- [`isValid(string $filename): bool|int`](method-isvalid.md) Is the given file valid?
- [`getPage(): NullPage|Page`](method-getpage.md) Get the Page associated with any isValid() calls
- [`getField(): null|Field`](method-getfield.md) Get the Field object associated with any isValid() calls
- [`getPagefile(): Pagefile|null`](method-getpagefile.md) Get the Pagefile or Pageimage object associated with any isValid() calls
- [`log(string $str = '', array $options = array()): WireLog|null`](method-___log.md) (hookable) Log a message for this class
