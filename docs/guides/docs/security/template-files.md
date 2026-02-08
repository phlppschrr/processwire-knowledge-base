# Security for template files in ProcessWire

Source: https://processwire.com/docs/security/template-files/

## Summary

While ProcessWire handles a lot of the common security considerations before your template files are even loaded, you should also follow security best practices within your template files as you would in any other PHP framework.

## Key Points

- While ProcessWire handles a lot of the common security considerations before your template files are even loaded, you should also follow security best practices within your template files as you would in any other PHP framework.
- Your ProcessWire installation is only as secure as your template files. ProcessWire template files are PHP files, and anything that is possible in PHP is also possible in your template files.
- If your template files deal with any kind of user input, they must sanitize and validate any user input. Never send any kind of user input directly to ProcessWire's API methods (other than those provided by $sanitizer) without first sanitizing it, and validating it where appropriate.
