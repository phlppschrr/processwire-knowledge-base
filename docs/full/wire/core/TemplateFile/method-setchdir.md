# $templateFile->setChdir($chdir)

Source: `wire/core/TemplateFile.php`

Set the directory to temporarily change to during rendering

If not set, it changes to the directory that $filename is in.
To disable TemplateFile from changing any directories, set to false (3.0.154+).

## Arguments

- `$chdir` `string|bool`
