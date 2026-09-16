# jp3_navidrome_connector

This will be a major challenge, as for some reason. I will develop this API using vim for the first time.
I will also do this without AI, which I have used extensively for the last 2 years.

As I will use at least 3 Libraries for my pthon tech stack I will include a requirements.txt page!

## Coding Norms (shouldn't quite be here but will clean this up later)
For Restful Endpoints - no trailing slashes. e.g. endpoints will be `/health`

---

## Create venv and install requirements

To install python virtual environment:

```bash
python -m venv venv # is this because I gitignore this file.
```

Run this command in order to download virtual environment and libraries for tech stack.

```bash
source venv/bin/activate
pip install > requirements.txt
```

---
## Where to begin
Must now re-evaluate the plan with navidrome. 
Start by configuring the server, without any music. Once done I will investigate how to upload music. This is a todo. Can make tickets once this is done!

config path will be: "/media/music"

port will be running on: 4533

---

## Tagging with Navidrome

Navidrome uses tagging, which means we will not have to set up a system to rename files, but ensure files can be added via an api.

We must ensure tagging norms are bullet proof. Fields we must have are:
- Title
- Album 
- Artist
- Album Artist
- Track Number (is this that important)

Optionally include:
- Year (`yyyy` is accepted)
- Genre

## File and folder naming
- To track for future, we should still have logic to split up music so have:
- Artist/Album/Songs

Follow this pattern

## Images
If image is present save file path in tagging. Should be with Album Folder, name the image cover.jpg or cover.png depending on file ext. Always `cover` for consistency.

## Multi Artists
I'm pretty sure I don't allow multi artists so we can maye skip this.

## Syntax to avoid

Don't use `/` or `;` as this will disurpt folders!

## Tagging guidelines

We must use ID3 tags for mp3 and all audio files these must be encoded with this metadata below:

```json
{
    title: "good 4 u",
    artist: "Olivia Rodrigo",
    albumartist: "Olivia Rodrigo",
    album: "SOUR",
    genre: "pop",
    track: "1",
    year: "2020"
}
```

## API Specifications

This API needs to a way to have:
- CRUD for all of the files and folders in config path.
    - Get (Shows all songs uploaded)
    - Create (Ability to take in a path, create if it doesn't exist)
    - PUT (update songs that exist, old and new filepath and data)
    - Delete (given the path delete it)

- In a seperate folder upload all of the metadata to a JSON file that is updated.
    - This file can be used to match what files exist in navidrome vs jp3

- Have good error handling if anything goes wrong in this process





