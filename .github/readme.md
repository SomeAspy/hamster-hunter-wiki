# Official Hamster Hunter Wiki

## Endorsed by Hamuno

> [!NOTE]
    Assets are spelled exactly how the game references them internally.
    Do not open issues renaming assets.

I made this because the wiki is on Fandom.
I HATE FANDOM SO MUCH

## To build the site

I used [uv](https://docs.astral.sh/uv/) because I took a liking to it.
To prepare the environment just run `uv sync`
Build with `uv run zensical build`
Use `uv run zensical serve` to watch the files and serve for development

production should be served out of `dist`

Building the site itself

## Rendering the D2 Diagram

You should only need to do this if you actually modify the diagram or the pictures it links to.

The diagram for crafting is made in [D2lang](https://d2lang.com/)

To render it just run `d2 recipes.d2 pages/assets/recipes.svg`

The D2 binary is not included in this repo, so just use their install script.
