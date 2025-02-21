# English-Chinese Digital Dictionary

A feature-rich bilingual dictionary application with dual interface support, implementing efficient word lookup, intelligent spelling correction, and contextual phrase search.

## Features Highlights
- **Dual Interface**: Choose between GUI (graphical) or CLI (command-line) versions
- **Smart Search**:
  - Instant prefix suggestions using Trie algorithm
  - Context-aware spelling corrections with edit-distance algorithm
  - Phrase understanding with semantic relationships
- **Cross-platform**: Compatible with Windows, Linux, and macOS

## Installation
```bash
git clone https://github.com/yourusername/digital_dictionary.git
cd digital_dictionary
```
## Usage
### GUI Version
```bash
python3 gui.py
```
#### Interface Guide:

**Search Box:**
- Direct word input + Enter / Search button
- Real-time prefix suggestions (double-click to select)
- Click "Correct" button for spelling suggestions
**Results Display:**
- Headword: Bold black text
- Related Words: Clickable gray links
- Definitions: Regular text formatting
### CLI Version
```bash
python3 cli.py
```
#### Interactive Commands:

|Command|Action|Example|
|:-:|:-:|:-:|
|f:word|Lookup word definition|f:dictionary|
|c:word|Get spelling suggestions|c:dictiomary|
|p:prefix|Search words by prefix|p:dict|
|e:|Exit the program|e:|
## Requirements
- Python **3.6+**
- Standard Libraries:
  - tkinter (required for **GUI version only**)
  - json, heapq, os
## Dictionary Data Format
```json
{
  "algorithm": {
    "meaning": {
      "n.": "A process or set of rules to be followed in calculations"
    },
    "phrase": {
      "algorithm design": "The process of creating mathematical processes"
    }
  }
}
```
