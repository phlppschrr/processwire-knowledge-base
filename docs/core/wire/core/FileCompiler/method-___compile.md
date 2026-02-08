# $fileCompiler->___compile($sourceFile): string

Source: `wire/core/FileCompiler.php`

Compile given source file and return compiled destination file

## Arguments

- string $sourceFile Source file to compile (relative to sourcePath given in constructor)

## Return value

string Full path and filename of compiled file. Returns sourceFile is compilation is not necessary.

## Throws

- WireException if given invalid sourceFile
