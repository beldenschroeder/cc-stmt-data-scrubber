Run the credit card statement data scrubber using the configuration in `.env`.

Steps:
1. Read `.env` to show the user the current configuration (CC_TYPE, INPUT_FILE, OUTPUT_FILE).
2. Confirm the input file exists. If it does not, tell the user and stop.
3. Run `uv run cc-scrubber` and stream the output to the user.
4. Report whether the run succeeded and where the output file was written.
