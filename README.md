# DDC Assistance — Streamlit

This repository currently stores the application source in `ddc-assistant-github.zip`. The root `app.py` extracts that bundle into a temporary directory and runs its included Streamlit app, so the repository can be launched directly with Streamlit Community Cloud or locally.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
streamlit run app.py
```

If the app uses Gemini, provide the API key as a Streamlit secret. For local development, create `.streamlit/secrets.toml` (do not commit it):

```toml
GEMINI_API_KEY = "your-api-key"
```

On Streamlit Community Cloud, add the same key under **App settings → Secrets**. Keep API keys out of source code and commits.

## Deploy

Create a Streamlit Community Cloud app for this repository and set the main file path to `app.py`. The launcher uses the project and relative paths from the bundled archive. If you update the project archive, make sure its `app.py` and supporting files are included.

The root `requirements.txt` lists the app's primary runtime packages. If you add dependencies to the bundled project, add them to the root requirements file as well so Streamlit Cloud installs them.
