import os
from pypdf import PdfReader, PdfWriter
from app.errors import PdfProcessingError, PasswordError


def merge_pdfs(files, output, password=None):
    writer = PdfWriter()

    if not files:
        raise PdfProcessingError("No PDF files to merge")

    for file in files:
        reader = PdfReader(file)

        if reader.is_encrypted:
            if not password:
                raise PasswordError("Password required")

            if reader.decrypt(password) == 0:
                raise PasswordError("Wrong password")

        for page in reader.pages:
            writer.add_page(page)

    with open(output, "wb") as f:
        writer.write(f)


def extract_attachments(file, output_dir, password=None):

    os.makedirs(output_dir, exist_ok=True)

    reader = PdfReader(file)

    if reader.is_encrypted:
        if not password:
            raise PasswordError("Password required")

        if reader.decrypt(password) == 0:
            raise PasswordError("Wrong password")

    attachments = reader.attachments

    saved_files = []

    for name, data in attachments.items():

        clean_name = os.path.basename(name)

        clean_name = clean_name.replace(":", "_")

        for i, content in enumerate(data):

            path = os.path.join(output_dir, f"{i}_{clean_name}")

            with open(path, "wb") as f:
                f.write(content)

            saved_files.append(path)

    return saved_files
