# FPL Rank Summary

This Python 3.10 program uses the FPL API along with visualisation tools like Matplotlib to display your Gameweek rank over the season.

## Installation

Download the Python fplRankSummary.py file along with the requirements.txt

## Team ID?

This is required for the program to fetch your FPL details via the API.
Your team ID can be found on the Fantasy Premier league website, after logging in and either:
- Going to the Points tab
- Going to Pick Team --> Gameweek History Tab

The ID be a multi digit value, such as 6740264

For more details on getting your ID:  https://www.premierfantasytools.com/how-to-check-your-fpl-id/

## Usage

After running the program, enter your Team ID when prompted.

Run the file using:

```bash
Python fplRankSummary.py
```
Information on Rank and Gameweek can also be printed in table form by uncommenting the line:

```python
print(df)
```

More improvements and work on this program will be done in the future.