import os
from app.errors import ConfigError


def load_config():
    config = {
        "operation": os.getenv("OPERATION", "merge"),
        
        "input_dir": os.getenv("INPUT_DIR", "/data/input"),

        "output_file": os.getenv("OUTPUT_FILE", "/data/output/merged.pdf"),

        "output_dir": os.getenv("OUTPUT_DIR", "/data/output/attachments"),

        "attachments_merged_output": os.getenv(
           "ATTACHMENTS_MERGED_OUTPUT",
           "/data/output/attachments_merged.pdf"
        ),

        "password": os.getenv("PDF_PASSWORD"),
    }

    validate(config)

    return config


def validate(config):

    if config["operation"] not in ["merge", "extract"]:
        raise ConfigError("OPERATION must be merge or extract")
