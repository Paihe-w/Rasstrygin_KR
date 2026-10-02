from django.test import SimpleTestCase
from django.urls import reverse

from .detector import Probe, evaluate


class DetectorTests(SimpleTestCase):
    def test_twenty_distinct_denied_hosts_trigger(self):
        events = [Probe(99, "source", "external", f"10.0.0.{i}", True) for i in range(20)]
        result = evaluate(events, "source", "external", 100)
        self.assertEqual(result.unique_hosts, 20)
        self.assertTrue(result.suspicious)

    def test_retries_allowed_and_other_zones_do_not_count(self):
        events = [Probe(99, "source", "external", "10.0.0.1", True) for _ in range(20)]
        events += [Probe(99, "source", "guest", "10.0.0.2", True)]
        events += [Probe(99, "source", "external", "10.0.0.3", False)]
        events += [Probe(80, "source", "external", "10.0.0.4", True)]
        result = evaluate(events, "source", "external", 100)
        self.assertEqual(result.unique_hosts, 1)
        self.assertFalse(result.suspicious)

    def test_page_and_scenario(self):
        self.assertEqual(self.client.get(reverse("dashboard")).status_code, 200)
        self.client.post(reverse("run_scenario", args=["external"]))
        page = self.client.get(reverse("dashboard"))
        self.assertContains(page, "20 различных")
        self.assertContains(page, "Предлагается временное правило")
