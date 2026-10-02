from django.http import HttpResponseBadRequest
from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST

from .detector import Probe, evaluate


def _scenario(name: str):
    now = 1000.0
    source = "198.51.100.24"
    zone = "external" if name != "guest" else "guest"
    if name == "normal":
        probes = [Probe(now - 2, source, zone, "10.20.0.10", False)]
        title = "Штатный пользователь"
        description = "HTTPS-запрос к публичному шлюзу разрешён. Запрещённых направлений нет."
    elif name in {"external", "guest"}:
        probes = [Probe(now - 2 + i * 0.1, source, zone, f"10.20.0.{i+1}", True) for i in range(20)]
        title = "Разведка из внешней сети" if name == "external" else "Разведка из гостевого сегмента"
        description = "20 различных внутренних адресов опрошены за 10 секунд."
    elif name == "repeat":
        probes = [Probe(now - 2 + i * 0.1, source, zone, "10.20.0.7", True) for i in range(20)]
        title = "Повторные пакеты"
        description = "20 попыток к одному адресу: H увеличивается только один раз."
    else:
        raise ValueError("unknown scenario")
    decision = evaluate(probes, source, zone, now)
    return {
        "key": name, "title": title, "description": description,
        "source": source, "zone": zone, "events": len(probes),
        "unique_hosts": decision.unique_hosts,
        "suspicious": decision.suspicious, "action": decision.action,
    }


def dashboard(request):
    key = request.session.get("scenario", "normal")
    try:
        result = _scenario(key)
    except ValueError:
        result = _scenario("normal")
    return render(request, "security_console/index.html", {"result": result})


@require_POST
def run_scenario(request, scenario):
    if scenario not in {"normal", "external", "guest", "repeat"}:
        return HttpResponseBadRequest("Неизвестный сценарий")
    request.session["scenario"] = scenario
    return redirect("dashboard")
