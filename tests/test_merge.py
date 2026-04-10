import os
from app.pdf_ops import merge_pdfs
from app.errors import PdfProcessingError, PasswordError


def test_merge_pdfs(tmp_path):
    # Arrange
    input1 = tmp_path / "file1.pdf"
    input2 = tmp_path / "file2.pdf"
    output = tmp_path / "merged.pdf"

    from pypdf import PdfWriter

    writer = PdfWriter()
    writer.add_blank_page(width=72, height=72)
    with open(input1, "wb") as f:
        writer.write(f)

    writer = PdfWriter()
    writer.add_blank_page(width=72, height=72)
    with open(input2, "wb") as f:
        writer.write(f)

    # Act
    merge_pdfs(
        [str(input1), str(input2)],
        str(output),
        password=None
    )

    # Assert
    assert os.path.exists(output)
