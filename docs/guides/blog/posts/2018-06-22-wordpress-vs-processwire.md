# WordPress vs. ProcessWire

Source: https://processwire.com/blog/posts/wordpress-vs-processwire/

## Sections


## Comparing WordPress with ProcessWire

22 June 2018 by Ryan Cramer [ 5 Comments](/blog/posts/wordpress-vs-processwire/#comments)


## PW & WP video series

[Jonathan Lahijani](https://processwire.com/talk/profile/495-jonathan-lahijani/) recently released a great series of [ProcessWire vs. WordPress videos](#watch-the-wordpress-vs-processwire-videos). This week, we'll highlight these and take a closer look. The scope, quantity and quality of the videos made me curious about what inspired them, as well as the process that Jonathan used in making them. I was also interested in his experiences, having significant expertise in both WordPress and ProcessWire. So we'll cover some of that exchange in this blog post as well.


### WordPress vs. ProcessWire video topics

As you might know, ProcessWire and WordPress are really different animals, and they can be difficult to directly compare, being so different. Many in the ProcessWire community started with WordPress and then moved on to ProcessWire as their needs as a developer—and very often the needs of their clients—grew and evolved. The title and scope of this video series naturally limits it to aspects that have equivalents between WordPress and ProcessWire, and I imagine it will be especially useful to web designers/developers that are migrating from WP to PW, or those considering it. However I think the [videos](#watch-the-wordpress-vs-processwire-videos) are also useful even to developers that work with ProcessWire exclusively, as Jonathan really knows his way around the system and there's a lot to learn from these.

Most of the videos start by looking at the WordPress side of things, and then switch to looking at the same aspect in ProcessWire. It is very educational, the pace is fast, and Jonathan does a great job of focusing on the more important bits, making the videos easy and enjoyable to watch. There is something to learn in all of these. The playlist currently includes a comprehensive set of 36 videos comparing WordPress with ProcessWire in the following topics:

- Installation
- Admin
- Pages
- Page Templates
- Custom Fields
- Page Order
- Visual WYSIWYG Editor
- Flexible Content / Section Builders
- Custom Post Types
- Documentation
- The Loop
- Front-end Editing
- Images
- Search
- Users and Roles
- Global Settings and Options
- Plugins
- Updates
- Database Backups
- Shortcodes
- Forms
- Menus
- Search Engine Optimization (SEO)
- XML Sitemaps
- Config File
- Comments
- Revisions
- Themes
- Page Caching
- Multi-Language
- Bootstrapping
- Debugging
- Composer
- Database Structure
- Command Line Interface
- Community

While many of the videos show older versions of ProcessWire, this really doesn't reduce their value in the slightest, as the core concepts of ProcessWire are largely consistent across all major versions.


### About the WordPress vs. ProcessWire videos

*Here's how Jonathan describes this set of videos (from YouTube). *

**Jonathan: **This series compares different aspects of both WordPress and ProcessWire CMS. I made this series to introduce ProcessWire to advanced WordPress developers after having searched for an alternative to WordPress. I worked with WordPress for over 8 years and became unsatisfied with many aspects, such as the reliance of plugins that should really be in the core (for example, Advanced Custom Fields), major security issues, performance problems, and wanting true control of my frontend.

After evaluating dozens of content management systems, I found ProcessWire to be beautifully architected and extremely fun to work with. The community is amazing as well. Most importantly, because they are both PHP/MySQL systems, the transition was not too painful. The videos in this series will answer major questions in that regard.

Note: Most of the videos in series were recorded in 2014 through 2016 (and uploaded June 2018), so some interfaces may look "old", but it's mostly consistent. Please visit [wirecasts.com](http://wirecasts.com) for more information and join my mailing list. Also please [subscribe to my YouTube channel](https://www.youtube.com/channel/UCAzZwO7DZ91tQmZqZwe5vuQ).


### Jonathan’s production tools and process

*I was really impressed with Jonathan’s videos and curious about his process, as well as anything learned from working on these. Following are some excerpts from our conversation.*

**Ryan:** I'm curious to know what tools you used, whether you recorded the voiceover and video separately, and how much editing it took? I've always struggled making screencasts, but it appears you've got it all figured out. Nice job!

**Jonathan:** I use Camtasia. It includes the recorder and the editor, which are both feature rich and easy to use. My approach involves first writing a script or outline of what I'm going to say, sometimes followed up with a dry-run. I keep that to one side of my screen in a text file. Then I setup all the necessary windows and browser tabs. I then record it while talking. Sometimes I'll pause the video recording when switching between things (easy to do with Camtasia since there's a key assigned to pause/resume) or if I need to edit my script. If I screw up anytime during recording, I usually just keep recording and repeat what I'm trying to demonstrate until I get it right, then I cut out the bloopers during editing. To make it easy to identify bloopers when recording, I say "CUT" (in a louder voice), which makes quickly identifiable in the audio timeline. It's faster and less tedious this way.

I recorded those videos at 720p (1280x720), but 1080p is better (1920x1080). At these resolutions, you won't have any letterboxing since most devices (TVs, phones, standard sized monitors) use this ratio. As you record at higher resolutions (1080p and above), text becomes smaller, so bumping up the font size in my browser, text editor and terminal is advised since it makes it easier for the viewer to read. They're recorded at 30fps.

I also have a Blue Yeti mic with a pop filter so it sounds professional (although there was still quite a bit of "popping" in some of these videos... I'll have to fix that in future videos). Some videos in the WP vs. PW series were with a headset mic, and some were with a my Blue Yeti mic. Audio leveling is easy to do in Camtasia as well. Just a couple clicks.

For [Wirecasts](http://wirecasts.com), at least for the series of videos that are chronological (one of which I'm most likely naming "ProcessWire From Scratch"), an easier approach is one where I just simply record how I would normally build a site (which will take like a few hours depending on how deep I go; no narration during the recording), THEN cut it up into various pieces that make sense and injecting things like the documentation/API section of processwire.com to demonstrate what I'm coding and its origination. With this approach, it puts much less pressure to figure out the best outline and come up with exactly what I should say while I'm recording, which I can instead figure out while doing a voice-over for during editing. I tried this approach with some of the WP vs. PW videos, but it didn't work well, but I know it will with heavily chronological videos.


### Strengths of ProcessWire vs. strengths of WordPress

**Ryan:** In your experience working with both WordPress and ProcessWire, what technical strengths do you think WordPress has relative to ProcessWire, and ProcessWire relative to WordPress? Please exclude the obvious market share difference and all that accompanies that, and instead focus on aspects that only you might know from your extensive experience with both platforms.

**Jonathan:** ProcessWire has too many technical strengths to name here, but the one that immediately stood out to me when trying out ProcessWire back in 2012 was how custom fields were done in the system and how it's a native, first-class feature. Simply put, everything is a custom field, which in-turn makes the API easy to work with and querying data from these fields is super simple.

In WordPress, there are a handful of built-in fields (title, content, excerpt, date), and then there's WordPress's approach to custom fields (key value pairs). However it's an extremely basic implementation unless you use a plugin to take it to the next level. Every advanced WordPress developer has heard of Advanced Custom Fields ([ACF](https://www.advancedcustomfields.com/)) or similar plugins. But even then, the way the field data is stored in WordPress's database ('wp_postmeta' table) quickly leads to performance bottlenecks and [querying the data is awkward](https://codex.wordpress.org/Class_Reference/WP_Query#Custom_Field_Parameters).

I believe WordPress's strengths are related to it's opinionated setup as opposed to those that are technical. For example, with a fresh installation of WordPress, you are by default given blogging capability, a page system, a menu builder, categories, tags, a media library and a handful of themes, none of which ProcessWire has with a blank site profile, nor which are standardized.

Of course, these are only strengths depending on the developer's skill level. Early in my career, I would rely on these features, but as I started to build more complex websites, these features came to be seen as bloat and would oftentimes go unused. For example, how many WordPress websites utilize the Blog/Posts feature of WordPress? I would guess fewer than 50%. What if you need a few extra custom fields on WordPress's standardized Categories feature? Things get tricky from there, while in ProcessWire creating categories is just fields, templates and pages, like everything else.


### Further Insights on WordPress, ProcessWire and the videos

**Ryan:** What were the most useful things that you learned from creating this series of videos? (whether about the platforms, or the video making process)?

**Jonathan:** Creating informative and engaging videos is definitely a challenge, and oftentimes my level of wanting things to be *perfectly* displayed and communicated gets in my own way. This is part of the reason why I sat on these videos for a couple years before deciding to release them, which was silly of me. Also, when creating videos, it forces you to think about what the end-result of a series will be and how to cut the videos into pieces to get to that end-result in a logical way. Combine that with wanting to make sure you touch upon certain features that aren't used as often (say, URL Segments), and it can become challenging. Lastly, I tend to talk quickly in my everyday life, so remembering to slow down and enunciate my words is helpful when talking into the mic. :)


### Plans for future videos

**Ryan:** I see you've also done other ProcessWire videos, such as this set on [3rd party module demos](https://www.youtube.com/playlist?list=PLOrdUWNK38ia_owzEUTmLoW4ysGrlOSUI). Can you tell us more about your future plans for videos, as well as Wirecasts.com?

**Jonathan:** I've been using ProcessWire practically everyday for the last 6 years and I'm very thankful I found it. I think developers can relate to how the tools and systems they use everyday can have an impact on their career and levels of satisfication in other parts of their life. Part of my goal with the videos I make is to help grow the community and increase the exposure of ProcessWire to people who haven't heard of it yet, or have inertia in giving it a shot. With the WordPress vs. ProcessWire series, I felt like I could reach and speak to a large portion of developers where ProcessWire would be a good fit, especially for those who "outgrow" WordPress, like myself.

When it comes to learning any sophisticated software or system, there are many resources available: official documentation, blog articles, forum posts and various videos. Oftentimes, if a software has a large enough following, premium resources get developed. A great example of this is [Laracasts.com](https://laracasts.com/) by Jeffrey Way, which I'm also subscribed to and has been an invaluable resource. He's an excellent teacher and his [podcast](https://laracasts.com/podcast) is insightful in explaining how he does it... like a behind-the-scenes look at how the sausage gets made.

So my goal of Wirecasts.com is just that... a premium resource that demonstrates how to use ProcessWire in-depth and how to make the most complex of websites as cleanly as possible, which is what I've done over all these years. I want it to save developers who are new to the system hundreds of hours of time and have fun in the process. And for those who are not as skillful in coding, provide a great segway into writing code without feeling overwhelmed. It seems a lot of innovation in the WordPress space is this mantra of "no code required," while I think writing code should be embraced depending on the circumstances. With ProcessWire, I believe that knowing just the basics of PHP (like loops and conditionals), you can do more than you think.


### Watch the WordPress vs. ProcessWire videos

You can go directly to the [WordPress vs. ProcessWire video playlist at YouTube](https://www.youtube.com/playlist?list=PLOrdUWNK38ibz8U_5Vq4zSPZfvFKzUuiT), or you can watch them below. Below is the first video in the playlist. To reveal the playlist and jump to a specific video, click the icon in the top left corner of the video below:

Thanks for reading! Also thanks to Jonathan for creating these videos. You might also want to subscribe to Jonathan's [Wirecasts list](http://wirecasts.com) to be notified when he launches his new site with more ProcessWire-related videos like these. I also recommend subscribing to [Jonathan’s YouTube channel](https://www.youtube.com/channel/UCAzZwO7DZ91tQmZqZwe5vuQ). Next week, we'll be back with coverage of ProcessWire 3.0.107. And for more ProcessWire news and updates be sure to read the [ProcessWire Weekly](http://weekly.pw).
