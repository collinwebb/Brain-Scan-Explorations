"""
write things!!
"""

from mne import Epochs, find_events
from mne.io import read_raw_edf

###############
# Import Data #
###############

# Define Paths
# TODO: automate based on brefix names (with muse prefixes are before the underscore).
filePath = "MuseData/"
beforePracticeFile = filePath + "Before Mindfulness_Muse-BE53_2019-01-26--15-44-02_1548546368888.edf"
afterPracticeFile = filePath + "Post Muse 5 min v4.2_Muse-BE53_2019-01-26--15-56-03_1548547065702.edf"


# Read Raw Data
# TODO 1: This should be all that is needed. There is a chance I need to mess with the
# channels or annotate the data to get at least more detailed readings.
# TODO 2 automate based on Path automation above.

beforePracticeRawData = read_raw_edf(beforePracticeFile, stim_channel="auto", preload=True)
afterPracticeRawData = read_raw_edf(afterPracticeFile, stim_channel="auto", preload=True)

# this is just for beforePracticeRawData

#############
# Read Data #
#############

beforePracticeRawData = beforePracticeRawData.pick_types(eeg=True, exclude='bads')

sampleFrequency = beforePracticeRawData.info["sfreq"]

bands=[
    (.5, 4, "Delta"),
    (4, 8, "Theta"),
    (8, 12, "Alpha"),
    (12, 30, "Beta"),
    (30, 100, "Gamma")
]

for fmin, fmax, name in bands:
    filteredData = beforePracticeRawData.filter(fmin, fmax)
    print(fmin, fmax, name)

    flattenedData = [y for x in filteredData.get_data() for y in x]
    averageData = sum(flattenedData) / float(len(flattenedData))
    print(averageData)

    # filteredData.plot_psd()
