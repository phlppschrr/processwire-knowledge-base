# FileCompiler::___compile()

Source: `wire/core/FileCompiler.php`

Compile given source file and return compiled destination file

@param string $sourceFile Source file to compile (relative to sourcePath given in constructor)

@return string Full path and filename of compiled file. Returns sourceFile is compilation is not necessary.

@throws WireException if given invalid sourceFile
