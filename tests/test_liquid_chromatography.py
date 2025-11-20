from proteosim.liquid_chromatography import (
    select_retention_time_window,
    predict_lc_retention_times
)

from pyteomics import achrom

def test_predict_lc_retention_times():
    # Test-Peptide-Liste
    test_peptides = ["AAAAAA", "PPPPPP", "CCCCCC"]

    # Erwartete Werte berechnen und auf 2 Nachkommastellen runden
    expected = {}
    for pep in test_peptides:
        expected[pep] = round(achrom.calculate_RT(pep, achrom.RCs_guo_ph7_0), 2)

    # Funktion aufrufen
    actual = predict_lc_retention_times(test_peptides)

    # Prüfen, ob die Ausgabe stimmt
    assert actual == expected

# Test ausführen
test_predict_lc_retention_times()


def test_select_retention_time_window():
    peptide_rt_map = {"AAAAAA": 4.0, "PPPPPP":10.0, "CCCCCC":13.0}
    selected = select_retention_time_window(peptide_rt_map, lower_ret_time=5, upper_ret_time=15)

    assert selected == {"PPPPPP":10.0, "CCCCCC":13.0}

test_select_retention_time_window()