from __future__ import annotations

from pathlib import Path

import httpx
import pytest

from proxyrequest_sdk import AsyncClient, Client

BASE_URL = "https://api.proxyrequest.com/api/v1"
PDF = b"%PDF-1.7\nexample"


def response(_: httpx.Request) -> httpx.Response:
    return httpx.Response(
        200,
        content=PDF,
        headers={
            "Content-Type": "application/pdf",
            "Content-Disposition": 'attachment; filename="invoice-42.pdf"',
        },
    )


def test_invoice_pdf_download_and_safe_save(tmp_path: Path) -> None:
    http_client = httpx.Client(base_url=BASE_URL, transport=httpx.MockTransport(response))
    client = Client.with_api_key("key", http_client=http_client)
    download = client.download_invoice_pdf("42")

    assert download.content == PDF
    assert download.filename == "invoice-42.pdf"
    assert download.content_type == "application/pdf"
    destination = download.save(tmp_path)
    assert destination.read_bytes() == PDF
    with pytest.raises(FileExistsError):
        download.save(destination)


@pytest.mark.asyncio
async def test_async_invoice_pdf_download() -> None:
    http_client = httpx.AsyncClient(base_url=BASE_URL, transport=httpx.MockTransport(response))
    client = AsyncClient.with_api_key("key", http_client=http_client)
    download = await client.download_invoice_pdf("42")
    assert download.content == PDF
    await http_client.aclose()
