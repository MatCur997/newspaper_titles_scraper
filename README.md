# newspaper_titles_scraper

Collects the latest headlines from the RSS feeds of three Italian newspapers
(Corriere della Sera, La Repubblica, Il Messaggero) and saves them to a CSV
file. It can run locally or as a manually triggered GitHub Actions workflow.

## What it does

`RSS_Scraper.py` reads the homepage feed of each newspaper with `feedparser`,
takes the first 10 entries and writes one row per headline:

| Column | Content |
| --- | --- |
| `Timestamp` | time of the run |
| `Newspaper` | source |
| `Title` | headline |

The output file is `dataset_YYYY-MM-DD_HH-MM.csv`, in the current directory.

## Usage

```bash
pip install -r requirements.txt
python RSS_Scraper.py
```

### GitHub Actions

The workflow in `.github/workflows/scraper.yml` ("Esegui Scraper") is started
by hand from the Actions tab. It installs the requirements on Ubuntu with
Python 3.11, runs the script and uploads the CSV as the `dataset_giornata`
artifact.

## Known limitations

- Only headlines are saved: no links, publication dates or article text.
- The feed URLs are hard-coded; if a newspaper changes or removes its feed,
  that source is missing from the output.
- Each run writes a separate file: there is no deduplication across runs.

## License

MIT (see `LICENSE`).
