# Flow Log Parser

## Overview

This program parses a flow log file, maps each row to a tag based on a lookup table, and generates an output file with statistics on tag and port/protocol combinations. The program is designed to handle flow logs in the default format (version 2 only) and uses a CSV file as a lookup table to assign tags to specific `dstport` and `protocol` combinations.

## Features

- **Tag Assignment:** Assigns tags to each flow log entry based on the `dstport` and `protocol` values using a lookup table.
- **Tag Counts:** Counts and lists the number of occurrences for each tag.
- **Port/Protocol Combination Counts:** Counts and lists the number of occurrences for each unique `port/protocol` combination.

## Requirements

- Python 3.x
- No external libraries or packages (only Python's built-in modules are used).

## Assumptions

- The program only supports the default flow log format and version 2 logs.
- The input flow log file and the lookup table file must be in plain text (ASCII).
- Case sensitivity is not required for matching tags; the program handles matching in a case-insensitive manner.
- The lookup file can contain up to 10,000 mappings, and the flow log file can be up to 10 MB in size.
- The program assumes that the protocol numbers map to the following protocol names:
  - `6` → `tcp`
  - `17` → `udp`
  - `1` → `icmp`
  - Any other protocol numbers are treated as `other`.
- Any flow log entry that does not match a `dstport` and `protocol` combination in the lookup table is tagged as `Untagged`.

## Usage

### Input Files

- **lookup_table.csv**: CSV file containing the mapping of `dstport`, `protocol`, and `tag`.
- **flow_logs.txt**: Text file containing the flow logs in default format (version 2).

### Output File

- **output.txt**: Text file containing the counts of tags and port/protocol combinations.

### Example Command

To run the program, use the following command:

```bash
python3 flow_log_parser.py
