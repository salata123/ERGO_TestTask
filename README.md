## Build Docker Image

docker build -t test-task .

---

## Run — Extract/Merge Attachments

docker run -e OPERATION=extract test-task

docker run -e OPERATION=merge test-task

For passworded files add an environment variable: -e PDF_PASSWORD=*your password here*

Example of full Docker line (example files included in this project are procetced with password "PDF_PASSWORD"):

docker run -e OPERATION=merge -e PDF_PASSWORD=PDF_PASSWORD test-task

---

## Environment Variables

OPERATION

merge | extract

INPUT_DIR

default:
/data/input

OUTPUT_FILE

default:
/data/output/merged.pdf

OUTPUT_DIR

default:
/data/output/attachments

PDF_PASSWORD

password for encrypted PDFs

---

## Input Directory

Mount PDFs into:

/data/input

Example:

test_files/
test1.pdf
teste2.pdf

---

## Output

Merge:

/data/output/merged.pdf

Extract:

/data/output/attachments/

---

## Run Tests

pytest -v

---

## Run Tests in Docker

docker run test-task pytest

---

## Exit Codes

0 success  
1 processing error  
2 config error  
3 password error  

---
