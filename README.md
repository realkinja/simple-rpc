<div id="top"></div>


<br />
<div align="center">
  <a href="https://github.com/realkinja/simple-rpc">
    <img src="https://user-images.githubusercontent.com/78376161/179116922-0dd93a66-662e-432f-b535-49e5083577de.png" alt="Logo" width="588" height="144">
  </a>


<h3 align="center">Simple-RPC</h3>

  <p align="center">
    Simple Rich Presence for Discord made with Python and pypresence.
    <br />
    <a href="https://github.com/realkinja/simple-rpc/issues">Report Bug</a>
    ·
    <a href="https://github.com/realkinja/simple-rpc/issues">Request Feature</a>
  </p>

[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

</div>

## About

Ever wanted an RPC for Discord that's easy to setup? Well I've got you covered.

With my simple RPC all you really have to do is edit stuff in the config.json.

As of right now, I didn't yet make a way to have buttons that you can disable and enable, hoping that I can add this in the future.

## Setup

First off, you need Python, which you can get by clicking [here.](https://www.python.org/downloads/)

Once you've finished installing Python, launch a terminal of your choice and type this in.

`pip install pypresence`

Once you're done is go to https://discord.com/developers/applications/

Log in, and make a new application.

Choose a name (it will be visible on your RPC so.)

Now, go to Rich Presence, Art Assets and add an Image that will be the big image in your RPC. (Not the cover image.)

And that's pretty much it! Now, download Simple-RPC by either doing `git clone https://github.com/realkinja/simple-rpc.git` in your Terminal, or by clicking on Code and download zip.

Extract it, now open the config.json, this is where the fun begins.

Open config.json.

Replace the "put your client id here" with the Application ID you can get by going to the Developer Portal, clicking on your application and copying the Application ID.

![rpc ss](https://user-images.githubusercontent.com/78376161/179119615-057bd061-469a-4504-beb4-a9a92bc1b6fd.png)

Here's what you can change and how it will look like.

You can take it from there! The large text is what pops up when hovering over the large Image.

The largeimage is what you named your large Image

The small Image is what appers in the bottom right of your large Image. You don't need to add it.

## Acknowledgments

* [pypresence](https://github.com/qwertyquerty/pypresence) - What I used for this.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/realkinja/simple-rpc?color=blueviolet&style=for-the-badge
[contributors-url]: https://github.com/realkinja/simple-rpc/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/realkinja/simple-rpc?color=blueviolet&style=for-the-badge
[forks-url]: https://github.com/realkinja/simple-rpc/network/members
[stars-shield]: https://img.shields.io/github/stars/realkinja/simple-rpc?color=blueviolet&style=for-the-badge
[stars-url]: https://github.com/realkinja/simple-rpc/stargazers
[issues-shield]: https://img.shields.io/github/issues/realkinja/simple-rpc?color=blueviolet&style=for-the-badge
[issues-url]: https://github.com/realkinja/simple-rpc/issues
