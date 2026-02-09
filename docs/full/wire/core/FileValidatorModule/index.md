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
Method: [getModuleInfo()](method-getmoduleinfo.md)
Method: [isValidFile()](method-isvalidfile.md)
Method: [isValid()](method-isvalid.md)
Method: [getPage()](method-getpage.md)
Method: [getField()](method-getfield.md)
Method: [getPagefile()](method-getpagefile.md)
Method: [log()](method-___log.md) (hookable)
