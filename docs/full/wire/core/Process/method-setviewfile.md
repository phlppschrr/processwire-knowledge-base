# Process::setViewFile()

Source: `wire/core/Process.php`

Set the file to use for the output view, if different from default.

- The default view file for the execute() method would be: ./views/execute.php
- The default view file for an executeFooBar() method would be: ./views/execute-foo-bar.php
- To specify your own view file independently of these defaults, use this method.


@param string $file File must be relative to the module's home directory.

@return $this

@throws WireException if file doesn't exist
