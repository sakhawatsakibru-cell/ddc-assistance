"""Streamlit entry point for the project bundled in ddc-assistant-github.zip."""

from __future__ import annotations

import os
import runpy
import sys
import tempfile
import zipfile
from pathlib import Path

import streamlit as st


ROOT = Path(__file__).resolve().parent
ARCHIVE = ROOT / "ddc-assistant-github.zip"


def main() -> None:
    if not ARCHIVE.is_file():
        st.error("The project archive ddc-assistant-github.zip is missing.")
        st.stop()

    with tempfile.TemporaryDirectory(prefix="ddc-assistant-") as temp_dir:
        project_dir = Path(temp_dir)
        with zipfile.ZipFile(ARCHIVE) as archive:
            # Refuse unsafe archive paths before extracting the trusted project bundle.
            for member in archive.infolist():
                destination = (project_dir / member.filename).resolve()
                if not destination.is_relative_to(project_dir.resolve()):
                    st.error("The project archive contains an unsafe file path.")
                    st.stop()
            archive.extractall(project_dir)

        bundled_app = project_dir / "app.py"
        if not bundled_app.is_file():
            st.error("The project archive does not contain its expected app.py file.")
            st.stop()

        old_cwd = Path.cwd()
        sys.path.insert(0, str(project_dir))
        try:
            # Preserve the bundle's expected relative file paths and local imports.
            os.chdir(project_dir)
            runpy.run_path(str(bundled_app), run_name="__main__")
        finally:
            os.chdir(old_cwd)
            if sys.path and sys.path[0] == str(project_dir):
                sys.path.pop(0)


main()
