# WireUpload::saveUpload()

Source: `wire/core/WireUpload.php`

Save the uploaded file

@param string $tmp_name Temporary filename (full path and filename)

@param string $filename Actual filename (basename)

@param bool $ajax Is this an AJAX upload?

@return array|bool|string Boolean false on fail, array of multiple filenames, or string of filename if maxFiles=1
