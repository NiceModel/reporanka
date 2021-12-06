"""Module for specifying the environmental variables."""
import os

DIRNAME = os.path.dirname(__file__)

DB_NAME = "items.csv"
DB_PATH = os.path.join(DIRNAME, "data", DB_NAME)

TEST_DB = "test_items.csv"
TEST_DB_PATH = os.path.join(DIRNAME, "data", TEST_DB)

INSTRUCTIONS = (
            "\nValitse toiminto"
            "\n (1) lisää"
            "\n (2) listaa"
            "\n (0) lopeta\n")
