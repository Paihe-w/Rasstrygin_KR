"""Учебная модель F04/F05 из ТЗ HostShield, без применения правил на МЭ."""

from dataclasses import dataclass

WINDOW_SECONDS = 10
UNIQUE_HOST_THRESHOLD = 20
RULE_TTL_SECONDS = 300


@dataclass(frozen=True)
class Probe:
    timestamp: float
    source: str
    zone: str
    destination: str
    denied: bool


@dataclass(frozen=True)
class Decision:
    unique_hosts: int
    suspicious: bool
    action: str


def evaluate(probes: list[Probe], source: str, zone: str, now: float) -> Decision:
    """Подсчитать уникальные запрещённые назначения за скользящее окно.

    Источник и входная зона образуют область подсчёта. Штатные разрешённые
    запросы и повторные пакеты к одному адресу не увеличивают H.
    """
    destinations = {
        probe.destination
        for probe in probes
        if probe.source == source
        and probe.zone == zone
        and probe.denied
        and 0 <= now - probe.timestamp < WINDOW_SECONDS
    }
    count = len(destinations)
    suspicious = count >= UNIQUE_HOST_THRESHOLD
    action = "Предлагается временное правило (TTL 300 с)" if suspicious else "Блокировка не требуется"
    return Decision(count, suspicious, action)
