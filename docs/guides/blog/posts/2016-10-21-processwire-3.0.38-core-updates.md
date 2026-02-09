# ProcessWire 3.0.38 core updates

Source: https://processwire.com/blog/posts/processwire-3.0.38-core-updates/

## Sections


## ProcessWire 3.0.38 core updates

21 October 2016 by Ryan Cramer [ 2 Comments](/blog/posts/processwire-3.0.38-core-updates/#comments)

This week we've got a new dev branch version with several updates which we'll merge to master soon. This post also includes a useful recipe on how to log all outgoing emails sent from your site.


## ProcessWire 3.0.38 updates


### Configurable modules?

There are several core modules that identify themselves as configurable, but actually aren't interactively configurable. You'll see several in the Modules > Configurable drop-down menu, as well as in the modules lists. But when you go to configure them, you find there's nothing there to configure. Now technically these modules are labeled as configurable because they actually do implement the interface for configuration and are storing configuration data somewhere, even if not interactively configurable. But it's still admittedly useless to see them listed as Configurable in the admin.

Awhile back a request came in to have it avoid showing these modules as configurable, since there's nothing for the user to do. This makes sense, but I wasn't sure how to accomplish it at the time. Later it became clear how to implement, so I went ahead and put in this update this week. It's a minor thing, but a nice enhancement too I think.


### SmartyPants module upgrade

We put in an upgrade to the TextformatterSmartypants core module, which really hadn't changed in about 5 years. The latest version enables you to make SmartyPants insert UTF-8 characters rather than HTML entities, which is useful for some scenarios, especially ones where you might be applying other Textformatters that entity-encode afterwards. This behavior is not the default, so if you find you need it, you'll find the configuration option available in the TextformatterSmartypants module configuration.


### Additional WireMail upgrades

We merged a pull request from [BitPoet](https://github.com/BitPoet) that makes some nice tweaks to WireMail, including:

- Support wrapping of long subject headers
- Nest plaintext+html bodies in their own multipart-alternative header if attachments are present so that the display of the html part still has precedence over the plaintext part.
- Put quotes around name parts after quoted-printable encoding of the name in name+address combinations.


### Added support for common multi-language translations

There are several translatable phrases that appear repeatedly across multiple files in ProcessWire. For example, words like "Yes", "No", "Save", "Name", "Label", "New", and about 30 others. Currently, when translating ProcessWire files, one would have to translate these words/phrases every time they appear. Now they can be skipped over and will fall-back to the common translation when available.

When such a phrase is encountered during translation, ProcessWire identifies that to the person translating, so that they can skip over translation of the word/phrase if they would like to. The phrases appear in this file:

/wire/modules/LanguageSupport/LanguageTranslator.php

Once this file has been translated, the phrases are available as translations regardless of what file the word/phrase appears in.


### Bug fixes

We fixed an issue where uploading an image in the CKEditor image dialog, to a page other than the one being edited, resulted in the image potentially being later lost.

We also corrected the behavior of the `Pageimage::maxSize()` method, which was cropping images in some cases where it shouldn't.


## Recipe: Logging all outgoing emails

Lets say that you want to maintain a log of every email sent from your site. This can be done quite easily by hooking the WireMail class. Place the following in your /site/ready.php file:

```
$wire->addHookAfter('WireMail::send', function($event) {
  $mail = $event->object;
  $event->wire('log')->save('sent-mail',
    "SENT ($event->return of " . count($mail->to) . "), " .
    "SUBJECT ($mail->subject), " .
    "TO (" .  implode(", ", $mail->to) . "), " .
    "FROM ($mail->from)"
  );
});
```

*Side note: Why do we use `$event->wire('log')` rather than `wire('log')` to access the [$log](../../../full/wire/core/WireLog/index.md) API variable? In reality, either will work just fine. But with ProcessWire 3.x supporting multi-instance, it's preferable to pull API variables from an existing object in this case (like $event). That ensures that that the $log API variable we get will be from the correct ProcessWire instance (if there happened to be more than one). *

Test things out by sending an email. Here's an example of how I might send a message with the API:

```
$mail->new()
  ->to('test@processwire.com')
  ->from('ryan@test.com')
  ->subject('Hello world')
  ->body('How are you doing?')
  ->send();
```

In your admin, if you go to Setup > Logs > sent-mail, you should see a log entry like this:

```
SENT (1 of 1), SUBJECT (Hello world), TO (test@processwire.com), FROM (ryan@test.com)
```

Of course, the log entry also includes the date/time sent, user and current URL when the email was sent, as this information accompanies all log entries already.

That's it for this week, hope that you have a great weekend and enjoy reading the [ProcessWire Weekly](https://weekly.pw).
