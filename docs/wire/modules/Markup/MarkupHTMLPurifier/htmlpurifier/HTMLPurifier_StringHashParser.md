# HTMLPurifier_StringHashParser

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/HTMLPurifier.standalone.php`

Parses string hash files. File format is as such:

     DefaultKeyValue
     KEY: Value
     KEY2: Value2
     --MULTILINE-KEY--
     Multiline
     value.

Which would output something similar to:

     array(
         'ID' => 'DefaultKeyValue',
         'KEY' => 'Value',
         'KEY2' => 'Value2',
         'MULTILINE-KEY' => "Multiline\nvalue.\n",
     )

We use this as an easy to use file-format for configuration schema
files, but the class itself is usage agnostic.

You can use ---- to forcibly terminate parsing of a single string-hash;
this marker is used in multi string-hashes to delimit boundaries.

## parseMultiFile()

Parses a file that contains multiple string-hashes delimited by '----'
@param string $file
@return array

## parseHandle()

Internal parser that acepts a file handle.
@note While it's possible to simulate in-memory parsing by using
      custom stream wrappers, if such a use-case arises we should
      factor out the file handle into its own class.
@param resource $fh File handle with pointer at start of valid string-hash
           block.
@return array
