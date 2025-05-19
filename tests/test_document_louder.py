import pytest
from services.document_loader import load_documents
from pathlib import Path

def test_load_txt_document(tmp_path):
    # Create a temp .txt file
    test_file = tmp_path / "test.txt"
    test_file.write_text("This is a test document.")

    docs = load_documents(str(test_file))

    assert len(docs) == 1
    assert "This is a test document." in docs[0].page_content

def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        load_documents("non_existent.txt")

def test_unsupported_file_type(tmp_path):
    bad_file = tmp_path / "test.docx"
    bad_file.write_text("Unsupported type")

    with pytest.raises(ValueError):
        load_documents(str(bad_file))
