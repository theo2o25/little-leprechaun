# The Little Leprechaun

An interactive children's storybook web app built with Streamlit, based on the book _The Little Leprechaun_ by Adam Molden.

## Run it

```bash
pip install -r requirements.txt
streamlit run app.py
```

## How it works

- Displays each illustrated page of the book (`page_1.png` ... `page_13.png`).
- Back / Next navigation with a progress bar.
- **Listen to this page** reads the story aloud using the browser's text-to-speech.
- Interactive surprises: make Mani wave on the moon page, and sprinkle the stars on the ending page.
- "Did you know?" fun facts and a parents' corner.

## Notes

- The app expects the book's illustration files in a folder configured via `BOOK_DIR` at the top of `app.py` (currently `E:\Books\The Little Leprechaun`). The PNGs are not included in this repository.
- Per-page text and ordering live in the `PAGES` list in `app.py`.
