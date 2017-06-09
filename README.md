# Rip multiple CDs to FLAC and MP3
abcde (A Better CD Encoder) is a command line audio CD ripper for Linux. The configuration in this repository will rip
an audio CD to FLAC and MP3 V0. Since FLAC is a lossless format, you will not lose any data during the conversion and the `.flac`
files can be transcoded to another music format.

## Rip multiple CDs in parallel
The provided Python script will watch for audio CD files in the directories that you set and then run abcde to rip any newly
entered discs once they are mounted. This allows you to use as many separate disc drives as you want, allowing you to rip
a large collection of audio CDs in a short amount of time, since you are not limited to a single disc drive.

Since abcde is run in non-interactive mode, you will only have to insert the disc and the rest will be taken care of automatically.
When the disc has been ripped, it will auto-eject and you can insert another disc.

## Notice
If you are only going to be using a single disc drive, a recommend not using this script. It is much easier to change the
preferences of your OS to autorun abcde for any audio discs that are inserted into your computer. The purpose of this script
is for ripping multiple CDs at the same time.

## How to use
In order to use this script, you will need to install the following packages:

```
abcde cdparanoia flac imagemagick glyrc lame cd-discid id3 id3v2 libmusicbrainz-discid-perl libwebservice-musicbrainz-perl eyed3
```

Once you have those, update the following line in `.abcde.conf` to include the directory you want the files to save in:
`OUTPUTDIR="{INSERT LOCATION FOR RIPPED TRACKS WITHOUT BRACKETS}"`

Then, make sure to update `script.py` to point to where the audio CDs mount, and run the script.

When you enter a CD, it should automatically start to convert and eject once it is completed.
