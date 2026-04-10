import sys
import os

from app.config import load_config
from app.pdf_ops import merge_pdfs, extract_attachments
from app.logger import setup_logger, log_json
from app.errors import ConfigError, PasswordError


logger = setup_logger()


def main():
    try:
        config = load_config()

        input_dir = config["input_dir"]
        output_dir = config["output_dir"]
        operation = config["operation"]
        password = config["password"]

        os.makedirs(os.path.dirname(config["output_file"]), exist_ok=True)

        os.makedirs(config["output_dir"], exist_ok=True)

        os.makedirs(
            os.path.dirname(config["attachments_merged_output"]),
            exist_ok=True
        )
        
        files = []

        for file in os.listdir(input_dir):

            if file.lower().endswith(".pdf"):

                full_path = os.path.join(input_dir, file)

                files.append(full_path)

        if not files:
            raise ConfigError("No PDF files found in input directory")

        log_json(logger, "info", "pdf files discovered", count=len(files))

        extracted_files = []

        if operation == "merge":

            merge_pdfs(
                files,
                config["output_file"],
                password
            )

            log_json(logger, "info", "merge completed")

        elif operation == "extract":

            for file in files:
                extract_attachments(
                    file,
                    output_dir,
                    password
                )

            log_json(logger, "info", "extraction completed")

        sys.exit(0)

    except ConfigError as e:
        log_json(logger, "error", "config error", error=str(e))
        sys.exit(2)

    except PasswordError as e:
        log_json(logger, "error", "password error", error=str(e))
        sys.exit(3)

    except Exception as e:
        log_json(logger, "error", "processing error", error=str(e))
        sys.exit(1)


if __name__ == "__main__":
    main()
