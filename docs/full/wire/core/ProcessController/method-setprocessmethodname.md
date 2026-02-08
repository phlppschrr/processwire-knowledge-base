# ProcessController::setProcessMethodName()

Source: `wire/core/ProcessController.php`

Set the name of the method to execute in the Process

It is only necessary to call this if you want to override the default behavior.
The default behavior is to execute a method called "execute()" OR "executeSegment()" where "Segment" is
the last URL segment in the request URL.

@param string $processMethod
