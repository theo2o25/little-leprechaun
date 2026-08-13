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

- The book's page illustrations are included in `images/` (`page_1.png` ...
  `page_13.png`), so the app runs out of the box from this repo.
- To use a different image folder, set the `LEPRECHAUN_BOOK_DIR` environment
  variable (or `BOOK_DIR` in Streamlit secrets). The app checks, in order:
  `LEPRECHAUN_BOOK_DIR` -> `BOOK_DIR` secret -> the local `images/` folder.
- Per-page text and ordering live in the `PAGES` list in `app.py`.
