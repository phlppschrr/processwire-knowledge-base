# New modules, file validation, and great websites

Source: https://processwire.com/blog/posts/new-modules-and-great-websites/

## Sections


## New modules, file validation, and great websites

27 December 2019 by Ryan Cramer [ 0 Comments](/blog/posts/new-modules-and-great-websites/#comments)

Hope that you had a Merry Christmas and a great week. Time to get ready for 2020 — Happy New Year!

With this being a holiday week, family in town and kids home from school, there's not much time for work! Nevertheless we’ve got a lot to cover here, including release of the new LoginRegisterPro module, a new FileValidator module, and also a couple of really cool ProcessWire powered websites I became aware of this week.

Focused on our upcoming new master release, this week there have been just minor changes and additions to the core. I’m basically just keeping my eye out for any showstopper issues on GitHub and trying to avoid making any additions or changes that might require live testing. This is to ensure that we can get our next master version released by or before January 1st. I think we’re ready for that master version now, but am going to wait a few more days, just to be sure. Following that, we’ll get back to more regular additions/changes on the dev branch and working through other GitHub issues.


### [](/store/login-register-pro/)LoginRegisterPro released

The LoginRegisterPro module was released on the 24th and is [now available](/store/login-register-pro/) in the ProcessWire store. This module has been covered in previous posts and now has a dedicated [info page](/store/login-register-pro/) and comprehensive [documentation page](/store/login-register-pro/docs/), so see those for more details. If you've ever wanted to maintain a website with secure front-end login, new user registration, profile editing and more, I think you'll really like this one.

As a thanks for getting it during the beta period (which will go till January 1st) use coupon code PWLRBETA1 to subtract $20 from the Personal/single edition, or PWLRBETA2 to subtract $40 from the Dev or Agency edition. These are used at checkout. Thank you for all of the interest in this module and I hope that you like the result as much as I've enjoyed building it. I'm very excited about this addition to the collection Pro modules available here.


### New FileValidatorImage module

This week I released a module (available on GitHub or in the modules directory) that performs comprehensive validation of image files: [FileValidatorImage](https://github.com/ryancramerdesign/FileValidatorImage). This uses ProcessWire’s [FileValidatorModule](https://github.com/processwire/processwire/blob/dev/wire/core/FileValidatorModule.php) pre-defined module type, which (as far as I know) is something only Adrian had put to use before, with his [FileValidatorSvgSanitizer](https://github.com/adrianbj/FileValidatorSvgSanitizer) module.

This module implements ProcessWire’s FileValidator interface, which is used by $sanitizer->validateFile() as part of ProcessWire’s built-in file validations. This is used by existing file uploads in InputfieldFile and InputfieldImage, for example. This module adds support for validation of common image bitmap formats, currently JPG, PNG, GIF.

The new FileValidatorImage module focuses on validating JPG, PNG and GIF files more thoroughly than the core. The nice thing about FileValidator modules is that the core already supports and uses them, and has for a long time. They are used automatically whenever a file is uploaded (without you having to configure anything). In addition, ProcessWire’s [$sanitizer->validateFile()](../../../full/wire/core/Sanitizer/method-validatefile.md) uses them automatically as well. Below is a list of validations that the Image FileValidator module performs:

- Extension must be one of: jpg, jpeg, gif, png.
- Image type must match PHP’s `IMAGETYPE_*` constant for GIF, PNG or JPEG.
- Image type must be consistent with that specified by file extension.
- MIME type must be consistent with that specified by file extension.
- MIME type must be any one of the following: image/gif, image/png, image/jpeg, image/pjpeg, image/x-png.
- EXIF data must not contain specific PHP or Javascript malware.
- Image must always be greater than 1x1 in size dimension.
- Image must fit within specified min-width/min-height and max-width/max-height dimensions (if used).


### About FileValidator modules

I’m going to be developing more FileValidator modules for other file types like PDF and others shortly. The reason for a renewed focus on FileValidator modules is in part related to an upcoming feature in the LoginRegisterPro module. I’ve been developing a front-end file uploads feature for it (via a module named InputfieldFrontendFile), and in this environment we aren’t dealing with trusted users. So we have to maintain much stronger validation than we would in an admin (trusted user) environment.

The FileValidator modules seem like an ideal way to handle this, and they’ve been (so-far) underutilized, so I’m going to continue building them out for more file types. Having the appropriate FileValidator module(s) will be a necessity with front-end file uploads, like in LoginRegisterPro, but also definitely a useful addition on any ProcessWire-powered site.


## New ProcessWire-powered websites

I’m always amazed at the work you all are doing in building websites with ProcessWire. There’s just some really impressive work coming from the community and I wanted to highlight a couple that caught my attention this week.


### [](https://www.aaroncopland.com/)Aaron Copland

[The website for composer Aaron Copland](https://www.aaroncopland.com/) was posted this week by Macrura and he’s done a beautiful job with it. Ever since I was a little kid, I’ve always really enjoyed Aaron Copland’s music, and I was really honored to see this amazing website running ProcessWire. Macrura posted more details about the website and what tools were used in this [forum thread](https://processwire.com/talk/topic/22807-aaron-copland/). There’s a discussion thread on the website going there as well.


### [](https://sonomotors.com/)Sono Motors

[The website for Sono Motors](https://sonomotors.com/) is a beautiful ProcessWire-powered site that long-time ProcessWire user Jakob Härter emailed me about this week. I had never seen it, and I don't think he's yet posted it to our sites directory. As a [fan](/blog/posts/tesla-model-s/) of electric cars, I was really captivated by the website and the product it represents. Take some time to click around, it’s really quite impressive. Sono Motors is an EV startup with 100 employees working to bring an impressive and innovative solar-electric car to the market. From what I understand, they are fighting hard to keep their project going and could use our support in getting the word out, especially now. So if you have any kind of social reach I know they’d appreciate your support in sharing their impressive project and website with the world.

See more ProcessWire powered websites in our [sites directory](/sites/) and [Showcase board](https://processwire.com/talk/forum/9-showcase/) and please [add your sites](https://processwire.com/sites/submit/) too.

Thanks for reading, and be sure to read the always awesome [ProcessWire Weekly](https://weekly.pw) this weekend too. Have a great weekend and a Happy New Year!
