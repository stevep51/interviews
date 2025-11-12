import json
from pathlib import Path
from typing import Any, Sequence

## Load the data from the JSONL file
DATA_PATH = Path(__file__).resolve().parent / "data.jsonl"
with DATA_PATH.open("r", encoding="utf-8") as data_file:
    DATA = [json.loads(line) for line in data_file if line.strip()]

KNOWN_SUSPICIOUS_IPS: list[str] = [
    "45.83.91.12",
    "77.247.109.50",
    "103.150.10.88",
    "198.51.100.250",
]


def count_events_by_level(data: Sequence[dict[str, Any]], level: str) -> int:
    """
    Count how many events were emitted with the specified severity level.

    Args:
        data: Sequence of parsed event dictionaries from the proxy log.
        level: Expected value of the `level` field (for example ``\"WARN\"``).

    Returns:
        The number of log entries whose `level` field matches ``level``.
    """
    pass


def list_events_for_user(data: Sequence[dict[str, Any]], user_id: str) -> list[dict[str, Any]]:
    """
    Collect every event that references the provided user identifier.

    Args:
        data: Sequence of parsed event dictionaries from the proxy log.
        user_id: Value to match against the `user_id` key inside each event.

    Returns:
        A list of matching event dictionaries retaining their original structure.
    """
    pass


def find_events_from_suspicious_ips(
    data: Sequence[dict[str, Any]], suspicious_ips: Sequence[str]
) -> list[dict[str, Any]]:
    """
    Return the subset of events that originate from known suspicious IP addresses.

    Args:
        data: Sequence of parsed event dictionaries from the proxy log.
        suspicious_ips: IP addresses that should be treated as malicious indicators.
            Use ``KNOWN_SUSPICIOUS_IPS`` as a starting point.

    Returns:
        A list of event dictionaries whose ``src_ip`` value matches any entry in
        ``suspicious_ips``.
    """
    pass
