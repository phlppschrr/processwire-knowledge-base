# ProcessWire 3.0.21 and 2.8.21!

Source: https://processwire.com/blog/posts/processwire-3.0.21-and-2.8.21/

## Sections


## ProcessWire 3.0.21 and 2.8.21!

10 June 2016 by Ryan Cramer [ 3 Comments](/blog/posts/processwire-3.0.21-and-2.8.21/#comments)

We've got some great updates for you this week, especially for those still running ProcessWire 2.x. ProcessWire 3.x also got a lot more stable this week. In fact, this week ProcessWire 2.x and 3.x got a lot closer!


## Core updates 3.0.21


### Lots of fixes and enhancements

Like last week, we focused on covering GitHub issue reports this week and made it through all pending issue reports (at the time of writing this). If you look in this week's [commit log](https://github.com/ryancramerdesign/ProcessWire/commits/devns), you'll see there have been quite a lot of updates to the core this week for version 3.0.21! There's still plenty of follow-up remaining on issues we've not been able to reproduce, or needed more information on. But other than that, just about everything is accounted for, and we'll be able to start getting into the queue of PRs very soon.


### Multi-language toggle

For those using ProcessWire in a multi-language environment, you'll also be glad to know of a new feature that was added this week. I was developing a multi-language site this week, but a few sections in the site didn't require multi-language support. All the inputs for 6 extra languages simply weren't needed (and potentially confusing to editors). Yet I didn't want to maintain both single and multi-language versions of all the fields common to those templates. I imagine this is not an unusual scenario for those working with multi-language sites.

The solution was to add a new option that lets you disable multi-language on a per-template basis. When you disable multi-language for a given template, all of its multi-language fields then behave like single language fields, without all the unnecessary extra inputs. You'll see this option under the "Advanced" tab when editing a template. This new feature is particularly useful for sites that want to have the general pages be multi-language, but have some other pages (like press releases or news items) that are not multi-language.


## News for ProcessWire 2.x


### ProcessWire 2.8 arrives

This week I'm happy to say that [ProcessWire 2.8](https://github.com/ryancramerdesign/pw28) is here in a development version. There's not much to write about it because it is technically identical to ProcessWire 3.x, except that it operates without namespaces, like ProcessWire 2.7. So it's basically a hybrid between 2.7 and 3.0, but shares its code with 3.0. We've automated the process so that any change to our 3.x version automatically gets applied to the 2.8 version as well, which makes it very much sustainable from a maintenance standpoint.


### Why have a 2.8 version?

While namespaces are great for ProcessWire and our growth as a project, we've noticed that they also do cause confusion for some. Many people simple don't need ProcessWire to work in a namespace environment, and the namespaces create another thing to keep track of. While we've amended much of that by supporting compiled templates and modules, the reality is that if you genuinely don't need namespace support, we don't think it should be forced on you. We think there's still demand for a version of ProcessWire that continues along the PW 2.x flow with no namespaces.


### Who should use 2.8 and 3.x?

If you are a PHP developer, or using ProcessWire as a framework, or integrating with any other applications (or think you ever will), you will most definitely want to stick with ProcessWire 3.0 and it's namespace support. But if you are simply building a website (whether large or small) where namespaces really don't apply, we want to continue to provide you with the simplest possible path. For those that have no need for namespaces, that will be the 2.8 version. The 2.8 version will replace the 2.7 version of ProcessWire, and continue to get updates every time 3.x gets them.


### 2.8.x versions

The ProcessWire 2.8 version revisions mirror those of ProcessWire 3.x. For instance, this week's 3.x version is 3.0.21 and the 2.8.x version is 2.8.21 (note the common "21" revision). These revisions indicate that the two versions are technically operating from the same core code.

ProcessWire 2.8 is in a [new repository](https://github.com/ryancramerdesign/pw28) (at least temporarily) while we continue testing and determine the best way to make it more official. The intention is that either 3.x or 2.8.x will be viable upgrade paths from 2.7.


### Testing 2.8

Please note that 2.8 has not had a lot of testing at this point, so you'll want to consider this in an alpha state. While the code is functionally identical to 3.x, it should be considered less stable than 3.x since there may still be issues to uncover due to removal of the namespaces that have been present in 3.x for quite some time now. However, those should become apparent quickly and we may be able to release 3.x and 2.8.x official versions at the same time.

The work day has been cut short by a change in schedule (kids), so I've got to stop the post here. But please reply with any questions you may have. Hope that you all have a great weekend and remember to read the [ProcessWire Weekly](http://weekly.pw)!
