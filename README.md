# English-Chinese Digital Dictionary

## Project Overview
A bilingual dictionary application with GUI and CLI interfaces, implementing word lookup, spelling correction, and phrase search. Features Trie-based prefix search and edit-distance algorithm for spelling suggestions.
## How to Use
- **Launch GUI Version**
  `python3 gui.py`
- **Launch CLI Version**
  `python3 cli.py`
## GUI Instructions
- **Search box supports**:
  - Direct word input + Enter/Search button
  - Real-time prefix suggestions (double-click to select)
  - Click Correct button for spelling suggestions
- **Result formatting**:
  - Black bold: Query headword
  - Clickable related words (gray text)
  - Regular text: Definitions
## CLI Instruions
  At the ":" prompt：
  |prompt|to do|
  |:-:|:-:|
  |`f:word`|Lookup word|
  |`c:word`|Get corrections|
  |`p:prefix`|Prefix search|
  |`e:`|Exit the program|
## Requirements
  - Python **3.6**+
  - Standard libraries: tkinter(just the **gui** version), json, heapq
## Sample Dictionary Data Format
  ```json
{
  "algorithm": {
    "meaning": {
      "n.": "a process or set of rules to be followed in calculations"
    },
    "phrase": {
      "algorithm design": "the process of creating mathematical processes"
    }
  }
}
  ```
