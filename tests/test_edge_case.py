import pytest
from app.pdf_ops import merge_pdfs


def test_merge_empty_list(tmp_path):
    # Arrange
    output = tmp_path / "merged.pdf"

    # Act + Assert
    with pytest.raises(Exception):
        merge_pdfs(
            [],
            str(output),
            password=None
        )
