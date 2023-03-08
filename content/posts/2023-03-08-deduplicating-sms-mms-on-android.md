Title: Deduplicating SMS/MMS on Android
Date: 2023-03-08 08:02
Tags: android, python
Summary: Got duplicates in your SMS backups, or already restored them thinking it's too late? Think again!

**TL;DR:** If you want to clean up SMS/MMS duplicates from your Android phone, and know how to run a python script, check out the [README here](https://github.com/pcraciunoiu/AndroidSMSBackupRestoreCleaner#readme).

## The Premise

For one or more reasons below (or even others), you ended up with duplicate SMS or MMS messages on your Android phone. If you're like me and carry them around for years (digital hoarder?), you wanna clean that up and save some space on your device.

* I was using Signal for years for both SMS/MMS and secure messages. Then, Signal decided to [drop support for insecure messaging](https://signal.org/blog/sms-removal-android/) altogether - bummer, but I get it. I exported my messages, but already had some of them on my phone from before. And the duplicates got exported as MMS from signal, instead of SMS, making it tricky to dedupe between the two
* You may accidentally restore multiple backups of your SMS using "SMS Backup & Restore".

## Existing Solutions

I first stumbled upon [DeduplicateSMS](https://play.google.com/store/apps/details?id=com.venomvendor.sms.deduplicate), but unfortunately that hasn't been updated in a while and crashes on Android 9+.

Then I stumbled upon this python script. Thanks to [Roger Cas](https://github.com/radj/AndroidSMSBackupRestoreCleaner) for his detailed [blog post](http://blog.radj.me/removing-duplicates-sms-backup-restore-xml-android), and open sourcing the code on GitHub, I was getting hopeful. Shortly after, I saw that [Hameer Abbasi](https://github.com/hameerabbasi/AndroidSMSBackupRestoreCleaner) forked the repo and added MMS support. Amazing! Now to try it out...

### Running the restore

So I cloned the repo and ran the restore. Hit some issues which were fairly easy to fix, and decided to make some improvements while I'm at it.

## Upgraded Solution

The new solution isn't perfect, it does a lot of duplicate detection in python, but it worked for my use case.

Check it out on GitHub: [https://github.com/pcraciunoiu/AndroidSMSBackupRestoreCleaner](https://github.com/pcraciunoiu/AndroidSMSBackupRestoreCleaner)

I have many ideas for improvement and some of them can be found in the Issues tab.

