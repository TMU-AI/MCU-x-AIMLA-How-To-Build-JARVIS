#!/usr/bin/env python3
"""list_available_models.py

Lists available models for the current OpenAI account.

Requirements (see `requirements.txt`):
- `python-dotenv` to load `.env`
- `langchain-openai` (LangChain) to create the OpenAI client

Environment:
- `OPENAI_API_KEY` in `.env`
"""

from __future__ import annotations

import os
import sys
from datetime import datetime

from dotenv import load_dotenv
from openai import APIConnectionError, APIError, AuthenticationError

try:
    # LangChain integration; preferred path.
    from langchain_openai import ChatOpenAI
except Exception:  # pragma: no cover
    ChatOpenAI = None  # type: ignore[assignment]


def _print_api_key_missing_help() -> None:
    print("Error: OPENAI_API_KEY not found.")
    print("Create a .env file in the project root containing:")
    print("  OPENAI_API_KEY=your-api-key-here")


def _print_invalid_api_key_help() -> None:
    print("Error: Authentication failed (invalid or revoked API key).")
    print("Verify OPENAI_API_KEY in your .env file and try again.")


def _list_models_via_langchain(api_key: str):
    """Return a list of model ids.

    We use LangChain to construct the OpenAI client when possible, but the
    LangChain wrapper's underlying client is not guaranteed to expose the full
    OpenAI Models API.
    """

    if ChatOpenAI is None:
        raise RuntimeError(
            "langchain-openai is not installed. Install dependencies from requirements.txt."
        )

    # Use LangChain for credential/config wiring.
    llm = ChatOpenAI(api_key=api_key)

    # Best-effort: if the wrapped client exposes `models.list()`, use it.
    client = getattr(llm, "client", None)
    if client is not None and hasattr(client, "models"):
        models_page = client.models.list()
        return [m.id for m in models_page.data]

    # Fallback: use the official OpenAI SDK for model listing.
    from openai import OpenAI

    sdk_client = OpenAI(api_key=api_key)
    models_page = sdk_client.models.list()
    return [m.id for m in models_page.data]


def main() -> int:
    load_dotenv()

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        _print_api_key_missing_help()
        return 1

    try:
        model_ids = sorted(_list_models_via_langchain(api_key=api_key))

        print(f"Available Models ({len(model_ids)} total):\n")
        print(f"{'Model ID':<48} {'Created':<19} {'Owned By':<24}")
        print("-" * 96)

        # Created/owned_by are only available when using the full Models API.
        # When falling back to ids-only, print dashes for those columns.
        for mid in model_ids:
            print(f"{mid:<48} {'-':<19} {'-':<24}")
        return 0
    except AuthenticationError:
        _print_invalid_api_key_help()
        return 1
    except APIConnectionError as e:
        print(f"Error: Network/connection problem while calling the API: {e}")
        print("Check your internet connection (and any proxy/firewall) and try again.")
        return 1
    except APIError as e:
        print(f"Error: OpenAI API error: {e}")
        return 1
    except Exception as e:
        print(f"Error: Unexpected failure: {e}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
