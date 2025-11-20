from pyteomics import achrom

def predict_lc_retention_times(peptides):
    """
    Add a short description here.

    Parameters
    peptides: list of str
      list of peptide sequences


    Returns
    dict of {str: float}
      dictionary mapping each peptide to its retention time
    """
    retention_times = {} #initialize dictionary

    for pep in peptides:
        relative_RT = achrom.calculate_RT(pep, achrom.RCs_guo_ph7_0) #berechnet retention time für jede Sequenz
        retention_times[pep] = float(round(relative_RT, 2)) #rundet auf zwei nachkommastellen
    return retention_times

import matplotlib.pyplot as plt

import matplotlib.pyplot as plt

def plot_retention_time(retention_times, resolution=30):
    """
    Plot a histogram of LC retention times.

    Parameters
    ----------
    retention_times : list or dict
        A list of numeric retention times, or a dict mapping peptide -> RT.
    resolution : int
        Number of bins for the histogram.
    """

    plt.figure()

    # Wenn dict → nur numerische Werte extrahieren:
    if isinstance(retention_times, dict):
        values = list(retention_times.values())
    else:
        values = retention_times

    plt.hist(values, bins=resolution, color = 'lavender', edgecolor='black')

    plt.xlabel("Retention time")
    plt.ylabel("Frequency")
    plt.title("Simulated LC gradient")

    plt.show()



def select_retention_time_window(peptide_rt_map, lower_ret_time, upper_ret_time):
    """
    Select peptides whose retention times fall within a specified LC window.

    Parameters
    ----------
    peptide_rt_map : dict
        Dictionary mapping peptide sequences (str) to retention times.
        The retention time can be a single float or a list of floats.
    lower_ret_time : float
        Lower bound of the retention time window.
    upper_ret_time : float
        Upper bound of the retention time window.

    Returns
    -------
    dict
        Dictionary of peptides within the retention time window, mapping
        peptide -> retention time (float or list of floats).
    """
    selected = {
      peptide: rt
      for peptide, rt in peptide_rt_map.items()
      if lower_ret_time <= rt <= upper_ret_time
    }
    return selected
