# A look at FormBuilder v34

Source: https://processwire.com/blog/posts/formbuilder-v34/

## Sections


## A look at FormBuilder v34

8 June 2018 by Ryan Cramer [ 3 Comments](/blog/posts/formbuilder-v34/#comments)

I'm still working on the latest version of ProcessWire (version 3.0.106) and don't have it quite ready to push to GitHub today, so we'll save that for next week. But I do have a fairly major FormBuilder release ready, and am placing it for download in the FormBuilder support board today. In this post, I'll cover what's new in this version of FormBuilder. After that, there is a how-to guide for using hooks in FormBuilder, though some might also find it also generally useful for any hooks in ProcessWire. Lastly, there's a FormBuilder hooks reference, which has been asked for a few times lately, so figured that was a good way to round out this FormBuilder blog post.


### FormBuilder version 34

[FormBuilder](/blog/categories/form-builder/) was the first ProcessWire Pro module, and it remains one of the most popular in the [ProcessWire store](/store/). With each new version, FormBuilder gets more and more powerful, while remaining very simple to use. Today I'm posting version 34 (0.3.4) of FormBuilder to the support board [download thread](/talk/topic/1844-form-builder-download-and-updates-032/) (available to FormBuilder subscribers), right after publishing this post. While I've been using this version quite a bit here (and we're using it on this site too), for the moment, I'm considering this a beta version, since there is so much that is new. So if you opt to use it, please let me know if you run into any issues. Below is a partial list of what's new in this version, along with screenshots were relevant.

**New email files as attachments option.** Previously files could only be accessed via protected URL on the server. Now you can optionally configure your forms to add user uploaded files as attachments to the email that gets sent to the administrator. This option is found under the Actions tab when editing a form, in the "Send email to administrators" fieldset, field: "How to handle uploaded files?"

The file attachment feature works when using the core built-in WireMail in ProcessWire 3.x. It should also work in any version of the core when paired with one of the following WireMail modules: [WireMailSMTP](https://modules.processwire.com/modules/wire-mail-smtp/), [WireMailPHPMailer](https://modules.processwire.com/modules/altivebirit/), [WireMailMailgun](https://modules.processwire.com/modules/wire-mail-mailgun/) or [WireMailMandrill](https://modules.processwire.com/modules/wire-mail-mandrill/). As far as I can tell, WireMailSwiftMailer and WireMailMailChimp do not support attachments (though someone correct me if I'm wrong).

**Support for automatically deleting form submissions (entries) from the server, after a specific number of days. **This is useful if you don't want user-submitted data to live on the server indefinitely. The option can be found on the Actions tab when editing a form, in the "Save to entries database" fieldset, field: "Automatically delete entries after how many days?". FormBuilder performs entry maintenance twice per day via LazyCron.

**Multi-language options are now available for Select, Checkboxes, Radios and AsmSelect Inputfields, as well as any others that extend them.** Previously you had to use Page fields for multi-language options. Note however that in order to take advantage of it, you have to use ProcessWire 3.0.105 or newer.

**Improved drop-down menus in Setup > Forms**, now lets you drill down directly to form-specific entries or editor. In addition, the main form list (and dropdown) now shows when the last form entry was received for each form.

**Support for form-specific custom email template files.** While this support was actually added in the previous version, it was not yet documented. Documentation can now be found in those template files.

**New markdown and HTML options for defining your success message in the form editor. **Previously the success message was plain text, unless you used a hook to modify it.

**New option to specify multiple auto-responder fields** (fields containing email address to send auto-responder to).

**Added ability to edit the tags that FormBuilder uses for embed methods A and B.** It is editable in the FormBuilder module configuration “Output” fieldset. In addition, this enables you to do things like force it to always load forms from HTTPS, or use URL without scheme/host if you prefer it.

**Several new hooks have been added **to the form rendering, processing and saving events. We'll outline all the available hooks in this post.

In addition to the above, various improvements have been made throughout to improve appearance and UI in AdminThemeUikit. Visual improvements have been made to the FormBuilder module configuration screen. And of course this version also contains several other minor tweaks, fixes and adjustments not mentioned here.


### FormBuilder hooks: how-to guide

This section has moved here: [FormBuilder hooks](/store/form-builder/hooks/)


### FormBuilder hooks reference

This section has moved to a new page: [FormBuilder hooks](/store/form-builder/hooks/)

FormBuilder subscribers can download FormBuilder v34 in the [FormBuilder support board](/talk/topic/1844-form-builder-download-and-updates-032/) (download thread, requires login). Check back here next week for ProcessWire 3.0.106 and be sure to check in at [weekly.pw](http://weekly.pw) this weekend for the latest issue of ProcessWire Weekly. Thanks for reading and have a great weekend!
