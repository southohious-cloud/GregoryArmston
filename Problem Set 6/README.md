# CS50P - Problem Set 6 Logic Pattern Summary Sheet

1. lines.py - Print Lines Without Comments
Logic pattern: filtering + stripping
· Read file line by line
· Strip whitespace
· Skip blank lines
· Skip lines starting with "#"
· Print remaining lines

2. shirt.py - Overlay Shirt Image
Logic pattern: image processing with PIL
· Validate CLI args (input + output)
· Open input image
· Open shirt image
· Resize input to shirt size
· Paste shirt on top using mask
· Save output image

3. pizza.py - CSV to Table
Logic pattern: CSV parsing
· Validate CLI args
· Open CSV file
· Use csv.reader or DictReader
· Print table in formatted columns

4. scourgify.py - Name Reformatting
Logic pattern: CSV transform
· Validate CLI args
· Read input CSV
· Split "last, first" into fields
· Write output CSV with first and last columns

5. shirtificate.py - Certificate Generator
Logic pattern: text overlay on image
· Prompt for name
· Open certificate template
· Use ImageDraw to write name
· Center text horizontally
· Save final image