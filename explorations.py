"""
write things!!
"""

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

beforePracticeRawData = read_raw_edf(beforePracticeFile, stim_channel='auto', preload=True)
afterPracticeRawData = read_raw_edf(afterPracticeFile, stim_channel='auto', preload=True)

# (optional exploratory) print raw data info to see what is going on.
# print(beforePracticeRawData.info)

#############
# Read Data #
#############

#
#TODO 1: make this a class that can be called with more general parameters and compared.
#TODO 2: allow for further refining based on events ====>> raw.find_edf_events()
# (no events used in initial test data).

sfreq = beforePracticeRawData.info["sfreq"]
pickedChannels = beforePracticeRawData.pick_types(eeg=True, stim=False, exclude='bads')

print(pickedChannels)
