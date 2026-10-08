"""Små kontroller av grenser og kjente resultater. Kjør python -m unittest -v."""
import unittest
from datetime import datetime, timedelta
from pathlib import Path
from les_data import les_data, velg_aar
from ski_og_plot import skidager
from vekst_og_varme import plantevekst, varme_dager, dagsvekst, avansert_vekst
from torke import lengste_torke


def dag(dato, **verdier):
    return {"dato": datetime.fromisoformat(dato), "sno": None, "nedbor": None,
            "temperatur": None, "maks": None, "vind": None, **verdier}


class Grenser(unittest.TestCase):
    def test_skisesong_og_20_cm(self):
        data = [dag("2019-10-31", sno=50), dag("2019-11-01", sno=20),
                dag("2020-05-31", sno=21), dag("2020-06-01", sno=50),
                dag("2020-02-29", sno=19)]
        self.assertEqual(skidager(data, 2020), (2, 210, 213))

    def test_strenge_overlappende_varmegrenser(self):
        data = [dag(f"2020-01-{i:02}", maks=t)
                for i, t in enumerate([20, 20.1, 25, 25.1, 30, 30.1], 1)]
        self.assertEqual(varme_dager(data, 2020), ([5, 3, 1], 360))

    def test_vekst_og_frost(self):
        data = [dag(f"2020-01-{i:02}", temperatur=t)
                for i, t in enumerate([-2, 0, 5, 6, 10], 1)]
        self.assertEqual(plantevekst(data, 2020), (6, 361))
        self.assertEqual([dagsvekst(t) for t in [-2, 0, 5, 6]], [-2, 0, 0, 1])

    def test_torke_brudd_og_siste_periode(self):
        data = [dag("2020-01-01", nedbor=0), dag("2020-01-02", nedbor=None),
                dag("2020-01-03", nedbor=0), dag("2020-01-05", nedbor=0),
                dag("2020-01-06", nedbor=0)]
        self.assertEqual(lengste_torke(data),
                         (2, datetime(2020, 1, 5), datetime(2020, 1, 6)))
        self.assertEqual(lengste_torke([]), (0, None, None))

    def test_i_frost_topp_og_fast_slutt(self):
        dager = velg_aar([], 2020)
        for d in dager:
            d["temperatur"] = 0
        endringer = {datetime(2020, 4, 1): -2, datetime(2020, 4, 2): 10,
                     datetime(2020, 4, 3): -1}
        for d in dager:
            d["temperatur"] = endringer.get(d["dato"], 0)
        april, beste, fast = avansert_vekst(dager, 2020)
        self.assertEqual(april, (3, datetime(2020, 4, 2), 2))
        self.assertEqual(beste, (5, datetime(2020, 4, 2), datetime(2020, 4, 2)))
        self.assertEqual(fast, (4, datetime(2020, 4, 2)))
        dager[0]["temperatur"] = None
        with self.assertRaises(ValueError):
            avansert_vekst(dager, 2020)


class Filkontroll(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rot = Path(__file__).resolve().parent / "data"
        cls.data = les_data(cls.rot / "sinnes_2014_2025_med_makstemperatur.csv")

    def test_filer_samsvarer(self):
        grunn = les_data(self.rot / "sinnes_2014_2025.csv")
        self.assertEqual(len(self.data), 4383)
        self.assertEqual(len(grunn), 4335)
        self.assertEqual(grunn[-1]["dato"], datetime(2025, 11, 13))
        oppslag = {d["dato"]: d for d in self.data}
        for a in grunn:
            b = oppslag[a["dato"]]
            self.assertEqual({k: v for k, v in a.items() if k != "maks"},
                             {k: v for k, v in b.items() if k != "maks"})
        self.assertTrue(all(b["dato"] - a["dato"] == timedelta(days=1)
                            for a, b in zip(self.data, self.data[1:])))

    def test_referanse_2020(self):
        self.assertEqual(skidager(self.data, 2020), (77, 0, 213))
        self.assertAlmostEqual(plantevekst(self.data, 2020)[0], 936.7)
        self.assertEqual(varme_dager(self.data, 2020), ([31, 8, 0], 0))
        self.assertEqual(lengste_torke(self.data),
                         (24, datetime(2018, 5, 5), datetime(2018, 5, 28)))


if __name__ == "__main__":
    unittest.main()
