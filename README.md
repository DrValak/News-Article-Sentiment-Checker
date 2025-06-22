# News Article Sentiment and Word Frequency Analyzer

This Python script fetches a news article from a given URL, cleans the text, removes Portuguese stop words, and analyzes the sentiment based on the frequency of positive and negative words. It also allows for easy extension to count word frequencies.

## Features

- Fetches and parses HTML content from a news article URL.
- Cleans the text by removing scripts, styles, navigation, footer, and header elements.
- Extracts and joins all paragraph texts.
- Removes common Portuguese stop words.
- Counts the number of positive and negative words based on predefined lists.
- Prints the overall sentiment of the article (positive, negative, or neutral).

## Requirements

- Python 3.x
- [requests](https://pypi.org/project/requests/)
- [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)

Install dependencies with:

```bash
pip install requests beautifulsoup4
```

## Usage

1. Edit the `url` variable in the script to point to the news article you want to analyze.
2. Run the script:

```bash
python test_url.py
```

## How It Works

1. **Fetch Article:**  
   The script uses `requests` to download the HTML content from the specified URL.

2. **Parse and Clean HTML:**  
   It uses `BeautifulSoup` to parse the HTML and remove unnecessary elements like scripts, styles, navigation, footer, and header.

3. **Extract Text:**  
   All paragraph (`<p>`) elements are extracted and joined into a single string.

4. **Remove Stop Words:**  
   The text is split into words, and common Portuguese stop words are filtered out.

5. **Sentiment Analysis:**  
   The script counts how many words from the filtered list are in the predefined positive and negative word lists, then prints the counts and the overall sentiment.

## Customization

- **Add More Stop Words:**  
  Extend the `stop_words` list for better filtering.
- **Expand Sentiment Lists:**  
  Add more words to `positive_words` and `negative_words` for improved sentiment detection.
- **Word Frequency:**  
  To print the most frequent words, you can use Python's `collections.Counter` on the `filter_words` list.

## Example Output

```
Positive words: 2
Negative words: 5
The article has a more NEGATIVE tone
```

## License

This project is licensed under the MIT License.
