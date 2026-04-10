# PDF Processing Service – Design Document

Hello ERGO team,
Thank You once again for considering me for this role :)
Here is a brief design file You asked.

## Architecture Overview

The service performs one of two operations:

- Merge multiple PDF files
- Extract attachments from PDF files

The application is built with a simple architecture:

app/
│
├── app.py
├── config.py
├── pdf_ops.py
├── errors.py
└── logger.py

Execution Flow:

1. Load configuration from environment variables
2. Scan input directory for PDF files
3. Execute selected operation (merge or extract)
4. Upload results to output directory
5. Return exit code

The application runs once with some environment variables

---

## Library Choices and Tradeoffs

### pypdf

The simplest library for reading, merging, extracting attachments and handling encrypted files tested million times. It was the best option for me, because I had very limited time to do this task and still I can see a lot of things to improve. I wanted to find something to test heavier files, but sadly there was no more time left for research.

---

## How Attachments Are Extracted

Attachments are accessed using:

reader.attachments

This returns:

{
  filename: [binary_data]
}

The application:

1. Iterates over attachments dictionary
2. Cleans filename
3. Creates output path
4. Writes binary content to disk

Example:

PDF:
report.pdf
 └── attachment: image.jpg

Output:

attachments/
 └── 0_image.jpg

---

## Input Parsing and Validation

Input directory is configured via:

INPUT_DIR=/data/input

The application:

- scans directory
- filters .pdf files
- validates if file list is not empty

Validation errors:

- No PDF files found
- Invalid operation
- Missing directories

---

## Handling Password Protected PDFs

The application checks:

reader.is_encrypted

If encrypted:

reader.decrypt(password) with environment variable

Password provided via:

PDF_PASSWORD env variable

Behavior:

Valid password → file processed  
Invalid password → PasswordError  
No password → PasswordError  

For password usage check README file

---

## Error Handling Strategy

Custom exceptions:

ConfigError  
PasswordError  
PdfProcessingError  

Main entrypoint catches:

- configuration errors
- processing errors
- unexpected errors

Application returns exit codes:

0 success  
1 processing error  
2 config error  
3 password error  

This allows workflow systems to react accordingly.

---

## Possible Improvements

Future improvements:

- other libraries testing for heavier files
- metrics endpoint
- S3 input/output support
- retry mechanism
- progress logging
- more throughful tests

---

## Thank You for the opportunity and I'm sending You my best regards!
## Michał Lisek
