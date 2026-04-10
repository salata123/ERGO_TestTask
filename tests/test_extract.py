import os
from app.pdf_ops import extract_attachments


def test_extract_attachments(tmp_path):
    # Arrange
    pdf_file = tmp_path / "file.pdf"
    output_dir = tmp_path / "attachments"

    from pypdf import PdfWriter

    writer = PdfWriter()

    writer.add_blank_page(width=72, height=72)

    writer.add_attachment(
        "test.txt",
        b"hello"
    )

    with open(pdf_file, "wb") as f:
        writer.write(f)

    # Act
    extract_attachments(
        str(pdf_file),
        str(output_dir),
        password=None
    )

    # Assert
    files = os.listdir(output_dir)
    assert len(files) == 1
