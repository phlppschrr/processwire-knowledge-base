# ProcessWire 3.0.113 core updates

Source: https://processwire.com/blog/posts/processwire-3.0.113-core-updates/

## Sections


## ProcessWire 3.0.113 core updates

14 September 2018 by Ryan Cramer [ 0 Comments](/blog/posts/processwire-3.0.113-core-updates/#comments)


## ProcessWire 3.0.113

This latest version on the dev branch has a lot of updates and this post covers all the details. The focus this week was on covering the queue of issue reports, and a whole lot of progress was made, plus some other useful additions in ProcessWire 3.0.113.


### Summary of updates

In terms of completed issue reports, there were about fifteen of them covered. See the [commit log](https://github.com/processwire/processwire/commits/dev) for this week (especially September 12 and 13) for most of the details.

The CKEditor version has been upgraded from 4.8.0 to 4.10.1.

The *SessionLoginThrottle* module has been refactored and improved. Previously it was a bit too aggressive when two factor authentication was installed. This fixes that, as well as adds a new configuration setting so that you can log activity.

The *ProcessController* class was refactored so that it now supports method-level permission settings. It uses the existing module info "nav" array permission settings that were previously just used for determining what navigation was shown. As a result, ProcessController can now further reduce the access control/permission code requirements on Process modules.

Added Horst's pull request [#118](https://github.com/processwire/processwire/pull/118) for the *ImageSizerEngine* which improves the output when requesting a dimension larger than what the image can support, by maintaining the aspect ratio. Thanks also to @thomasaull for identifying this and for the suggestions in issue [#628](https://github.com/processwire/processwire-issues/issues/628).

The `$mail` API variable now has shortcut to(), from() and subject() methods to shorten the fluent interface calls for sending an email. For fluent interface calls, it's no longer necessary to call $mail->new(); Now you can do this if you want to:

```
$mail->to('foo@bar.com')
  ->from('bar@foo.com')
  ->subject('Hi')
  ->body('Hello world')
  ->send();
```


### New $sanitizer methods

Several new case conversion methods were added to `$sanitizer`. The need has come up often enough (both in the core and outside of it) that I thought we needed a standard set of case conversion methods in the core Sanitizer class:

```
$sanitizer->hyphenCase('Hello world'); // hello-world
$sanitizer->kebabCase('Hello world'); // hello-world (alias)
$sanitizer->snakeCase('Hello world'); // hello_world
$sanitizer->camelCase('Hello world'); // helloWorld
$sanitizer->pascalCase('Hello world'); // HelloWorld
```

You can pass these methods a short string (like above) or a giant string of text. They will take whatever you throw at them. While the hyphen/kebab case methods might seem very similar to the pageName() sanitizer, they are actually quite a bit simpler and more standard for general purpose use, rather than page names.


### Special support for required attributes

Implemented @Toutouwai request [#224](https://github.com/processwire/processwire-requests/issues/224) which enables using HTML5 required attribute on inputs that aren't visible. Previously it wasn't practical to use them so much because when the user hits the Save button, the error for the missing required field might appear on a different tab than the user is on. Thus, they would never see the browser error message. This update captures that scenario and automatically changes it to the right tab, and opens any fieldsets and Inputfields as needed till it can reveal the field with the missing requirements.

This update also adds JS API methods, which were built in part to accomodate the above:

- `InputfieldFocus($inputfield)` - Show given $inputfield element, regardless of where it is (changing tabs, open fieldsets/fields as needed), and focus.
- `InputfieldOpen($inputfield)` - Open the given $inputfield element.
- `InputfieldClose($inputfield)` - Close/collapse the given $inputfield element.

Thanks to @Toutouwai (Robin S) for the suggestion and initial code that got this started.

Thanks for reading this week's summary of updates in ProcessWire 3.0.113 and have a great weekend. Visit the [ProcessWire Weekly](https://weekly.pw) for the latest ProcessWire news and updates!
